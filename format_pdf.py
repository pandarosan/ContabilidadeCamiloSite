import re

with open('calculadora-simples-nacional.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the print-header
new_header = """<div class="print-header" style="display: none; text-align: center; margin-bottom: 2.5rem; position: relative;">
          <div style="position: absolute; top: 1.25rem; left: 0; width: 100%; height: 1px; background-color: #ddd; z-index: 1;"></div>
          <div style="font-size: 2.8rem; font-weight: bold; color: var(--primary-color); margin-bottom: 1.5rem; position: relative; z-index: 2; display: inline-block; background: white; padding: 0 1.5rem;">Contabilidade <span style="color: #d4af37;">Camilo</span></div>
          <h2 style="color: var(--primary-color); margin: 0; font-size: 1.6rem;">Relatório de Simulação - Simples Nacional</h2>
          <p style="color: #666; margin-top: 0.5rem; font-size: 1rem;">Cálculo estimado com base nas informações fornecidas.</p>
        </div>"""

html = re.sub(
    r'<div class="print-header" style="display: none; text-align: center; margin-bottom: 2rem;">.*?</div>\s*(?=<form id="simplesForm">)',
    new_header + '\n\n      ',
    html,
    flags=re.DOTALL
)


# 2. Update the print-only-footer
new_footer = """<div class="print-only-footer" style="display: none; margin-top: 2rem; padding-top: 1rem; text-align: center;">
          
          <div style="margin-bottom: 1.5rem;">
            <p style="font-size: 8pt; color: #64748b; margin: 0 0 0.2rem 0; line-height: 1.4;">
              *Os cálculos aqui demonstrados são aproximações baseadas nas tabelas gerais do Simples Nacional.<br>
              Para valores exatos e obrigações acessórias, consulte um de nossos especialistas.
            </p>
          </div>
          
          <hr style="border: none; border-top: 1px solid #ddd; margin: 1.5rem 0;">

          <div style="text-align: center; line-height: 1.4;">
            <p style="font-weight: bold; color: var(--primary-color); font-size: 1.2rem; margin: 0 0 0.4rem 0;">Simulação realizada no site da Contabilidade Camilo.</p>
            <div style="font-size: 1.05rem; font-weight: bold; color: var(--primary-color); margin: 0 0 1.5rem 0;">
              <span style="color: #007bff;">🌐</span> contabilidadecamilo.com.br
            </div>

            <p style="color: #444; font-size: 1.05rem; margin: 0 0 0.8rem 0;">Precisa de ajuda para reduzir seus impostos com segurança?</p>
            <div style="font-size: 1.05rem; font-weight: bold; color: var(--primary-color); margin: 0 0 4rem 0;">
              <span style="color: #25D366;">WhatsApp:</span> (11) 94491-3323 <span style="font-weight: normal; margin: 0 0.3rem;">|</span> E-mail: contato@contabilidadecamilo.com.br
            </div>

            <div style="display: flex; justify-content: space-between; align-items: flex-end; font-size: 7pt; color: #64748b;">
              <div style="color: #007bff; font-weight: 500;"><span style="font-size: 9pt;">🌐</span> por PandaRoSan</div>
              <div>&copy; 2026 Contabilidade Camilo. Todos os direitos reservados. | Política de Privacidade | Termos de Uso</div>
            </div>
          </div>
        </div>"""

html = re.sub(
    r'<div id="print-footer" class="print-only-footer"[^>]*>.*?</div>\s*(?=</form>)',
    new_footer + '\n\n      ',
    html,
    flags=re.DOTALL
)

html = re.sub(
    r'<div class="print-only-footer"[^>]*>.*?</div>\s*(?=</section>)',
    new_footer + '\n    ',
    html,
    flags=re.DOTALL
)

with open('calculadora-simples-nacional.html', 'w', encoding='utf-8') as f:
    f.write(html)
