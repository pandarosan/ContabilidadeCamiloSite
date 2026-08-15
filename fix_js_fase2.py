import re

with open('calculadora-salario-liquido.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Replace the IRPF block
old_irpf = """    // 3. Cálculo do IRPF
    let irrf = 0;
    const valorDependente = irpfData.parametros['Deducao_Dependente'] || irpfData.parametros['Valor_Dependente'] || 189.59;
    const deducaoSimplificada = irpfData.parametros['Desconto_Simplificado'] || 564.80;
    
    const deducoesLegais = inss + pensao + (dependentes * valorDependente);
    const baseLegal = Math.max(0, bruto - deducoesLegais);
    const baseSimplificada = Math.max(0, bruto - deducaoSimplificada);
    
    // O contribuinte utiliza a base que resultar no menor imposto
    const baseCalculoFinal = Math.min(baseLegal, baseSimplificada);
    
    for (let faixa of irpfData.tabelaProgressiva) {
      if (baseCalculoFinal <= faixa.limite) {
        irrf = (baseCalculoFinal * (faixa.aliquota > 1 ? faixa.aliquota / 100 : faixa.aliquota)) - faixa.deducao;
        break;
      }
    }

    if (irrf < 0) irrf = 0;"""

new_irpf = """    // 3. Cálculo do IRPF (CLT e Autônomos Normais)
    let irrf = 0;
    if (categoriaNome !== 'MEI') {
      const valorDependente = irpfData.parametros['Deducao_Dependente'] || irpfData.parametros['Valor_Dependente'] || 189.59;
      const deducaoSimplificada = irpfData.parametros['Desconto_Simplificado'] || 564.80;
      
      const deducoesLegais = inss + pensao + (dependentes * valorDependente);
      const baseLegal = Math.max(0, bruto - deducoesLegais);
      const baseSimplificada = Math.max(0, bruto - deducaoSimplificada);
      
      // Escolhe a base mais vantajosa
      const baseCalculoFinal = Math.min(baseLegal, baseSimplificada);
      
      for (let faixa of irpfData.tabelaProgressiva) {
        if (baseCalculoFinal <= faixa.limite) {
          const aliq = faixa.aliquota > 1 ? faixa.aliquota / 100 : faixa.aliquota;
          irrf = (baseCalculoFinal * aliq) - faixa.deducao;
          break;
        }
      }

      // Regra adicional para IRPF (Alta Renda PL 1087)
      const tetoAdicional = irpfData.parametros['Limite_Isencao_Adicional'] || 50000;
      const aliqAdicional = irpfData.parametros['Aliquota_Adicional'] || 0.10;
      if (bruto > tetoAdicional) {
        irrf += (bruto - tetoAdicional) * aliqAdicional;
      }
    }

    if (irrf < 0) irrf = 0;"""

js = js.replace(old_irpf, new_irpf)

# 2. Add UX logic for MEI
old_events = """  // Event Listeners Reativos
  [els.nome, els.categoria, els.bruto, els.dependentes, els.pensao].forEach(input => {
    input.addEventListener('input', calcularEAtualizarTela);"""

new_events = """  // Event Listeners Reativos
  els.categoria.addEventListener('change', function(e) {
    const isMEI = this.value === 'MEI';
    const divDep = document.getElementById('divDependentes');
    const divPen = document.getElementById('divPensao');
    if (isMEI) {
      if(divDep) { divDep.style.opacity = '0.5'; els.dependentes.disabled = true; els.dependentes.value = ''; }
      if(divPen) { divPen.style.opacity = '0.5'; els.pensao.disabled = true; els.pensao.value = ''; }
    } else {
      if(divDep) { divDep.style.opacity = '1'; els.dependentes.disabled = false; }
      if(divPen) { divPen.style.opacity = '1'; els.pensao.disabled = false; }
    }
    calcularEAtualizarTela();
  });

  [els.nome, els.categoria, els.bruto, els.dependentes, els.pensao].forEach(input => {
    input.addEventListener('input', calcularEAtualizarTela);"""

js = js.replace(old_events, new_events)

with open('calculadora-salario-liquido.js', 'w', encoding='utf-8') as f:
    f.write(js)
