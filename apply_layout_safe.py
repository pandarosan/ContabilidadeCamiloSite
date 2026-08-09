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
    '<div id="msg-erro-rbt12" class="alert-msg" style="position: relative; display: none; background-color: #ffedd5; color: #9a3412; padding: 1.5rem; border-radius: 8px; margin-bottom: 1.5rem; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); text-align: center; border: 1px solid #ffeeba; border-left: 5px solid #d97706;">'
)

# 3. Headers of the table: hide <br> in print, show space
html = html.replace('Faturamento<br>do Mês', 'Faturamento<br class="hide-print"><span class="show-print"> </span>do Mês')
html = html.replace('Alíquota<br>Efetiva', 'Alíquota<br class="hide-print"><span class="show-print"> </span>Efetiva')
html = html.replace('Valor<br>do DAS', 'Valor<br class="hide-print"><span class="show-print"> </span>do DAS')

# 4. Rows of the table: hide <br> in print, show " - "
html = html.replace('Anexo I<br><span', 'Anexo I<br class="hide-print"><span class="show-print"> - </span><span')
html = html.replace('Anexo II<br><span', 'Anexo II<br class="hide-print"><span class="show-print"> - </span><span')
html = html.replace('Anexo III<br><span', 'Anexo III<br class="hide-print"><span class="show-print"> - </span><span')
html = html.replace('Anexo IV<br><span', 'Anexo IV<br class="hide-print"><span class="show-print"> - </span><span')
html = html.replace('Anexo V<br><span', 'Anexo V<br class="hide-print"><span class="show-print"> - </span><span')

# Add class for the rbt12 container
html = html.replace('<div class="form-group" style="max-width: 400px; margin: 0 auto 1.5rem auto;">', '<div class="form-group rbt12-group" style="max-width: 400px; margin: 0 auto 1.5rem auto;">')

# Ensure the footer has the site name
if 'contabilidadecamilo.com.br' not in html.split('<div id="print-footer"')[1].split('</div>')[0]:
    html = html.replace(
        'WhatsApp: (11) 94491-3323 | E-mail: contato@contabilidadecamilo.com.br\n          </div>',
        'WhatsApp: (11) 94491-3323 | E-mail: contato@contabilidadecamilo.com.br\n          </div>\n          <div style="font-size: 1rem; font-weight: 500; color: #666;">\n            contabilidadecamilo.com.br\n          </div>'
    )

# Duplicate footer to page 2 (info-importantes section end)
if 'Precisa de ajuda para reduzir seus impostos' not in html.split('<!-- INFORMAÇÕES IMPORTANTES -->')[1]:
    footer_copy = """
    <div class="print-only-footer" style="display: none; margin-top: 2rem; padding-top: 1rem; border-top: 2px solid #eee; text-align: center;">
      <p style="font-weight: bold; color: var(--primary-color); font-size: 1.2rem; margin-bottom: 0.5rem;">Precisa de ajuda para reduzir seus impostos com segurança?</p>
      <div style="font-size: 1.1rem; font-weight: bold; color: #25D366; margin-bottom: 0.5rem;">
        WhatsApp: (11) 94491-3323 | E-mail: contato@contabilidadecamilo.com.br
      </div>
      <div style="font-size: 1rem; font-weight: 500; color: #666;">
        contabilidadecamilo.com.br
      </div>
    </div>
  </section>"""
    html = html.replace('  </section>', footer_copy)

# Fix the duplicate title on page 2 header
html = html.replace(
    '<div class="print-header" style="display: none; text-align: center; margin-bottom: 2rem; page-break-before: always;">\n        <div style="font-size: 2.5rem; font-weight: bold; color: var(--primary-color); margin-bottom: 1rem;">Contabilidade <span style="color: #d4af37;">Camilo</span></div>\n        <h2 style="color: var(--primary-color); margin: 0; font-size: 1.5rem;">Anexo - Informações Importantes</h2>',
    '<div class="print-header" style="display: none; text-align: center; margin-bottom: 2rem; page-break-before: always;">\n        <div style="font-size: 2.5rem; font-weight: bold; color: var(--primary-color); margin-bottom: 1rem;">Contabilidade <span style="color: #d4af37;">Camilo</span></div>'
)

with open('calculadora-simples-nacional.html', 'w', encoding='utf-8') as f:
    f.write(html)
