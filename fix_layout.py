import re

def get_block(html, start_tag, end_tag):
    pattern = re.compile(f'({start_tag}.*?{end_tag})', re.DOTALL)
    match = pattern.search(html)
    if match:
        return match.group(1)
    return None

with open('calculadora-simples-nacional.html', 'r', encoding='utf-8') as f:
    simples_html = f.read()

with open('calculadora-irpf.html', 'r', encoding='utf-8') as f:
    irpf_html = f.read()

# Blocks to replace
header_block = get_block(simples_html, r'<header class="header">', r'</header>')
footer_block = get_block(simples_html, r'<footer class="footer">', r'</footer>')
footer_bottom_block = get_block(simples_html, r'<div class="footer-bottom"', r'</div>')

# Fab buttons
fab_block_start = simples_html.find('<!-- Botões Flutuantes -->')
fab_block_end = simples_html.find('</body>')
fab_block = simples_html[fab_block_start:fab_block_end]

# Replace in IRPF
irpf_html = re.sub(r'<header class="header">.*?</header>', header_block, irpf_html, flags=re.DOTALL)
irpf_html = re.sub(r'<footer class="footer">.*?</footer>', footer_block, irpf_html, flags=re.DOTALL)

# Footer bottom wasn't even in IRPF properly? Wait, let's check
if '<div class="footer-bottom"' in irpf_html:
    irpf_html = re.sub(r'<div class="footer-bottom".*?</div>', footer_bottom_block, irpf_html, flags=re.DOTALL)
else:
    # insert before footer
    irpf_html = irpf_html.replace('<footer class="footer">', footer_bottom_block + '\n  <footer class="footer">')

# Fabs
if '<!-- Botões Flutuantes -->' not in irpf_html:
    irpf_html = irpf_html.replace('</body>', fab_block + '</body>')

with open('calculadora-irpf.html', 'w', encoding='utf-8') as f:
    f.write(irpf_html)

print("HTML layout fixed.")
