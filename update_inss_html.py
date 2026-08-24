import re

with open('calculadora-inss.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Title and description
content = content.replace('<title>Cálculo Salário Líquido - Contabilidade Camilo</title>', '<title>Calculadora de INSS - Contabilidade Camilo</title>')
content = content.replace('content="Calculadora de Salário Líquido CLT e Autônomos. Descubra os descontos reais de INSS e IRPF na folha de pagamento."', 'content="Calculadora de INSS para CLT, Autônomos e Pró-labore. Descubra sua alíquota e o valor exato da contribuição mensal."')

# 2. Update H1
content = content.replace('<h1>Cálculo de Salário Líquido</h1>', '<h1>Calculadora de INSS</h1>')
content = content.replace('Simule os descontos de INSS e Imposto de Renda', 'Simule a contribuição previdenciária e descubra o valor do INSS')

# 3. Remove Dependentes and Pensão from form
dep_pattern = r'<div class="form-group" id="divDependentes">.*?</div>\s*</div>'
content = re.sub(dep_pattern, '</div>', content, flags=re.DOTALL)

# Need to match the pensao group carefully
pensao_pattern = r'<div class="form-group">\s*<label for="pensao">.*?</div>\s*</div>'
# Wait, let's just use string replace for the inputs since regex can be tricky with HTML.
