import re

# Read files
with open('calculadora-irpf.html', 'r', encoding='utf-8') as f:
    irpf_html = f.read()
    
with open('calculadora-salario-liquido.html', 'r', encoding='utf-8') as f:
    liq_html = f.read()

# Extract header
header_match = re.search(r'(<header class="header.*?>.*?</header>)', irpf_html, re.DOTALL)
header_content = header_match.group(1) if header_match else ''

# Extract footer
footer_match = re.search(r'(<footer class="footer">.*?</footer>)', irpf_html, re.DOTALL)
footer_content = footer_match.group(1) if footer_match else ''

# In liq_html, replace header
liq_html = re.sub(r'<header class="header.*?">.*?</header>', header_content, liq_html, flags=re.DOTALL)

# In liq_html, insert footer before closing body
# But we need to keep the print footer.
print_footer = '<footer id="printFooter" class="show-print" style="display:none; background: white;">\n    <div style="text-align: center; border-top: 1px solid #ccc; padding-top: 10px; margin-top: 30px; font-size: 12px; color: #666;">\n        <p style="margin: 0;"><strong>Contabilidade Camilo</strong> - Excelência e Tradição</p>\n        <p style="margin: 0;">WhatsApp: (11) 94491-3323 | E-mail: contato@contabilidadecamilo.com.br</p>\n        <br><br>\n        <p style="margin: 5px 0 0 0;">© por PandaRoSan <span class="dynamic-ano">2026</span> Contabilidade Camilo. Todos os direitos reservados. | Política de Privacidade | Termos de Uso</p>\n    </div>\n  </footer>'

# Replace existing print footer with BOTH footers
liq_html = re.sub(r'<footer id="printFooter".*?</footer>', footer_content + '\n\n  ' + print_footer, liq_html, flags=re.DOTALL)

# Add hide-print to the real footer
liq_html = liq_html.replace('<footer class="footer">', '<footer class="footer hide-print">')
liq_html = liq_html.replace('<header class="header">', '<header class="header hide-print">')

# Modify layout spaces
liq_html = re.sub(r'gap: 1rem;', r'gap: 0.5rem;', liq_html)
liq_html = re.sub(r'padding: 1.5rem;', r'padding: 1rem;', liq_html)
liq_html = re.sub(r'margin-bottom: 1.5rem;', r'margin-bottom: 0.8rem;', liq_html)

# Add btnCalcular and update Limpar
btn_limpar_old = '<button type="button" class="btn-secondary" id="btnLimpar" style="flex: 1; border: 2px solid var(--primary-color);">Limpar Tudo</button>'
btn_limpar_new = '<button type="button" class="btn-secondary" id="btnLimpar" style="flex: 1; border: 2px solid var(--primary-color); color: var(--primary-color); max-width: 150px; padding: 0.8rem;">Limpar</button>\n              <button type="submit" class="btn-primary" id="btnCalcular" style="flex: 2; font-weight: bold; background-color: var(--primary-color); color: white; border: none; padding: 0.8rem;">Calcular</button>'
liq_html = liq_html.replace(btn_limpar_old, btn_limpar_new)

# Move '+ Adicionar mais um colaborador'
btn_adicionar_old = '''<div style="margin-top: 1.5rem; text-align: right;">
                <button type="button" id="btnAdicionar" class="btn-secondary" style="font-size: 0.95rem; border: 2px solid var(--primary-color); color: var(--primary-color); background: transparent; padding: 0.5rem 1rem;">
                  + Adicionar mais um colaborador
                </button>
              </div>'''

# We remove it from the old location
liq_html = liq_html.replace(btn_adicionar_old, '')

# We append it into the grid after divPensao
pensao_group = '''<div class="form-group" id="divPensao">
                  <label class="form-label" for="pensao">Pensão Alimentícia (R$)
                    <div class="tooltip-container"><span class="tooltip-icon">?</span><span class="tooltip-text">Valor descontado judicialmente da folha.</span></div>
                  </label>
                  <input type="text" id="pensao" class="form-control" placeholder="R$ 0,00">
                </div>'''

pensao_new = pensao_group + '''
                <div class="form-group" style="display: flex; align-items: flex-end; justify-content: flex-end;">
                  <button type="button" id="btnAdicionar" class="btn-secondary" style="font-size: 0.85rem; border: 2px dashed var(--primary-color); color: var(--primary-color); background: transparent; padding: 0.8rem 1rem; width: 100%;">
                    + Adicionar Colaborador
                  </button>
                </div>'''
liq_html = liq_html.replace(pensao_group, pensao_new)

with open('calculadora-salario-liquido.html', 'w', encoding='utf-8') as f:
    f.write(liq_html)
