document.addEventListener("DOMContentLoaded", async () => {
  let inssData = { parametros: {}, tabelaProgressiva: [], outrasCategorias: [] };
  let irpfData = { parametros: {}, tabelaProgressiva: [] };
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

    const nomeRefINSS = workbook.SheetNames.find(n => n.trim().toLowerCase() === "tabelas_referencia");
    if (nomeRefINSS) {
      const normalizeKeys = (obj) => {
        const newObj = {};
        for (let key in obj) {
          newObj[key.trim()] = obj[key];
        }
        return newObj;
      };

      inssData.tabelaProgressiva = XLSX.utils.sheet_to_json(workbook.Sheets[nomeRefINSS]).map(rawRow => {
        const row = normalizeKeys(rawRow);
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
      inssData.outrasCategorias = XLSX.utils.sheet_to_json(workbook.Sheets[nomeCatINSS]).map(rawRow => {
        const normalizeKeys = (obj) => {
          const newObj = {}; for (let k in obj) newObj[k.trim()] = obj[k]; return newObj;
        };
        const row = normalizeKeys(rawRow);
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

  function atualizarSEO() {
    const ano = inssData.parametros['Ano_Base'] || new Date().getFullYear();
    document.querySelectorAll('.dynamic-ano').forEach(el => el.innerText = ano);
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
    const getParam = (data, keys, label) => {
      for (let k of keys) {
        if (data.parametros[k] !== undefined) return parseFloat(data.parametros[k]);
      }
      throw new Error(`Falta parâmetro: ${label}`);
    };

    const calcularINSS = (valorBruto) => {
      let v_inss = 0;
      if (categoriaNome === 'CLT') {
        const tetoValor = getParam(inssData, ['Teto_INSS'], 'Teto INSS');
        
        if (valorBruto >= tetoValor && inssData.tabelaProgressiva.length > 0) {
          const ultimaFaixa = inssData.tabelaProgressiva[inssData.tabelaProgressiva.length - 1];
          if (ultimaFaixa && ultimaFaixa.deducao > 0) {
            v_inss = ultimaFaixa.deducao;
          } else {
            let baseAnterior = 0;
            let inssBrutoTemp = 0;
            for (const faixa of inssData.tabelaProgressiva) {
              if (tetoValor > baseAnterior) {
                let valorNaFaixa = Math.min(tetoValor, faixa.limite) - baseAnterior;
                inssBrutoTemp += valorNaFaixa * faixa.aliquota;
                baseAnterior = faixa.limite;
              } else {
                break;
              }
            }
            v_inss = Math.floor((inssBrutoTemp + 0.000001) * 100) / 100;
          }
        } else {
          let baseAnterior = 0;
          let inssBrutoTemp = 0;
          for (const faixa of inssData.tabelaProgressiva) {
            if (valorBruto > baseAnterior) {
              let valorNaFaixa = Math.min(valorBruto, faixa.limite) - baseAnterior;
              inssBrutoTemp += valorNaFaixa * faixa.aliquota;
              baseAnterior = faixa.limite;
            } else {
              break;
            }
          }
          v_inss = Math.floor((inssBrutoTemp + 0.000001) * 100) / 100;
        }
      } else {
        const cat = inssData.outrasCategorias.find(c => c.nome === categoriaNome);
        if (cat) {
          let base = valorBruto;
          if (cat.base.includes('mínimo') || cat.base.includes('minimo')) {
            base = getParam(inssData, ['Salario_Minimo'], 'Salário Mínimo');
          }
          const teto = getParam(inssData, ['Teto_INSS'], 'Teto INSS');
          if (base > teto) base = teto;
          v_inss = base * cat.aliquota;
        }
      }
      return Math.max(0, v_inss);
    };

    let inss = calcularINSS(bruto);
    return { bruto, inss };
  }

  function calcularEAtualizarTela() {
    const bruto = parseCurrency(els.bruto.value);
    
    // Gerenciar exibição do botão imprimir
    const containerImprimir = document.getElementById('containerImprimir');
    if (containerImprimir) {
      if (bruto > 0 || colaboradores.length > 0) {
        containerImprimir.style.display = 'flex';
      } else {
        containerImprimir.style.display = 'none';
      }
    }
    
    // Lógica de exibição para a Impressão e Card
    const tabelaContainer = document.getElementById('tabelaColaboradores');
    if (colaboradores.length > 1) {
      document.body.classList.add('hide-main-on-print'); // Oculta o card
      if (tabelaContainer) tabelaContainer.classList.remove('hide-print'); // Garante que a tabela imprima
    } else {
      document.body.classList.remove('hide-main-on-print'); // Mostra o card
      if (tabelaContainer && colaboradores.length <= 1) {
        tabelaContainer.classList.add('hide-print'); // Se só tem 1 (ou 0), a tabela não imprime
      }
    }

    if (bruto <= 0) {
      if (colaboradores.length === 1) {
        // Se há exatamente 1 colaborador na lista e o input está vazio, populamos o card com ele
        const c = colaboradores[0];
        if (els.resBruto) els.resBruto.innerText = formatCurrency(c.bruto);
        if (els.resINSS) els.resINSS.innerText = formatCurrency(c.inss);
        if (els.displayLiquido) els.displayLiquido.innerText = formatCurrency(c.inss);
        if (els.tituloPainel) els.tituloPainel.innerText = `Desconto do INSS de ${c.nome}:`;
        if (document.getElementById('resultadoDestaque')) document.getElementById('resultadoDestaque').style.display = 'block';
      } else {
        // 0 colaboradores e input vazio: Zera o card
        if (els.resBruto) els.resBruto.innerText = 'R$ 0,00';
        if (els.resINSS) els.resINSS.innerText = 'R$ 0,00';
        if (els.displayLiquido) els.displayLiquido.innerText = 'R$ 0,00';
        if (els.tituloPainel) els.tituloPainel.innerText = `Desconto do INSS:`;
        if (document.getElementById('resultadoDestaque')) document.getElementById('resultadoDestaque').style.display = 'none';
      }
      return;
    }
    
    if (document.getElementById('resultadoDestaque')) document.getElementById('resultadoDestaque').style.display = 'block';

    const cat = els.categoria ? els.categoria.value : 'CLT';
    const res = calcularDescontos(bruto, cat);
    
    if (els.resBruto) els.resBruto.innerText = formatCurrency(res.bruto);
    if (els.resINSS) els.resINSS.innerText = formatCurrency(res.inss);
    if (els.displayLiquido) els.displayLiquido.innerText = formatCurrency(res.inss);
    
    let nome = (els.nome && els.nome.value.trim()) ? els.nome.value.trim() : "Simulação";
    if (els.tituloPainel) els.tituloPainel.innerText = `Desconto do INSS de ${nome}:`;
    
    const cta = document.getElementById('cta-resultado');
    if (cta && bruto > 0) cta.style.display = 'block';
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
    const bruto = parseCurrency(els.bruto.value);
    // Se há dados preenchidos na tela E já existe uma lista, 
    // a impressão vai ignorar a tela e imprimir a lista.
    // Portanto, jogamos a simulação atual para dentro da lista antes de imprimir.
    if (bruto > 0 && colaboradores.length > 0) {
      adicionarColaborador();
    }
    window.print();
  };

  if (els.categoria) els.categoria.addEventListener('change', calcularEAtualizarTela);

  [els.nome, els.categoria, els.bruto].forEach(input => {
    if (input) input.addEventListener('input', calcularEAtualizarTela);
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
