

window.resetToasts = function() {
  const alertZone = document.getElementById("alert-zone");
  ["msg-erro-rbt12", "msg-erro-teto", "msg-aviso-sublimite"].forEach(id => {
    const el = document.getElementById(id);
    if (el) {
      if (alertZone && el.parentElement !== alertZone) {
         alertZone.appendChild(el);
         const closeBtn = el.querySelector('.btn-close-toast');
         if (closeBtn) closeBtn.style.display = 'block';
         // Restore original styling
         el.style.boxShadow = '0 4px 6px -1px rgba(0, 0, 0, 0.1)';
         el.style.display = 'none'; // reset to hidden when moved back
      }
    }
  });
};

window.moveToast = function(toastEl) {
  const leftContainer = document.getElementById('seo-cta-container');
  if (leftContainer) {
    leftContainer.appendChild(toastEl);
    const closeBtn = toastEl.querySelector('.btn-close-toast');
    if (closeBtn) closeBtn.style.display = 'none'; // hide close btn once moved
    toastEl.style.boxShadow = 'none'; // flatten
    toastEl.style.animation = 'none';
  }
};

// --- CONFIGURAÇÕES DO CLIENTE (AUTONOMIA) ---
// O valor do sublimite e os percentuais de repartição de ICMS/ISS da 5ª Faixa
// Podem ser alterados diretamente aqui caso haja mudanças na legislação.
let CONFIG_SIMPLES = {
  TETO: 4800000,
  SUBLIMITE: 3600000,
  REPARTICAO_ICMS_ISS_FAIXA5: {
    'I': 0.335,   // 33,50%
    'II': 0.320,  // 32,00%
    'III': 0.335, // 33,50%
    'IV': 0.400,  // 40,00%
    'V': 0.235    // 23,50%
  }
};
// ---------------------------------------------

