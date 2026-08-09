import re

with open('calculadora-simples-nacional.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Define the ultra-clean, tightly spaced footer content
beautiful_footer = """<div style="text-align: center; line-height: 1.3;">
            <p style="font-weight: bold; color: var(--primary-color); font-size: 1.1rem; margin: 0 0 0.3rem 0;">Simulação realizada no site da Contabilidade Camilo.</p>
            <p style="color: #444; font-size: 1rem; margin: 0 0 0.8rem 0;">Precisa de ajuda para reduzir seus impostos com segurança?</p>
            <div style="font-size: 1rem; font-weight: bold; color: var(--primary-color); margin: 0 0 0.2rem 0;">
              <span style="color: #25D366;">WhatsApp:</span> (11) 94491-3323 <span style="font-weight: normal; margin: 0 0.3rem;">|</span> E-mail: contato@contabilidadecamilo.com.br
            </div>
            <div style="font-size: 1rem; font-weight: bold; color: var(--primary-color); margin: 0 0 1.2rem 0;">
              contabilidadecamilo.com.br
            </div>
            <p style="font-size: 8pt; color: #64748b; margin: 0 0 0.3rem 0;">
              *Os cálculos aqui demonstrados são aproximações baseadas nas tabelas gerais do Simples Nacional.<br>
              Para valores exatos e obrigações acessórias, consulte um de nossos especialistas.
            </p>
            <p style="font-size: 8pt; color: #64748b; margin: 0;">
              &copy; 2026 Contabilidade Camilo. Todos os direitos reservados. | Política de Privacidade | Termos de Uso<br>
              <span style="color: #007bff; display: inline-block; margin-top: 0.3rem;">🌐 por PandaRoSan</span>
            </p>
          </div>"""

# Replace page 1 footer
html = re.sub(
    r'<div id="print-footer" class="print-only-footer"[^>]*>.*?</div>\s*</div>',
    f'<div id="print-footer" class="print-only-footer" style="display: none; margin-top: 1.5rem; padding-top: 1rem; border-top: 2px solid #eee; text-align: center;">\n          {beautiful_footer}\n        </div>\n      </form>\n    \n      </div>',
    html,
    flags=re.DOTALL
)

# Replace page 2 footer
html = re.sub(
    r'<div class="print-only-footer" style="display: none; margin-top: 2rem; padding-top: 1rem; border-top: 2px solid #eee; text-align: center;">.*?</div>',
    f'<div class="print-only-footer" style="display: none; margin-top: 2rem; padding-top: 1rem; border-top: 2px solid #eee; text-align: center;">\n          {beautiful_footer}\n    </div>',
    html,
    flags=re.DOTALL
)

with open('calculadora-simples-nacional.html', 'w', encoding='utf-8') as f:
    f.write(html)
