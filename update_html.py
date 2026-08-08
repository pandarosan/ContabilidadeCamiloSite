import re

with open('calculadora-simples-nacional.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Compact paddings
content = content.replace('padding: 2rem; background-color: white;', 'padding: 1.5rem; background-color: white;')
content = content.replace('margin: 0 auto 2rem auto;', 'margin: 0 auto 1.5rem auto;')
content = content.replace('padding: 1rem 0.2rem;', 'padding: 0.75rem 0.2rem;')
content = content.replace('padding: 0.75rem 0.2rem;', 'padding: 0.4rem 0.2rem;') # inputs
content = content.replace('padding: 1rem 0.5rem;', 'padding: 0.75rem 0.5rem;')

# 2. Add Print Header
print_header = """
        <!-- PRINT HEADER (Only visible on print) -->
        <div class="print-header" style="display: none; text-align: center; margin-bottom: 2rem;">
          <img src="img/logo-camilo.png" alt="Contabilidade Camilo" style="max-height: 60px; margin-bottom: 1rem;">
          <h2 style="color: var(--primary-color); margin: 0; font-size: 1.8rem;">Relatório de Simulação - Simples Nacional</h2>
          <p style="color: #666; margin-top: 0.5rem;">Cálculo estimado com base nas informações fornecidas.</p>
        </div>

      <form id="simplesForm">
"""
content = content.replace('<form id="simplesForm">', print_header)

# 3. Add Print CTA Footer and Imprimir Button
print_footer = """
        <div id="print-footer" style="display: none; margin-top: 3rem; padding-top: 2rem; border-top: 2px solid #eee; text-align: center;">
          <p style="font-weight: bold; color: var(--primary-color); font-size: 1.2rem; margin-bottom: 0.5rem;">Simulação realizada no site da Contabilidade Camilo.</p>
          <p style="color: #444; font-size: 1rem; margin-bottom: 1rem;">Precisa de ajuda para reduzir seus impostos com segurança?</p>
          <div style="font-size: 1.1rem; font-weight: bold; color: #25D366;">
            WhatsApp: (11) 94491-3323 | E-mail: contato@contabilidadecamilo.com.br
          </div>
        </div>
"""

btn_wrapper_old = """<div class="btn-wrapper" style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
          <button type="button" id="btn-limpar" class="btn-secondary" style="padding: 1rem 2rem; font-size: 1.1rem; width: auto; background-color: transparent; color: var(--primary-color); border: 1px solid var(--primary-color);">Limpar</button>
          <button type="submit" id="btn-calcular" class="btn-primary" style="padding: 1rem 3rem; font-size: 1.1rem; width: auto;">Calcular Impostos</button>
        </div>"""

btn_wrapper_new = """<div class="btn-wrapper" style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; margin-bottom: 1.5rem;">
          <button type="button" id="btn-limpar" class="btn-secondary" style="padding: 0.8rem 1.5rem; font-size: 1rem; width: auto; background-color: transparent; color: var(--primary-color); border: 1px solid var(--primary-color);">Limpar</button>
          <button type="button" id="btn-imprimir" class="btn-secondary" style="padding: 0.8rem 1.5rem; font-size: 1rem; width: auto; background-color: transparent; color: #64748b; border: 1px solid #cbd5e1; display: flex; align-items: center; gap: 0.5rem;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect x="6" y="14" width="12" height="8"></rect></svg>
            Imprimir
          </button>
          <button type="submit" id="btn-calcular" class="btn-primary" style="padding: 0.8rem 2.5rem; font-size: 1.05rem; width: auto;">Calcular Impostos</button>
        </div>""" + print_footer

content = content.replace(btn_wrapper_old, btn_wrapper_new)

# 4. Move Error Messages to "Alert Zone"
# Find the error messages block
msg_pattern = re.compile(r'<div id="msg-erro-rbt12"[\s\S]*?</div>\s*<div id="cta-resultado"', re.MULTILINE)
messages_match = msg_pattern.search(content)

if messages_match:
    messages_html = messages_match.group(0)
    messages_html = messages_html.replace('<div id="cta-resultado"', '') # remove the cta part
    
    # Remove from old position
    content = content.replace(messages_html, '')
    
    # Add classes for animation and clean up inline styles slightly
    messages_html = messages_html.replace('margin-top: 1.5rem;', 'margin-bottom: 1.5rem; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);')
    messages_html = messages_html.replace('id="msg-erro-rbt12"', 'id="msg-erro-rbt12" class="alert-msg"')
    messages_html = messages_html.replace('id="msg-erro-teto"', 'id="msg-erro-teto" class="alert-msg"')
    messages_html = messages_html.replace('id="msg-aviso-sublimite"', 'id="msg-aviso-sublimite" class="alert-msg"')
    
    # Insert after rbt12 div
    rbt12_block = """<input type="text" id="rbt12" class="form-control" placeholder="R$ 0,00" style="width: 100%; box-sizing: border-box;" required>
        </div>"""
    content = content.replace(rbt12_block, rbt12_block + "\n\n        <!-- ZONA DE ALERTA -->\n        <div id=" + '"alert-zone"' + ">\n" + messages_html + "\n        </div>")

with open('calculadora-simples-nacional.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Update completed.")
