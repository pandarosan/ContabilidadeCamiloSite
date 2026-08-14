import re

with open('calculadora-salario-liquido.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Fix IRPF Sheets
js = js.replace("const pSheet = workbook.Sheets['Configuracoes'];", """const nomeAbaParams = workbook.SheetNames.find(n => n.trim().toLowerCase() === "parametros_gerais");
    const pSheet = nomeAbaParams ? workbook.Sheets[nomeAbaParams] : null;""")

js = js.replace("const tSheet = workbook.Sheets['Tabela_Progressiva'];", """const nomeAbaRef = workbook.SheetNames.find(n => n.trim().toLowerCase() === "tabelas_referencia");
    const tSheet = nomeAbaRef ? workbook.Sheets[nomeAbaRef] : null;""")

# Fix INSS Sheets
js = js.replace("const paramsSheet = workbook.Sheets['Parametros_Gerais'];", """const nomeParamsINSS = workbook.SheetNames.find(n => n.trim().toLowerCase() === "parametros_gerais");
    const paramsSheet = nomeParamsINSS ? workbook.Sheets[nomeParamsINSS] : null;""")

js = js.replace("const tabSheet = workbook.Sheets['Tabelas_Referencia'];", """const nomeRefINSS = workbook.SheetNames.find(n => n.trim().toLowerCase() === "tabelas_referencia");
    const tabSheet = nomeRefINSS ? workbook.Sheets[nomeRefINSS] : null;""")

js = js.replace("const catSheet = workbook.Sheets['Outras_Categorias'];", """const nomeCatINSS = workbook.SheetNames.find(n => n.trim().toLowerCase() === "outras_categorias");
    const catSheet = nomeCatINSS ? workbook.Sheets[nomeCatINSS] : null;""")

# Fix the bug with 'Parametro' and 'Valor' for IRPF (in IRPF it uses row.Parametro and row.Valor, but my code was using row.Variavel)
# In my code:
# if (row.Variavel) irpfData.parametros[row.Variavel.trim()] = row.Valor;
# Let's replace it to handle both Variavel/Parametro and Valor/valor
irpf_params_old = "if (row.Variavel) irpfData.parametros[row.Variavel.trim()] = row.Valor;"
irpf_params_new = """const paramName = (row.Variavel || row.Parametro || row.parametro || "").toString().trim();
        if (paramName) irpfData.parametros[paramName] = row.Valor !== undefined ? row.Valor : row.valor;"""
js = js.replace(irpf_params_old, irpf_params_new)

# Fix INSS Parametro
inss_params_old = "if (row.Parametro && row.Valor !== undefined) {"
inss_params_new = """const paramName = (row.Parametro || row.parametro || "").toString().trim();
        const val = row.Valor !== undefined ? row.Valor : row.valor;
        if (paramName && val !== undefined) {"""
js = js.replace(inss_params_old, inss_params_new)
js = js.replace("inssData.parametros[row.Parametro.trim()] = row.Valor;", "inssData.parametros[paramName] = val;")

# Fix IRPF Tabela Progressiva limit and aliquota parsing
# My code was:
# let limite = row.Limite_Ate;
# aliquota: (parseFloat(row.Aliquota) || 0),
# deducao: parseFloat(row.Parcela_Deduzir) || 0
irpf_tab_old = """irpfData.tabelaProgressiva = XLSX.utils.sheet_to_json(tSheet).map(row => {
        let limite = row.Limite_Ate;
        if (typeof limite === 'string' && isNaN(parseFloat(limite))) limite = Infinity;
        return {
          limite: limite,
          aliquota: (parseFloat(row.Aliquota) || 0), // IRPF spreadsheet is already divided or decimal? Need to test, wait, IRPF formula was parsed carefully
          deducao: parseFloat(row.Parcela_Deduzir) || 0
        };
      });"""
irpf_tab_new = """irpfData.tabelaProgressiva = XLSX.utils.sheet_to_json(tSheet).map(row => {
        let limite = row.Limite_Ate || row.Limite || row.limite;
        if (typeof limite === 'string' && isNaN(parseFloat(limite))) limite = Infinity;
        return {
          limite: parseFloat(limite),
          aliquota: parseFloat(row.Aliquota || row.aliquota || 0),
          deducao: parseFloat(row.Parcela_Deduzir || row.Deducao || row.deducao || 0)
        };
      });"""
js = js.replace(irpf_tab_old, irpf_tab_new)

# Fix config fetch
js = js.replace("const inssPath = configJson.calculadora_simples?.planilha_inss || '/calculadora-inss-configuracoes.xlsx';", "const inssPath = configJson.planilha_inss || '/calculadora-inss-configuracoes.xlsx';")
js = js.replace("const irpfPath = configJson.calculadora_simples?.planilha_irpf || '/calculadora-ir-configuracoes.xlsx';", "const irpfPath = configJson.planilha_irpf || '/calculadora-ir-configuracoes.xlsx';")

with open('calculadora-salario-liquido.js', 'w', encoding='utf-8') as f:
    f.write(js)
