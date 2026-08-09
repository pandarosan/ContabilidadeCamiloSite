import re

with open('calculadora-simples-nacional.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the specific comment for info importantes with the print header + the original comment
info_comment = "<!-- INFORMAÇÕES IMPORTANTES -->"
print_header_2 = """
      <!-- PRINT HEADER PAGE 2 -->
      <div class="print-header" style="display: none; text-align: center; margin-bottom: 2rem; page-break-before: always;">
        <div style="font-size: 2.5rem; font-weight: bold; color: var(--primary-color); margin-bottom: 1rem;">Contabilidade <span style="color: #d4af37;">Camilo</span></div>
        <h2 style="color: var(--primary-color); margin: 0; font-size: 1.5rem;">Anexo - Informações Importantes</h2>
      </div>
"""

if 'PRINT HEADER PAGE 2' not in html:
    html = html.replace(info_comment, print_header_2 + '\n  ' + info_comment)

# I also need to make sure the section itself doesn't have an extra page-break if the print-header handles it, 
# but the easiest way is to let the print header have `page-break-before: always;`.

with open('calculadora-simples-nacional.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Also fix the style.css where I put `.info-importantes { page-break-before: always; }` because that class doesn't exist.
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()
css = css.replace('.info-importantes { page-break-before: always; margin-top: 0 !important; }', '')
with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("HTML print header updated.")
