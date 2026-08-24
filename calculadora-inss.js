document.addEventListener("DOMContentLoaded", async () => {
  let inssData = { parametros: {}, tabelaProgressiva: [], outrasCategorias: [] };
  let colaboradores = [];

  const els = {
    form: document.getElementById('calcForm'),
    nome: document.getElementById('nomeColaborador'),
    categoria: document.getElementById('categoria'),
    bruto: document.getElementById('salarioBruto'),
    btnLimpar: document.getElementById('btnLimpar'),
    btnAdicionar: document.getElementById('btnAdicionar'),
    resBruto: document.getElementById('resSalarioBruto'),
    resINSS: document.getElementById('resINSS'),
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

  if(els.bruto) els.bruto.addEventListener('input', formatInputCurrency);

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
      await loadINSS(inssUrl);

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
      pData.forEach(rawRow => {
        const row = typeof normalizeKeys === 'function' ? normalizeKeys(rawRow) : (() => {
          const newObj = {}; for (let k in rawRow) newObj[k.trim()] = rawRow[k]; return newObj;
        })();
        const paramName = (row.Parametro || row.parametro || "").toString().trim();
        const val = row.Valor !== undefined ? row.Valor : row.valor;
        if (paramName && val !== undefined) inssData.parametros[paramName] = val;
      });
    }

    const nomeAbaOutras = workbook.SheetNames.find(n => n.trim().toLowerCase() === "outras_categorias");
    if (nomeAbaOutras) {
      inssData.outrasCategorias = XLSX.utils.sheet_to_json(workbook.Sheets[nomeAbaOutras]);
    }

    const nomeAbaProg = workbook.SheetNames.find(n => n.trim().toLowerCase() === "tabela_progressiva");
    if (nomeAbaProg) {
      inssData.tabelaProgressiva = XLSX.utils.sheet_to_json(workbook.Sheets[nomeAbaProg]).map(row => {
        let faixaStr = row.Faixa !== undefined ? row.Faixa : row.faixa;
        let deVal = parseFloat(row.De !== undefined ? row.De : row.de) || 0;
        let ateVal = row.Ate !== undefined ? row.Ate : row.ate;
        if (ateVal === undefined || ateVal === null || ateVal.toString().trim().toLowerCase() === 'teto' || isNaN(parseFloat(ateVal))) {
          ateVal = Infinity;
        } else {
          ateVal = parseFloat(ateVal);
        }
        let aliq = parseFloat(row.Aliquota !== undefined ? row.Aliquota : row.aliquota) || 0;

        return {
          Faixa: faixaStr,
          De: deVal,
          Ate: ateVal,
          Aliquota: aliq > 1 ? aliq / 100 : aliq
        };
      });
    }
  }

  function getParam(data, chavesPossiveis, defaultName = '') {
    const keys = Object.keys(data.parametros);
    for (let c of chavesPossiveis) {
      const foundKey = keys.find(k => k.toLowerCase() === c.toLowerCase());
      if (foundKey) return data.parametros[foundKey];
    }
    return undefined;
  }

  function atualizarSEO() {
    document.title = `Calculadora de INSS - Contabilidade Camilo`;
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

  function calcularDescontos(bruto, categoriaNome) {
    let inss = 0;
    const cat = inssData.outrasCategorias.find(c => c.Nome.trim().toLowerCase() === categoriaNome.trim().toLowerCase());
    
    if (!cat) {
      let valorRestante = bruto;
      for (const faixa of inssData.tabelaProgressiva) {
        let baseFaixa = 0;
        if (bruto > faixa.Ate) {
          baseFaixa = faixa.Ate - faixa.De;
        } else {
          baseFaixa = bruto - faixa.De;
        }
        if (baseFaixa > 0) {
          inss += baseFaixa * faixa.Aliquota;
        }
      }
    } else {
      const isProgressivo = (cat.Calculo || "").toString().trim().toLowerCase() === 'progressivo';
      if (isProgressivo) {
        let valorRestante = bruto;
        for (const faixa of inssData.tabelaProgressiva) {
          let baseFaixa = 0;
          if (bruto > faixa.Ate) {
            baseFaixa = faixa.Ate - faixa.De;
          } else {
            baseFaixa = bruto - faixa.De;
          }
          if (baseFaixa > 0) {
            inss += baseFaixa * faixa.Aliquota;
          }
        }
      } else {
        const aliquota = parseFloat(cat.Aliquota) || 0;
        const usaTeto = (cat.Usa_Teto || "").toString().trim().toLowerCase() === 'sim';
        const inssTeto = getParam(inssData, ['Teto_INSS', 'Teto', 'teto_inss'], 'Teto do INSS') || 0;
        
        let baseCalc = bruto;
        if (usaTeto && baseCalc > inssTeto) {
          baseCalc = inssTeto;
        }
        inss = baseCalc * aliquota;
      }
    }
    
    return { bruto, inss };
  }

  function calcularEAtualizarTela() {
    if (!els.bruto) return;
    const bruto = parseCurrency(els.bruto.value);
    const cat = els.categoria ? els.categoria.value : 'CLT';

    const containerImprimir = document.getElementById('containerImprimir');
    if (containerImprimir) {
      if (bruto > 0 || colaboradores.length > 0) {
        containerImprimir.style.display = 'flex';
      } else {
        containerImprimir.style.display = 'none';
      }
    }

    if (bruto <= 0) {
      if (els.resBruto) els.resBruto.innerText = "R$ 0,00";
      if (els.resINSS) els.resINSS.innerText = "R$ 0,00";
      if (els.displayLiquido) els.displayLiquido.innerText = "R$ 0,00";
      if (document.getElementById('resultadoDestaque')) document.getElementById('resultadoDestaque').style.display = 'none';
      if (!document.body.classList.contains('hide-main-on-print') && colaboradores.length > 0) {
         document.body.classList.add('hide-main-on-print');
      }
      return;
    }
    
    if (document.getElementById('resultadoDestaque')) document.getElementById('resultadoDestaque').style.display = 'block';
    document.body.classList.remove('hide-main-on-print');

    const res = calcularDescontos(bruto, cat);
    
    if (els.resBruto) els.resBruto.innerText = formatCurrency(res.bruto);
    if (els.resINSS) els.resINSS.innerText = formatCurrency(res.inss);
    if (els.displayLiquido) els.displayLiquido.innerText = formatCurrency(res.inss);
  }

  function adicionarColaborador() {
    const bruto = parseCurrency(els.bruto.value);
    if (bruto <= 0) { alert('Insira um salário bruto válido.'); return; }
    const cat = els.categoria ? els.categoria.value : 'CLT';
    const nome = (els.nome && els.nome.value.trim()) ? els.nome.value.trim() : `Colaborador ${colaboradores.length + 1}`;
    
    const res = calcularDescontos(bruto, cat);
    colaboradores.push({ nome, categoria: cat, ...res });
    renderTabela();
    
    if (els.nome) els.nome.value = '';
    if (els.bruto) els.bruto.value = '';
    calcularEAtualizarTela();
  }

  function renderTabela() {
    if (!els.tbody || !els.tabela) return;
    els.tbody.innerHTML = '';
    let totalBruto = 0, totalINSS = 0;
    
    colaboradores.forEach((c, index) => {
      totalBruto += c.bruto;
      totalINSS += c.inss;
      
      const tr = document.createElement('tr');
      tr.innerHTML = `
        <td><strong>${c.nome}</strong><br><small style="color:#64748b;">${c.categoria}</small></td>
        <td>${formatCurrency(c.bruto)}</td>
        <td style="color:#ef4444; font-weight:bold;">${formatCurrency(c.inss)}</td>
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
        <td style="color:#ef4444;">${formatCurrency(totalINSS)}</td>
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
    calcularEAtualizarTela();
  };

  window.prepararImpressao = function() {
    if(els.bruto) {
      const bruto = parseCurrency(els.bruto.value);
      if (bruto > 0) {
        adicionarColaborador();
      }
    }
    window.print();
  };

  if(els.categoria) els.categoria.addEventListener('change', calcularEAtualizarTela);

  [els.nome, els.categoria, els.bruto].forEach(input => {
    if (input) input.addEventListener('input', calcularEAtualizarTela);
  });

  if (els.btnAdicionar) els.btnAdicionar.addEventListener('click', adicionarColaborador);
  if (els.form) {
    els.form.addEventListener('submit', (e) => {
      e.preventDefault();
      adicionarColaborador();
    });
  }
  
  if (els.btnLimpar) {
    els.btnLimpar.addEventListener('click', () => {
      els.form.reset();
      colaboradores = [];
      renderTabela();
      calcularEAtualizarTela();
    });
  }

  initCalculadora();
});
