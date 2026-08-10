document.addEventListener("DOMContentLoaded", () => {
  const cacheBuster = `?v=${new Date().getTime()}`;
  let tabelasReferencia = [];
  let parametrosGerais = {
    Deducao_Dependente: 189.59,
    Adicional_Limite: 50000,
    Adicional_Aliquota: 10
  };

  const UI = {
    form: document.getElementById('irpfForm'),
    rendimentoBase: document.getElementById('rendimentoBase'),
    dependentes: document.getElementById('dependentes'),
    pensao: document.getElementById('pensao'),
    outrasDeducoes: document.getElementById('outrasDeducoes'),
    lucrosDividendos: document.getElementById('lucrosDividendos'),
    btnLimpar: document.getElementById('btnLimpar'),
    btnImprimir: document.getElementById('btnImprimir'),
    loadingIndicator: document.getElementById('loadingIndicator'),
    resultadoContainer: document.getElementById('resultadoContainer'),
    valBaseCalculo: document.getElementById('valBaseCalculo'),
    valImpostoPagar: document.getElementById('valImpostoPagar'),
    valRendaLiquida: document.getElementById('valRendaLiquida'),
    resultadoTabela: document.getElementById('resultadoTabela'),
    dataHoraImpressao: document.getElementById('data-hora-impressao')
  };

  // Funções de formatação
  function formatCurrency(value) {
    return value.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
  }

  function parseCurrency(valString) {
    if (!valString) return 0;
    const cleanStr = valString.replace(/[R$\s.]/g, '').replace(',', '.');
    const parsed = parseFloat(cleanStr);
    return isNaN(parsed) ? 0 : parsed;
  }

  function applyMoneyMask(input) {
    let value = input.value.replace(/\D/g, '');
    if (value === "") {
      input.value = "";
      return;
    }
    value = (parseInt(value, 10) / 100).toFixed(2);
    input.value = value.replace(".", ",").replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1.");
    input.value = "R$ " + input.value;
  }

  [UI.rendimentoBase, UI.pensao, UI.outrasDeducoes, UI.lucrosDividendos].forEach(el => {
    el.addEventListener('input', (e) => applyMoneyMask(e.target));
  });

  // Carregar dados da Planilha
  UI.loadingIndicator.style.display = 'block';
  UI.form.style.opacity = '0.5';
  
  fetch("/calculadora-ir-configuracoes.xlsx" + cacheBuster)
    .then(response => {
      if (!response.ok) throw new Error("Erro na rede ao baixar a planilha.");
      return response.arrayBuffer();
    })
    .then(data => {
      const workbook = XLSX.read(data, { type: 'array' });
      
      // Ler Aba de Tabelas de Referência
      const nomeAbaRef = workbook.SheetNames.find(n => n.trim().toLowerCase() === "tabelas_referencia");
      if (nomeAbaRef) {
        const sheetRef = workbook.Sheets[nomeAbaRef];
        const rawData = XLSX.utils.sheet_to_json(sheetRef, { defval: null });
        tabelasReferencia = rawData.map(row => ({
          faixa: row.Faixa || row.faixa,
          limite: parseFloat(row.Limite !== null && row.Limite !== undefined ? row.Limite : 99999999999),
          aliquota: parseFloat(row.Aliquota || row.aliquota || 0),
          deducao: parseFloat(row.Deducao || row.deducao || 0)
        })).sort((a, b) => a.limite - b.limite);
      }

      // Ler Aba de Parâmetros Gerais
      const nomeAbaParams = workbook.SheetNames.find(n => n.trim().toLowerCase() === "parametros_gerais");
      if (nomeAbaParams) {
        const sheetParams = workbook.Sheets[nomeAbaParams];
        const rawParams = XLSX.utils.sheet_to_json(sheetParams, { defval: null });
        rawParams.forEach(row => {
          const paramName = (row.Parametro || row.parametro || "").toString().trim();
          if (paramName) {
            parametrosGerais[paramName] = parseFloat(row.Valor || row.valor || 0);
          }
        });
      }

      UI.loadingIndicator.style.display = 'none';
      UI.form.style.opacity = '1';
    })
    .catch(err => {
      console.warn("Falha ao ler a planilha IRPF:", err.message);
      UI.loadingIndicator.innerHTML = '<p style="color:red;">Erro ao carregar configurações. Tente novamente mais tarde.</p>';
    });

  // Cálculo Principal
  function calcularIRPF() {
    const rendimento = parseCurrency(UI.rendimentoBase.value);
    const dividendos = parseCurrency(UI.lucrosDividendos.value);
    const dependentes = parseInt(UI.dependentes.value, 10) || 0;
    const pensao = parseCurrency(UI.pensao.value);
    const outrasDeducoes = parseCurrency(UI.outrasDeducoes.value);

    // 1. Deduções
    const deducaoDependentes = dependentes * parametrosGerais.Deducao_Dependente;
    const totalDeducoesCalc = deducaoDependentes + pensao + outrasDeducoes;

    // 2. Base de Cálculo do IRPF Progressivo
    let baseCalculo = rendimento - totalDeducoesCalc;
    if (baseCalculo < 0) baseCalculo = 0;

    // 3. Encontrar Faixa
    let faixaEncontrada = tabelasReferencia[tabelasReferencia.length - 1]; // Fallback pra última
    for (const f of tabelasReferencia) {
      if (baseCalculo <= f.limite) {
        faixaEncontrada = f;
        break;
      }
    }

    // 4. Calcular Imposto Progressivo
    let impostoProgressivo = (baseCalculo * (faixaEncontrada.aliquota / 100)) - faixaEncontrada.deducao;
    if (impostoProgressivo < 0) impostoProgressivo = 0;

    // 5. Adicional de Altas Rendas (PL 1087)
    const rendaTotal = rendimento + dividendos;
    let baseAdicional = 0;
    let impostoAdicional = 0;
    if (rendaTotal > parametrosGerais.Adicional_Limite) {
      baseAdicional = rendaTotal - parametrosGerais.Adicional_Limite;
      impostoAdicional = baseAdicional * (parametrosGerais.Adicional_Aliquota / 100);
    }

    // 6. Total a Pagar e Renda Líquida
    const impostoTotal = impostoProgressivo + impostoAdicional;
    
    // Renda líquida no bolso do contribuinte (receitas reais menos deduções reais e imposto)
    // O imposto come parte dos rendimentos. Pensão e Outras (como INSS) já saíram do bolso.
    const rendaLiquida = rendaTotal - pensao - outrasDeducoes - impostoTotal;

    // Atualizar UI
    UI.valBaseCalculo.textContent = formatCurrency(baseCalculo);
    UI.valImpostoPagar.textContent = formatCurrency(impostoTotal);
    UI.valRendaLiquida.textContent = formatCurrency(rendaLiquida);

    // Atualizar Tabela Detalhada
    let tabelaHTML = '';
    
    tabelaHTML += `<tr>
      <td style="padding: 0.6rem; border-bottom: 1px solid #e2e8f0;">Dedução por Dependentes (${dependentes})</td>
      <td style="padding: 0.6rem; border-bottom: 1px solid #e2e8f0; text-align: right; color: #ef4444;">- ${formatCurrency(deducaoDependentes)}</td>
    </tr>`;
    
    tabelaHTML += `<tr>
      <td style="padding: 0.6rem; border-bottom: 1px solid #e2e8f0;">Outras Deduções (Pensão + INSS)</td>
      <td style="padding: 0.6rem; border-bottom: 1px solid #e2e8f0; text-align: right; color: #ef4444;">- ${formatCurrency(pensao + outrasDeducoes)}</td>
    </tr>`;

    tabelaHTML += `<tr>
      <td style="padding: 0.6rem; border-bottom: 1px solid #e2e8f0;"><strong>Base de Cálculo do IRPF</strong></td>
      <td style="padding: 0.6rem; border-bottom: 1px solid #e2e8f0; text-align: right;"><strong>${formatCurrency(baseCalculo)}</strong></td>
    </tr>`;

    tabelaHTML += `<tr>
      <td style="padding: 0.6rem; border-bottom: 1px solid #e2e8f0;">Faixa do Imposto</td>
      <td style="padding: 0.6rem; border-bottom: 1px solid #e2e8f0; text-align: right;">Faixa ${faixaEncontrada.faixa} (${faixaEncontrada.aliquota}%)</td>
    </tr>`;

    tabelaHTML += `<tr>
      <td style="padding: 0.6rem; border-bottom: 1px solid #e2e8f0;">Imposto Progressivo (após dedução da faixa)</td>
      <td style="padding: 0.6rem; border-bottom: 1px solid #e2e8f0; text-align: right;">${formatCurrency(impostoProgressivo)}</td>
    </tr>`;

    if (impostoAdicional > 0) {
      tabelaHTML += `<tr>
        <td style="padding: 0.6rem; border-bottom: 1px solid #e2e8f0;">Adicional Altas Rendas (Sobre excedente de ${formatCurrency(baseAdicional)})</td>
        <td style="padding: 0.6rem; border-bottom: 1px solid #e2e8f0; text-align: right;">${formatCurrency(impostoAdicional)}</td>
      </tr>`;
    }

    tabelaHTML += `<tr>
      <td style="padding: 0.6rem; border-bottom: 2px solid var(--primary-color);"><strong>TOTAL DE IMPOSTO DEVIDO</strong></td>
      <td style="padding: 0.6rem; border-bottom: 2px solid var(--primary-color); text-align: right; color: var(--primary-color); font-weight: bold;">${formatCurrency(impostoTotal)}</td>
    </tr>`;

    // Alíquota Efetiva = Imposto Total / Renda Bruta Total
    const aliquotaEfetiva = rendaTotal > 0 ? (impostoTotal / rendaTotal) * 100 : 0;
    
    tabelaHTML += `<tr>
      <td style="padding: 0.6rem;">Alíquota Efetiva (Peso real do imposto)</td>
      <td style="padding: 0.6rem; text-align: right; font-weight: bold;">${aliquotaEfetiva.toFixed(2)}%</td>
    </tr>`;

    UI.resultadoTabela.innerHTML = tabelaHTML;
    UI.resultadoContainer.style.display = 'block';
  }

  UI.form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (tabelasReferencia.length === 0) return; // Aguardando carregar a planilha
    calcularIRPF();
  });

  UI.btnLimpar.addEventListener('click', () => {
    UI.form.reset();
    UI.resultadoContainer.style.display = 'none';
  });

  // Impressão
  UI.btnImprimir.addEventListener('click', () => {
    const now = new Date();
    UI.dataHoraImpressao.textContent = now.toLocaleString('pt-BR');
    window.print();
  });

});
