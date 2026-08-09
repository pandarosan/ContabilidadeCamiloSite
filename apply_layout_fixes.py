import re

with open('calculadora-simples-nacional.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove X from msg-erro-teto
html = re.sub(
    r'(<div id="msg-erro-teto"[^>]*>)\s*<button type="button" class="btn-close-toast"[^>]*>✖</button>',
    r'\1',
    html
)

# 2. Stronger colors for msg-erro-rbt12 (use same red as teto)
html = html.replace(
    '<div id="msg-erro-rbt12" class="alert-msg" style="position: relative; display: none; background-color: #fff3cd; color: #856404; padding: 1.5rem; border-radius: 8px; margin-bottom: 1.5rem; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); text-align: center; border: 1px solid #ffeeba;">',
    '<div id="msg-erro-rbt12" class="alert-msg" style="position: relative; display: none; background-color: #fff3cd; color: #b7791f; padding: 1.5rem; border-radius: 8px; margin-bottom: 1.5rem; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); text-align: center; border: 1px solid #ffeeba; border-left: 5px solid #d97706;">'
)
# Make the background actually red or dark orange to be "mais fortinho"
html = html.replace('background-color: #fff3cd; color: #b7791f;', 'background-color: #ffedd5; color: #9a3412;')

# 3. Headers of the table: remove <br>
html = html.replace('Faturamento<br>do Mês', 'Faturamento do Mês')
html = html.replace('Alíquota<br>Efetiva', 'Alíquota Efetiva')
html = html.replace('Valor<br>do DAS', 'Valor do DAS')

# 4. Rows of the table: remove <br> and add " - "
html = html.replace('Anexo I<br><span', 'Anexo I - <span')
html = html.replace('Anexo II<br><span', 'Anexo II - <span')
html = html.replace('Anexo III<br><span', 'Anexo III - <span')
html = html.replace('Anexo IV<br><span', 'Anexo IV - <span')
html = html.replace('Anexo V<br><span', 'Anexo V - <span')

# Add nowrap to Atividade column cells
html = html.replace('text-align: center; line-height: 1.2;">Anexo', 'text-align: center; line-height: 1.2; white-space: nowrap;">Anexo')
html = html.replace('text-align: center;">Atividade</th>', 'text-align: center; white-space: nowrap;">Atividade</th>')
html = html.replace('text-align: center;">Faturamento do Mês', 'text-align: center; white-space: nowrap;">Faturamento do Mês')
html = html.replace('text-align: center;">Alíquota Efetiva', 'text-align: center; white-space: nowrap;">Alíquota Efetiva')
html = html.replace('text-align: center;">Valor do DAS', 'text-align: center; white-space: nowrap;">Valor do DAS')

# 5. RBT12 input and label on the same line in print
# Currently it's a div with label and input.
old_rbt = """        <div class="form-group" style="max-width: 400px; margin: 0 auto 1.5rem auto;">
          <label class="form-label" for="rbt12" style="text-align: center; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 1px; color: var(--primary-color);">
            Faturamento Acumulado (Últimos 12 meses)
          </label>
          <input type="text" id="rbt12" class="form-control" placeholder="R$ 0,00" style="width: 100%; box-sizing: border-box;" required>
        </div>"""

new_rbt = """        <div class="form-group rbt-container" style="max-width: 600px; margin: 0 auto 1.5rem auto; display: flex; flex-direction: column; align-items: center; justify-content: center;">
          <label class="form-label" for="rbt12" style="text-align: center; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 1px; color: var(--primary-color); margin-bottom: 0.5rem;">
            Faturamento Acumulado (Últimos 12 meses)
          </label>
          <input type="text" id="rbt12" class="form-control" placeholder="R$ 0,00" style="width: 100%; max-width: 400px; box-sizing: border-box; text-align: center;" required>
        </div>"""
html = html.replace(old_rbt, new_rbt)

# 6. Logo size on page 1 vs title
# Title: <h2 style="color: var(--primary-color); margin: 0; font-size: 1.3rem;">Relatório de Simulação - Simples Nacional</h2>
# Logo page 1: I need to check how it's written. It's usually a header or just text? 
# In calculators, the header is "Contabilidade Camilo Home Soluções..." which is hidden in print! 
# But wait! I added a PRINT HEADER PAGE 2. Did I add a PRINT HEADER PAGE 1? No!
# The logo in page 1 print must be coming from the main header or I need to create one!
# Let's write the file and then check the HTML for page 1 header.

with open('calculadora-simples-nacional.html', 'w', encoding='utf-8') as f:
    f.write(html)
