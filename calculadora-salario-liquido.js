document.addEventListener("DOMContentLoaded", async () => {
  let inssData = {
    parametros: {},
    tabelaProgressiva: [],
    outrasCategorias: []
  };

  let irpfData = {
    parametros: {},
    tabelaProgressiva: []
  };

  let colaboradores = [];

  // DOM Elements
  const els = {
    form: document.getElementById('calcForm'),
    nome: document.getElementById('nomeColaborador'),
    categoria: document.getElementById('categoria'),
    bruto: document.getElementById('salarioBruto'),
    dependentes: document.getElementById('dependentes'),
    pensao: document.getElementById('pensao'),
    btnLimpar: document.getElementById('btnLimpar'),
    btnAdicionar: document.getElementById('btnAdicionar'),
    resBruto: document.getElementById('resSalarioBruto'),
    resINSS: document.getElementById('resINSS'),
    resIRRF: document.getElementById('resIRRF'),
    resPensao: document.getElementById('resPensao'),
    resLiquido: document.getElementById('resLiquidoFinal'),
    displayLiquido: document.getElementById('displaySalarioLiquido'),
    tabela: document.getElementById('tabelaColaboradores'),
    tbody: document.getElementById('tbodyColaboradores'),
    tituloPainel: document.getElementById('tituloPainel')
  };

  // Formatadores
  const parseCurrency = (val) => {
    if (!val) return 0;
    if (typeof val === 'number') return val;
    let clean = val.replace(/[^\d,-]/g, '').replace(',', '.');
    let num = parseFloat(clean);
    return isNaN(num) ? 0 : num;
  };

  const formatCurrency = (val) => {
    return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(val || 0);
  };

  const formatInputCurrency = (e) => {
    let value = e.target.value.replace(/\D/g, '');
    if (value === "") { e.target.value = ""; return; }
    value = (parseInt(value) / 100).toFixed(2) + '';
    value = value.replace(".", ",");
    value = value.replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1.");
    e.target.value = 'R$ ' + value;
  };

  els.bruto.addEventListener('input', formatInputCurrency);
  els.pensao.addEventListener('input', formatInputCurrency);

  // Inicialização Dupla de Planilhas
  async function initCalculadora() {
    try {
      const configRes = await fetch('/data/configuracoes.json');
      const configJson = await configRes.json();
      const inssPath = configJson.calculadora_simples?.planilha_inss || '/calculadora-inss-configuracoes.xlsx';
      const irpfPath = configJson.calculadora_simples?.planilha_irpf || '/calculadora-ir-configuracoes.xlsx';

      await Promise.all([
        loadINSS(inssPath),
        loadIRPF(irpfPath)
      ]);

      atualizarSEO();
      popularCategorias();
      calcularEAtualizarTela();

    } catch (e) {
      console.error("Erro ao carregar dados:", e);
      els.displayLiquido.innerText = "Erro ao carregar tabelas";
    }
  }

  async function loadINSS(path) {
    const res = await fetch(path);
    const arrayBuffer = await res.arrayBuffer();
    const workbook = XLSX.read(arrayBuffer, { type: 'array' });

    // Lendo Parametros_Gerais
    const paramsSheet = workbook.Sheets['Parametros_Gerais'];
    if (paramsSheet) {
      const pData = XLSX.utils.sheet_to_json(paramsSheet);
      pData.forEach(row => {
        if (row.Parametro && row.Valor !== undefined) {
          inssData.parametros[row.Parametro.trim()] = row.Valor;
        }
      });
    }

    // Lendo Tabelas_Referencia
    const tabSheet = workbook.Sheets['Tabelas_Referencia'];
    if (tabSheet) {
      inssData.tabelaProgressiva = XLSX.utils.sheet_to_json(tabSheet).map(row => {
        let limite = row.Limite_Ate;
        // Validação da Faixa 5 (=>B5 ou texto indica teto)
        if (typeof limite === 'string' && isNaN(parseFloat(limite))) limite = Infinity;
        return {
          limite: limite,
          aliquota: (parseFloat(row.Aliquota) || 0) / 100,
          deducao: parseFloat(row.Parcela_Deduzir) || 0
        };
      });
    }

    // Lendo Outras_Categorias
    const catSheet = workbook.Sheets['Outras_Categorias'];
    if (catSheet) {
      inssData.outrasCategorias = XLSX.utils.sheet_to_json(catSheet).map(row => ({
        nome: row.Categoria,
        aliquota: (parseFloat(row.Aliquota) || 0) / 100,
        base: (row.Base_Calculo || "").trim().toLowerCase()
      }));
    }
  }

  async function loadIRPF(path) {
    const res = await fetch(path);
    const arrayBuffer = await res.arrayBuffer();
    const workbook = XLSX.read(arrayBuffer, { type: 'array' });

    const pSheet = workbook.Sheets['Configuracoes'];
    if (pSheet) {
      const pData = XLSX.utils.sheet_to_json(pSheet);
      pData.forEach(row => {
        if (row.Variavel) irpfData.parametros[row.Variavel.trim()] = row.Valor;
      });
    }

    const tSheet = workbook.Sheets['Tabela_Progressiva'];
    if (tSheet) {
      irpfData.tabelaProgressiva = XLSX.utils.sheet_to_json(tSheet).map(row => {
        let limite = row.Limite_Ate;
        if (typeof limite === 'string' && isNaN(parseFloat(limite))) limite = Infinity;
        return {
          limite: limite,
          aliquota: (parseFloat(row.Aliquota) || 0), // IRPF spreadsheet is already divided or decimal? Need to test, wait, IRPF formula was parsed carefully
          deducao: parseFloat(row.Parcela_Deduzir) || 0
        };
      });
    }
  }

  function atualizarSEO() {
    const ano = inssData.parametros['Ano_Base'] || new Date().getFullYear();
    document.querySelectorAll('.dynamic-ano').forEach(el => el.innerText = ano);
    document.title = `Cálculo Salário Líquido ${ano} - Contabilidade Camilo`;
  }

  function popularCategorias() {
    if (inssData.outrasCategorias.length > 0) {
      inssData.outrasCategorias.forEach(cat => {
        const opt = document.createElement('option');
        opt.value = cat.nome;
        opt.innerText = cat.nome;
        els.categoria.appendChild(opt);
      });
    }
  }

  // Lógica de Cálculo
  function calcularDescontos(bruto, dependentes, pensao, categoriaNome) {
    let inss = 0;
    
    // Calcula INSS
    if (categoriaNome === 'CLT') {
      // Progressivo Simplificado pelas deduções (Igual IRPF)
      for (let faixa of inssData.tabelaProgressiva) {
        if (bruto <= faixa.limite) {
          inss = (bruto * faixa.aliquota) - faixa.deducao;
          break;
        }
      }
      // Se bruto maior que a última faixa (Teto)
      const ultimaFaixa = inssData.tabelaProgressiva[inssData.tabelaProgressiva.length - 1];
      if (bruto > ultimaFaixa.limite || ultimaFaixa.limite === Infinity) {
        inss = (bruto * ultimaFaixa.aliquota) - ultimaFaixa.deducao;
      }
      // Travar no Teto fixo (faixa sem aliquota, com deducao cheia no excel do usuário)
      // O usuário colocou a deducao cheia na ultima faixa
      if(ultimaFaixa.aliquota === 0 && bruto > inssData.tabelaProgressiva[inssData.tabelaProgressiva.length - 2].limite) {
        inss = ultimaFaixa.deducao;
      }
    } else {
      // Outras categorias
      const cat = inssData.outrasCategorias.find(c => c.nome === categoriaNome);
      if (cat) {
        let base = bruto;
        if (cat.base.includes('mínimo') || cat.base.includes('minimo')) {
          base = inssData.parametros['Salario_Minimo'] || 1621;
        }
        // Limitando a base ao Teto do INSS
        const teto = inssData.parametros['Teto_INSS'] || 8475.55;
        if (base > teto) base = teto;
        inss = base * cat.aliquota;
      }
    }

    // Calcula IRRF
    let irrf = 0;
    const valorDependente = irpfData.parametros['Valor_Dependente'] || 189.59;
    const deducaoSimplificada = irpfData.parametros['Desconto_Simplificado'] || 564.80;
    
    const deducoesLegais = inss + pensao + (dependentes * valorDependente);
    let baseIR = bruto - deducoesLegais;
    let baseSimplificada = bruto - deducaoSimplificada;
    
    // Escolher a base mais benéfica
    let baseCalculoFinal = Math.min(baseIR, baseSimplificada);
    if(baseCalculoFinal < 0) baseCalculoFinal = 0;

    for (let faixa of irpfData.tabelaProgressiva) {
      if (baseCalculoFinal <= faixa.limite) {
        irrf = (baseCalculoFinal * faixa.aliquota) - faixa.deducao;
        break;
      }
    }
    
    // Regra adicional para IRPF (Alta Renda PL 1087)
    const tetoAdicional = irpfData.parametros['Limite_Isencao_Adicional'] || 50000;
    const aliqAdicional = irpfData.parametros['Aliquota_Adicional'] || 0.10;
    if (bruto > tetoAdicional) {
      irrf += (bruto - tetoAdicional) * aliqAdicional;
    }

    if (irrf < 0) irrf = 0;

    const liquido = bruto - inss - irrf - pensao;
    return { bruto, inss, irrf, pensao, liquido };
  }

  function calcularEAtualizarTela() {
    const bruto = parseCurrency(els.bruto.value);
    const dependentes = parseInt(els.dependentes.value) || 0;
    const pensao = parseCurrency(els.pensao.value);
    const cat = els.categoria.value;

    const res = calcularDescontos(bruto, dependentes, pensao, cat);

    els.resBruto.innerText = formatCurrency(res.bruto);
    els.resINSS.innerText = formatCurrency(res.inss);
    els.resIRRF.innerText = formatCurrency(res.irrf);
    els.resPensao.innerText = formatCurrency(res.pensao);
    els.resLiquido.innerText = formatCurrency(res.liquido);
    els.displayLiquido.innerText = formatCurrency(res.liquido);
    
    let nome = els.nome.value.trim() || "Simulação";
    els.tituloPainel.innerText = `Salário Líquido de ${nome}:`;
  }

  function adicionarColaborador() {
    const bruto = parseCurrency(els.bruto.value);
    if (bruto <= 0) { alert('Insira um salário bruto válido.'); return; }

    const dependentes = parseInt(els.dependentes.value) || 0;
    const pensao = parseCurrency(els.pensao.value);
    const cat = els.categoria.value;
    const nome = els.nome.value.trim() || `Colaborador ${colaboradores.length + 1}`;

    const res = calcularDescontos(bruto, dependentes, pensao, cat);
    
    colaboradores.push({
      nome,
      categoria: cat,
      ...res
    });

    renderTabela();
    
    // Limpa para o próximo
    els.nome.value = '';
    els.bruto.value = '';
    els.dependentes.value = '';
    els.pensao.value = '';
    calcularEAtualizarTela();
  }

  function renderTabela() {
    els.tbody.innerHTML = '';
    
    let totalBruto = 0, totalINSS = 0, totalIRRF = 0, totalLiquido = 0;

    colaboradores.forEach((c, index) => {
      totalBruto += c.bruto;
      totalINSS += c.inss;
      totalIRRF += c.irrf;
      totalLiquido += c.liquido;

      const tr = document.createElement('tr');
      tr.innerHTML = `
        <td><strong>${c.nome}</strong><br><small style="color:#64748b;">${c.categoria}</small></td>
        <td>${formatCurrency(c.bruto)}</td>
        <td>${formatCurrency(c.inss)}</td>
        <td>${formatCurrency(c.irrf)}</td>
        <td style="color:#2563eb; font-weight:bold;">${formatCurrency(c.liquido)}</td>
        <td class="hide-print" style="text-align: center;">
          <button type="button" onclick="window.removerColaborador(${index})" style="background: none; border: none; color: #ef4444; cursor: pointer; font-size: 1.2rem;">&times;</button>
        </td>
      `;
      els.tbody.appendChild(tr);
    });

    if (colaboradores.length > 0) {
      // Linha de Total
      const trTotal = document.createElement('tr');
      trTotal.style.backgroundColor = '#f8fafc';
      trTotal.style.fontWeight = 'bold';
      trTotal.innerHTML = `
        <td>TOTAIS</td>
        <td>${formatCurrency(totalBruto)}</td>
        <td>${formatCurrency(totalINSS)}</td>
        <td>${formatCurrency(totalIRRF)}</td>
        <td style="color:#2563eb;">${formatCurrency(totalLiquido)}</td>
        <td class="hide-print"></td>
      `;
      els.tbody.appendChild(trTotal);
      els.tabela.style.display = 'block';
    } else {
      els.tabela.style.display = 'none';
    }
  }

  window.removerColaborador = function(index) {
    colaboradores.splice(index, 1);
    renderTabela();
  };

  // Event Listeners Reativos
  [els.nome, els.categoria, els.bruto, els.dependentes, els.pensao].forEach(input => {
    input.addEventListener('input', calcularEAtualizarTela);
    input.addEventListener('keydown', function(e) {
      if (e.key === 'Enter') {
        e.preventDefault();
        let formElements = Array.from(els.form.elements).filter(el => !el.disabled && el.tabIndex !== -1);
        let index = formElements.indexOf(this);
        if (index > -1 && index < formElements.length - 1) {
          formElements[index + 1].focus();
        }
      }
    });
  });

  els.btnAdicionar.addEventListener('click', adicionarColaborador);
  els.form.addEventListener('submit', (e) => { e.preventDefault(); calcularEAtualizarTela(); });
  els.btnLimpar.addEventListener('click', () => {
    els.form.reset();
    colaboradores = [];
    renderTabela();
    calcularEAtualizarTela();
  });

  // Iniciar
  initCalculadora();
});
