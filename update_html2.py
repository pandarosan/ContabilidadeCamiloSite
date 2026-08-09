import re

with open('calculadora-simples-nacional.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Text Breaking
content = content.replace(
    'Fique atento às principais características do<br>Simples Nacional:',
    'Fique atento às principais<br>características do Simples Nacional:'
)

# 2. Re-position CTA
cta_full_pattern = re.compile(r'<div id="cta-resultado"[\s\S]*?</a>\s*</div>')
cta_full_match = cta_full_pattern.search(content)
if cta_full_match:
    cta_html = cta_full_match.group(0)
    # Remove from old position
    content = content.replace(cta_html, '')
    
    # Add to new position (under the seo-content text)
    # The SEO content ends with:
    # <p style="margin-top: 1.5rem; font-size: 1.1rem; font-weight: 500;">A Contabilidade Camilo disponibiliza ao lado uma ferramenta de cálculo do Simples Nacional:</p>
    # </div>
    seo_end_str = 'A Contabilidade Camilo disponibiliza ao lado uma ferramenta de cálculo do Simples Nacional:</p>\n      </div>'
    content = content.replace(seo_end_str, 'A Contabilidade Camilo disponibiliza ao lado uma ferramenta de cálculo do Simples Nacional:</p>\n\n        ' + cta_html + '\n      </div>')

# 3. Toast Notifications HTML
# We already have <div id="alert-zone"> inside the calc-container.
# It's better to add the CSS classes and let CSS handle the fixed positioning.
content = content.replace('id="alert-zone"', 'id="alert-zone" class="toast-container"')

with open('calculadora-simples-nacional.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("HTML updated.")
