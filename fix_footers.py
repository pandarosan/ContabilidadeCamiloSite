import re

with open('calculadora-simples-nacional.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Define the full footer content
footer_content = """<p style="font-weight: bold; color: var(--primary-color); font-size: 1.2rem; margin-bottom: 0.5rem;">Simulação realizada no site da Contabilidade Camilo.</p>
          <p style="color: #444; font-size: 1rem; margin-bottom: 1rem;">Precisa de ajuda para reduzir seus impostos com segurança?</p>
          <div style="font-size: 1.1rem; font-weight: bold; color: var(--primary-color);">
            <span style="color: #25D366;">WhatsApp:</span> (11) 94491-3323 | E-mail: contato@contabilidadecamilo.com.br
          </div>
          <div style="font-size: 1.1rem; font-weight: bold; color: var(--primary-color); margin-top: 0.5rem;">
            contabilidadecamilo.com.br
          </div>
          <p style="text-align: center; font-size: 9pt; color: #64748b; margin-top: 1.5rem; line-height: 1.3;">*Os cálculos aqui demonstrados são aproximações baseadas nas tabelas gerais do Simples Nacional.<br>Para valores exatos e obrigações acessórias, consulte um de nossos especialistas.</p>
          <p style="text-align: center; font-size: 9pt; color: #64748b; margin-top: 0.5rem; line-height: 1.3;">&copy; 2026 Contabilidade Camilo. Todos os direitos reservados. | Política de Privacidade | Termos de Uso<br><span style="color: #007bff;">🌐 por PandaRoSan</span></p>"""

# Replace page 1 footer
html = re.sub(
    r'<div id="print-footer" class="print-only-footer".*?</div>',
    f'<div id="print-footer" class="print-only-footer" style="display: none; margin-top: 1rem; padding-top: 1rem; border-top: 2px solid #eee; text-align: center;">\n          {footer_content}\n        </div>',
    html,
    flags=re.DOTALL
)

# Remove the standalone note on page 1 (since it's now inside the footer)
html = re.sub(r'<p class="print-only-footer-note"[^>]*>.*?</p>', '', html)

# Replace page 2 footer
html = re.sub(
    r'<div class="print-only-footer" style="display: none; margin-top: 2rem; padding-top: 1rem; border-top: 2px solid #eee; text-align: center;">.*?</div>',
    f'<div class="print-only-footer" style="display: none; margin-top: 2rem; padding-top: 1rem; border-top: 2px solid #eee; text-align: center;">\n          {footer_content}\n    </div>',
    html,
    flags=re.DOTALL
)

with open('calculadora-simples-nacional.html', 'w', encoding='utf-8') as f:
    f.write(html)