document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("simplesForm");
  const rbt12Input = document.getElementById("rbt12");
  const fatMesInputs = document.querySelectorAll(".fat-mes");
  const btnLimpar = document.getElementById("btn-limpar");
  const btnCalcular = document.getElementById("btn-calcular");
  const btnImprimir = document.getElementById("btn-imprimir");
  const fatMesTotalDisplay = document.getElementById("fat-mes-total");
  const dasTotalDisplay = document.getElementById("das-total");

  // Formatador helper para exibir as configs na tela
  const formatMillions = (val) => "R$ " + (val / 1000000).toLocaleString('pt-BR') + " milhões";
  
  let aliquotasData = [];
  
  const cacheBuster = "?v=" + new Date().getTime();
  
  // Buscar as configurações do CMS para encontrar o arquivo Excel atualizado
  fetch("/data/configuracoes.json" + cacheBuster)
    .then(res => {
      if (!res.ok) throw new Error("Configuração não encontrada, usando arquivo local padrão.");
      return res.json();
    })
    .then(config => {
      const excelUrl = config.planilha_excel || "aliquotas-simples.xlsx";
      return fetch(excelUrl + cacheBuster);
    })
    .catch(err => {
      console.warn(err.message);
      // Fallback para arquivo padrão caso o CMS ainda não tenha gerado o JSON
      return fetch("aliquotas-simples.xlsx" + cacheBuster);
    })
    .then(response => {
      if (!response.ok) throw new Error("Erro na rede ao baixar a planilha.");
      return response.arrayBuffer();
    })
    .then(data => {
      // Lê o workbook do Excel usando a biblioteca SheetJS (XLSX)
      const workbook = XLSX.read(data, { type: 'array' });
      
      // 1. LER ABA DE REFERÊNCIA (Alíquotas e Faixas)
      // Procura a aba ignorando espaços em branco no final/começo
      const nomeAbaRef = workbook.SheetNames.find(n => n.trim().toLowerCase() === "tabelas_referencia");
      
      if (nomeAbaRef) {
        const sheetRef = workbook.Sheets[nomeAbaRef];
        const rawData = XLSX.utils.sheet_to_json(sheetRef, { defval: null });
        
        // Mapeia colunas novas (Anexo, Faixa, Limite, AliqNom, Ded) para o formato esperado
        aliquotasData = [];
        let prevLimite = {};

        // Garante que os dados estejam ordenados por Anexo e por Faixa
        rawData.sort((a, b) => {
          const anexoA = (a.Anexo || a.anexo || '').toString().trim();
          const anexoB = (b.Anexo || b.anexo || '').toString().trim();
          if (anexoA === anexoB) return (a.Faixa || 0) - (b.Faixa || 0);
          return anexoA.localeCompare(anexoB);
        });

        rawData.forEach(row => {
          const anexoRaw = row.Anexo || row.anexo;
          if (!anexoRaw) return;
          const anexo = anexoRaw.toString().trim();
          
          if (prevLimite[anexo] === undefined) {
            prevLimite[anexo] = 0;
          }
          
          let limite = parseFloat(row.Limite !== undefined && row.Limite !== null ? row.Limite : row.rbt12_ate);
          if (isNaN(limite)) limite = 99999999999; // Para a última faixa caso venha vazia

          let aliq = parseFloat(row.AliqNom !== undefined && row.AliqNom !== null ? row.AliqNom : row.aliquota);
          let ded = parseFloat(row.Ded !== undefined && row.Ded !== null ? row.Ded : row.parcela_deduzir);

          let de = row.rbt12_de !== undefined && row.rbt12_de !== null ? parseFloat(row.rbt12_de) : (prevLimite[anexo] + 0.01);
          if (prevLimite[anexo] === 0) de = 0; // Primeira faixa começa em 0

          aliquotasData.push({
            anexo: anexo,
            rbt12_de: de,
            rbt12_ate: limite,
            aliquota: aliq,
            parcela_deduzir: ded
          });

          prevLimite[anexo] = limite;
        });
      }

      // 2. LER ABA DE CONFIGURAÇÕES (Tetos, Sublimites e Repartições)
      const nomeAbaConf = workbook.SheetNames.find(n => n.trim().toLowerCase() === "configuracoes");
      if (nomeAbaConf) {
        const sheetConfig = workbook.Sheets[nomeAbaConf];
        const configData = XLSX.utils.sheet_to_json(sheetConfig, { defval: null });
        
        configData.forEach(row => {
          if (!row.Parametro || row.Valor === undefined || row.Valor === null) return;
          
          const param = String(row.Parametro).trim().toUpperCase();
          const valor = Number(row.Valor);
          
          if (param === "TETO") CONFIG_SIMPLES.TETO = valor;
          if (param === "SUBLIMITE") CONFIG_SIMPLES.SUBLIMITE = valor;
          
          // Os percentuais na planilha estão como números normais (ex: 33.5), então dividimos por 100
          if (param === "REPARTICAO_ANEXO_I") CONFIG_SIMPLES.REPARTICAO_ICMS_ISS_FAIXA5['I'] = valor / 100;
          if (param === "REPARTICAO_ANEXO_II") CONFIG_SIMPLES.REPARTICAO_ICMS_ISS_FAIXA5['II'] = valor / 100;
          if (param === "REPARTICAO_ANEXO_III") CONFIG_SIMPLES.REPARTICAO_ICMS_ISS_FAIXA5['III'] = valor / 100;
          if (param === "REPARTICAO_ANEXO_IV") CONFIG_SIMPLES.REPARTICAO_ICMS_ISS_FAIXA5['IV'] = valor / 100;
          if (param === "REPARTICAO_ANEXO_V") CONFIG_SIMPLES.REPARTICAO_ICMS_ISS_FAIXA5['V'] = valor / 100;
        });

        // Atualiza os textos do HTML de forma dinâmica a partir das novas configs lidas do Excel
        const txtLimite = document.getElementById("txt-limite");
        const txtSublimite = document.getElementById("txt-sublimite");
        if (txtLimite) txtLimite.textContent = formatMillions(CONFIG_SIMPLES.TETO);
        if (txtSublimite) txtSublimite.textContent = formatMillions(CONFIG_SIMPLES.SUBLIMITE);
      }
    })
    .catch(err => {
      console.error("Erro ao processar planilha:", err);
      alert("Falha ao ler o arquivo Excel das alíquotas. O arquivo pode ter sido deletado ou movido. Certifique-se de que o arquivo foi salvo corretamente no painel do CMS.");
      
      // Fallback visual caso o Drive esteja fora do ar (mantém os defaults do JS)
      const txtLimite = document.getElementById("txt-limite");
      const txtSublimite = document.getElementById("txt-sublimite");
      if (txtLimite) txtLimite.textContent = formatMillions(CONFIG_SIMPLES.TETO);
      if (txtSublimite) txtSublimite.textContent = formatMillions(CONFIG_SIMPLES.SUBLIMITE);
    });

  // Funções de formatação de moeda
  const formatCurrency = (value) => {
    return new Intl.NumberFormat("pt-BR", {
      style: "currency",
      currency: "BRL"
    }).format(value);
  };

  const formatNumber = (value) => {
    return value.toLocaleString('pt-BR', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  };

  const parseCurrency = (str) => {
    if (!str) return 0;
    // Remove "R$", pontos de milhar e troca vírgula por ponto
    const num = str.replace(/[^\d,-]/g, "").replace(/\./g, "").replace(",", ".");
    return parseFloat(num) || 0;
  };

  // Aplica máscara de moeda nos inputs
  const applyCurrencyMask = (e) => {
    let value = e.target.value.replace(/\D/g, "");
    if (value === "") return;
    value = (parseInt(value, 10) / 100).toFixed(2);
    e.target.value = formatCurrency(value);
  };

  rbt12Input.addEventListener("input", applyCurrencyMask);
  
  // Aplica máscara de moeda nos inputs de Faturamento do Mês
  fatMesInputs.forEach(input => {
    input.addEventListener('input', (e) => {
      let value = e.target.value.replace(/\D/g, '');
      if (value === '') {
        e.target.value = '';
        return;
      }
      value = (parseInt(value, 10) / 100).toLocaleString('pt-BR', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
      e.target.value = value;
    });
  });

  // Lógica para avançar no Enter e auto-calcular
  const allInputs = [rbt12Input, ...fatMesInputs];
  
  allInputs.forEach((input, index) => {
    input.addEventListener("keydown", (e) => {
      if (e.key === "Enter") {
        e.preventDefault();
        calcularImpostos();
        if (index < allInputs.length - 1) {
          allInputs[index + 1].focus();
        } else {
          input.blur();
        }
      }
    });
    
    input.addEventListener("blur", () => {
      if (input.value.trim() !== "") {
        calcularImpostos();
      }
    });
  });

  btnCalcular.addEventListener("click", (e) => {
    e.preventDefault();
    calcularImpostos();
  });

  btnLimpar.addEventListener("click", () => {
    rbt12Input.value = "";
    fatMesInputs.forEach(input => {
      input.value = "";
      const anexo = input.dataset.anexo;
      document.getElementById(`aliq-${anexo}`).textContent = "0,00%";
      document.getElementById(`aliq-${anexo}`).style.color = "var(--text-muted)";
      document.getElementById(`das-${anexo}`).textContent = "R$ 0,00";
    });
    fatMesTotalDisplay.textContent = "R$ 0,00";
    dasTotalDisplay.textContent = "R$ 0,00";
    
    const erroTeto = document.getElementById("msg-erro-teto");
    if (erroTeto) erroTeto.style.display = "none";
    const avisoSub = document.getElementById("msg-aviso-sublimite");
    if (avisoSub) avisoSub.style.display = "none";
    const erroRbt12 = document.getElementById("msg-erro-rbt12");
    if (erroRbt12) erroRbt12.style.display = "none";
  });

  if (btnImprimir) {
    btnImprimir.addEventListener("click", (e) => {
      e.preventDefault();
      window.print();
    });
  }

  // Realiza o cálculo principal
  const calcularImpostos = () => {
    window.resetToasts();
    if (aliquotasData.length === 0) {
      return; // Silencioso no auto-calculate, aguardando carregamento
    }

    const rbt12 = parseCurrency(rbt12Input.value);
    
    // Função auxiliar para zerar resultados da tabela
    const clearResults = () => {
      fatMesInputs.forEach(input => {
        const anexo = input.dataset.anexo;
        document.getElementById(`aliq-${anexo}`).textContent = "0,00%";
        document.getElementById(`das-${anexo}`).textContent = "0,00";
      });
      fatMesTotalDisplay.textContent = "R$ 0,00";
      dasTotalDisplay.textContent = "R$ 0,00";
      const ctaResultado = document.getElementById("cta-resultado");
      if (ctaResultado) ctaResultado.style.display = "none";


    };

    // BLOQUEIO DO TETO DO SIMPLES NACIONAL
    const erroTeto = document.getElementById("msg-erro-teto");
    if (rbt12 > CONFIG_SIMPLES.TETO) {
      if (erroTeto) erroTeto.style.display = "block";
      
      const erroDiv = document.getElementById("msg-erro-rbt12");
      if (erroDiv) erroDiv.style.display = "none";
      const avisoSub = document.getElementById("msg-aviso-sublimite");
      if (avisoSub) avisoSub.style.display = "none";
      
      clearResults();
      return;
    } else {
      if (erroTeto) erroTeto.style.display = "none";
    }

    // AVISO DO SUBLIMITE (Não bloqueia o cálculo)
    const avisoSub = document.getElementById("msg-aviso-sublimite");
    if (rbt12 > CONFIG_SIMPLES.SUBLIMITE) {
      if (avisoSub) avisoSub.style.display = "block";
    } else {
      if (avisoSub) avisoSub.style.display = "none";
    }

    let somaFaturamentoMes = 0;
    fatMesInputs.forEach(input => {
      somaFaturamentoMes += parseCurrency(input.value);
    });

    if (somaFaturamentoMes > rbt12 && rbt12 > 0) {
      const erroDiv = document.getElementById("msg-erro-rbt12");
      if (erroDiv) {
        erroDiv.style.display = "block";
      }
      clearResults();
      return;
    } else {
      const erroDiv = document.getElementById("msg-erro-rbt12");
      if (erroDiv) erroDiv.style.display = "none";
    }

    let dasTotal = 0;

    fatMesInputs.forEach(input => {
      const anexo = input.dataset.anexo;
      const fatMes = parseCurrency(input.value);

      const aliqDisplay = document.getElementById(`aliq-${anexo}`);
      const dasDisplay = document.getElementById(`das-${anexo}`);

      if (fatMes <= 0) {
        aliqDisplay.textContent = "0,00%";
        aliqDisplay.style.color = "var(--text-muted)";
        dasDisplay.textContent = "R$ 0,00";
        return;
      }

      // Encontra a faixa correspondente no CSV
      const faixaEncontrada = aliquotasData.find(row => 
        row.anexo === anexo && rbt12 >= row.rbt12_de && rbt12 <= row.rbt12_ate
      );

      if (faixaEncontrada) {
        let aliquotaEfetiva = 0;

        // Formula oficial: (RBT12 * Aliquota Nominal - Parcela a Deduzir) / RBT12
        if (rbt12 <= 0) {
          aliquotaEfetiva = faixaEncontrada.aliquota;
        } else {
          aliquotaEfetiva = ((rbt12 * faixaEncontrada.aliquota) - faixaEncontrada.parcela_deduzir) / rbt12;
        }
        
        // Para RBT12 > Sublimite, simuladores de mercado (como a Ozai) exibem a carga tributária total,
        // somando a alíquota federal da 6ª Faixa com o ICMS/ISS simulado pelas regras da 5ª Faixa.
        if (rbt12 > CONFIG_SIMPLES.SUBLIMITE) {
          const percentualReparticao = CONFIG_SIMPLES.REPARTICAO_ICMS_ISS_FAIXA5[anexo] || 0;
          
          // Busca os parâmetros reais da 5ª faixa na base de dados para o Anexo correspondente (usando o sublimite como teto)
          const faixa5 = aliquotasData.find(row => row.anexo === anexo && row.rbt12_ate === CONFIG_SIMPLES.SUBLIMITE);
          
          if (faixa5) {
            let aliquotaEfetivaFaixa5 = ((rbt12 * faixa5.aliquota) - faixa5.parcela_deduzir) / rbt12;
            let aliquotaIcmsIss = aliquotaEfetivaFaixa5 * percentualReparticao;
            aliquotaEfetiva += aliquotaIcmsIss;
          }
        }
        
        if (aliquotaEfetiva < 0) aliquotaEfetiva = 0;

        // Arredonda o valor do DAS da faixa para 2 casas antes de somar, como no sistema PGDAS
        const valorDas = Math.round(fatMes * aliquotaEfetiva * 100) / 100;
        dasTotal += valorDas;

        aliqDisplay.textContent = (aliquotaEfetiva * 100).toFixed(2).replace(".", ",") + "%";
        aliqDisplay.style.color = "var(--text-color)";
        dasDisplay.textContent = formatNumber(valorDas);
      } else {
        aliqDisplay.textContent = "N/A";
        dasDisplay.textContent = "0,00";
      }
    });

    fatMesTotalDisplay.textContent = formatCurrency(somaFaturamentoMes);
    dasTotalDisplay.textContent = formatCurrency(dasTotal);

    const ctaResultado = document.getElementById("cta-resultado");
    if (ctaResultado && dasTotal > 0) {
      ctaResultado.style.display = "block";
    }
  };
});
