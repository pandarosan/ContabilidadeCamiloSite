document.addEventListener("DOMContentLoaded", async () => {
  let inssData = { parametros: {}, tabelaProgressiva: [], outrasCategorias: [] };
  let irpfData = { parametros: {}, tabelaProgressiva: [] };
  let colaboradores = [];

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

  // Função de resolução de caminho e quebra de cache
  function resolveExcelPath(path, defaultPath) {
    const cacheBuster = `?v=${new Date().getTime()}`;
    let finalUrl = path || defaultPath;
    if (finalUrl && finalUrl.startsWith("public/")) {
      finalUrl = "/" + finalUrl.substring(7);
    } else if (finalUrl && !finalUrl.startsWith("/")) {
      finalUrl = "/" + finalUrl;
    }
    return finalUrl + cacheBuster;
  }

  async function initCalculadora() {
    try {
      const cacheBuster = `?v=${new Date().getTime()}`;
      const configRes = await fetch('/data/configuracoes.json' + cacheBuster);
      const configJson = configRes.ok ? await configRes.json() : {};

      const inssUrl = resolveExcelPath(configJson.planilha_inss, '/calculadora-inss-configuracoes.xlsx');
      const irpfUrl = resolveExcelPath(configJson.planilha_irpf, '/calculadora-ir-configuracoes.xlsx');

      await Promise.all([
        loadINSS(inssUrl),
        loadIRPF(irpfUrl)
      ]);

      atualizarSEO();
      popularCategorias();
      calcularEAtualizarTela();
    } catch (e) {
      console.error("Erro ao carregar dados:", e);
      if (els.displayLiquido) els.displayLiquido.innerText = "Erro ao carregar tabelas";
    }
  }

  async function loadINSS(path) {
    const res = await fetch(path);
    const arrayBuffer = await res.arrayBuffer();
    const workbook = XLSX.read(arrayBuffer, { type: 'array' });

    const nomeParamsINSS = workbook.SheetNames.find(n => n.trim().toLowerCase() === "parametros_gerais");
    if (nomeParamsINSS) {
      const pData = XLSX.utils.sheet_to_json(workbook.Sheets[nomeParamsINSS]);
      pData.forEach(row => {
        const paramName = (row.Parametro || row.parametro || "").toString().trim();
        const val = row.Valor !== undefined ? row.Valor : row.valor;
        if (paramName && val !== undefined) inssData.parametros[paramName] = val;
      });
    }

    const nomeRefINSS = workbook.SheetNames.find(n => n.trim().toLowerCase() === "tabelas_referencia");
    if (nomeRefINSS) {
      inssData.tabelaProgressiva = XLSX.utils.sheet_to_json(workbook.Sheets[nomeRefINSS]).map(row => {
        let limite = row.Limite_Ate !== undefined ? row.Limite_Ate : (row.Limite || row.limite);
        if (limite === undefined || limite === null || isNaN(parseFloat(limite))) limite = Infinity;
        
        let aliq = parseFloat(row.Aliquota !== undefined ? row.Aliquota : row.aliquota) || 0;
        let ded = parseFloat(row.Parcela_Deduzir !== undefined ? row.Parcela_Deduzir : (row.Deducao || row.deducao)) || 0;
        
        return {
          limite: limite === Infinity ? Infinity : parseFloat(limite),
          aliquota: aliq > 1 ? aliq / 100 : aliq,
          deducao: ded
        };
      });
    }

    const nomeCatINSS = workbook.SheetNames.find(n => n.trim().toLowerCase() === "outras_categorias");
    if (nomeCatINSS) {
      inssData.outrasCategorias = XLSX.utils.sheet_to_json(workbook.Sheets[nomeCatINSS]).map(row => {
        const catNome = row.Categoria || row.categoria || row.Nome || row.nome || "Outro";
        const catAliq = parseFloat(row.Aliquota || row.aliquota || 0);
        const catBase = (row.Base_Calculo || row.base_calculo || "").toString().trim().toLowerCase();
        return {
          nome: catNome,
          aliquota: catAliq > 1 ? catAliq / 100 : catAliq,
          base: catBase
        };
      });
    }
  }

  async function loadIRPF(path) {
    const res = await fetch(path);
    const arrayBuffer = await res.arrayBuffer();
    const workbook = XLSX.read(arrayBuffer, { type: 'array' });

    const nomeAbaParams = workbook.SheetNames.find(n => n.trim().toLowerCase() === "parametros_gerais");
    if (nomeAbaParams) {
      const pData = XLSX.utils.sheet_to_json(workbook.Sheets[nomeAbaParams]);
      pData.forEach(row => {
        const paramName = (row.Parametro || row.parametro || row.Variavel || "").toString().trim();
        if (paramName) irpfData.parametros[paramName] = row.Valor !== undefined ? row.Valor : row.valor;
      });
    }

    const nomeAbaRef = workbook.SheetNames.find(n => n.trim().toLowerCase() === "tabelas_referencia");
    if (nomeAbaRef) {
      irpfData.tabelaProgressiva = XLSX.utils.sheet_to_json(workbook.Sheets[nomeAbaRef]).map(row => {
        let limite = row.Limite_Ate !== undefined ? row.Limite_Ate : (row.Limite !== undefined ? row.Limite : row.limite);
        if (limite === undefined || limite === null || isNaN(parseFloat(limite))) limite = Infinity;
        
        let aliq = parseFloat(row.Aliquota !== undefined ? row.Aliquota : row.aliquota) || 0;
        let ded = parseFloat(row.Parcela_Deduzir !== undefined ? row.Parcela_Deduzir : (row.Deducao || row.deducao)) || 0;
        
        return {
          limite: limite === Infinity ? Infinity : parseFloat(limite),
          aliquota: aliq > 1 ? aliq / 100 : aliq,
          deducao: ded
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
      els.categoria.innerHTML = '<option value="CLT">CLT (Carteira Assinada)</option>';
      inssData.outrasCategorias.forEach(cat => {
        if (cat.nome && cat.nome !== "undefined") {
          const opt = document.createElement('option');
          opt.value = cat.nome;
          opt.innerText = cat.nome;
          els.categoria.appendChild(opt);
        }
      });
    }
  }

  function calcularDescontos(bruto, dependentes, pensao, categoriaNome) {
    let inss = 0;
    
    if (categoriaNome === 'CLT') {
      const penultimaFaixa = inssData.tabelaProgressiva[inssData.tabelaProgressiva.length - 2];
      const ultimaFaixa = inssData.tabelaProgressiva[inssData.tabelaProgressiva.length - 1];
      const tetoValor = inssData.parametros['Teto_INSS'] || (penultimaFaixa ? penultimaFaixa.limite : 8475.55);
      
      if (bruto >= tetoValor) {
        inss = ultimaFaixa && ultimaFaixa.deducao > 0 ? ultimaFaixa.deducao : 988.09;
      } else {
        for (let faixa of inssData.tabelaProgressiva) {
          if (bruto <= faixa.limite) {
            inss = (bruto * faixa.aliquota) - faixa.deducao;
            break;
          }
        }
      }
    } else {
      const cat = inssData.outrasCategorias.find(c => c.nome === categoriaNome);
      if (cat) {
        let base = bruto;
        if (cat.base.includes('mínimo') || cat.base.includes('minimo')) {
          base = inssData.parametros['Salario_Minimo'] || 1621.00;
        }
        const teto = inssData.parametros['Teto_INSS'] || 8475.55;
        if (base > teto) base = teto;
        inss = base * cat.aliquota;
      }
    }
    
    if (inss < 0) inss = 0;
    
    let irrf = 0;
    if (categoriaNome !== 'MEI') {
      const valorDependente = irpfData.parametros['Deducao_Dependente'] || irpfData.parametros['Valor_Dependente'] || 189.59;
      const deducaoSimplificada = irpfData.parametros['Desconto_Simplificado'] || 564.80;
      
      const deducoesLegais = inss + pensao + (dependentes * valorDependente);
      const baseLegal = Math.max(0, bruto - deducoesLegais);
      const baseSimplificada = Math.max(0, bruto - deducaoSimplificada);
      
      const baseCalculoFinal = Math.min(baseLegal, baseSimplificada);
      
      for (let faixa of irpfData.tabelaProgressiva) {
        if (baseCalculoFinal <= faixa.limite) {
          irrf = (baseCalculoFinal * faixa.aliquota) - faixa.deducao;
          break;
        }
      }

      const tetoAdicional = irpfData.parametros['Adicional_Limite'] || irpfData.parametros['Limite_Isencao_Adicional'] || 50000;
      const aliqAdicional = (irpfData.parametros['Adicional_Aliquota'] || irpfData.parametros['Aliquota_Adicional'] || 10) / 100;
      if (bruto > tetoAdicional) {
        irrf += (bruto - tetoAdicional) * aliqAdicional;
      }
    }

    if (irrf < 0) irrf = 0;
    const liquido = Math.max(0, bruto - inss - irrf - pensao);
    
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
    
    const cta = document.getElementById('cta-resultado');
    if (cta && bruto > 0) cta.style.display = 'block';
  }

  function adicionarColaborador() {
    const bruto = parseCurrency(els.bruto.value);
    if (bruto <= 0) { alert('Insira um salário bruto válido.'); return; }
    const dependentes = parseInt(els.dependentes.value) || 0;
    const pensao = parseCurrency(els.pensao.value);
    const cat = els.categoria.value;
    const nome = els.nome.value.trim() || `Colaborador ${colaboradores.length + 1}`;
    
    const res = calcularDescontos(bruto, dependentes, pensao, cat);
    colaboradores.push({ nome, categoria: cat, ...res });
    renderTabela();
    
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

  els.categoria.addEventListener('change', function() {
    const isMEI = this.value === 'MEI';
    const divDep = document.getElementById('divDependentes');
    const divPen = document.getElementById('divPensao');
    if (isMEI) {
      if (divDep) { divDep.style.opacity = '0.5'; els.dependentes.disabled = true; els.dependentes.value = ''; }
      if (divPen) { divPen.style.opacity = '0.5'; els.pensao.disabled = true; els.pensao.value = ''; }
    } else {
      if (divDep) { divDep.style.opacity = '1'; els.dependentes.disabled = false; }
      if (divPen) { divPen.style.opacity = '1'; els.pensao.disabled = false; }
    }
    calcularEAtualizarTela();
  });

  [els.nome, els.categoria, els.bruto, els.dependentes, els.pensao].forEach(input => {
    input.addEventListener('input', calcularEAtualizarTela);
  });

  els.btnAdicionar.addEventListener('click', adicionarColaborador);
  els.form.addEventListener('submit', (e) => { e.preventDefault(); calcularEAtualizarTela(); });
  els.btnLimpar.addEventListener('click', () => {
    els.form.reset();
    colaboradores = [];
    renderTabela();
    calcularEAtualizarTela();
  });

  initCalculadora();
});
