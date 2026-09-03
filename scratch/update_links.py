import glob
import re

for filepath in glob.glob('*.html'):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Replace the specific link
    content = content.replace(
        '<a href="index.html#calculadoras" target="_blank" rel="noopener noreferrer">Diagnóstico Fiscal da Empresa</a>',
        '<a href="index.html#diagnostico-fiscal" target="_blank" rel="noopener noreferrer">Diagnóstico Fiscal da Empresa</a>'
    )
    
    # Bump cache version just in case
    content = re.sub(r'style\.css\?v=\d+', 'style.css?v=25', content)
    content = re.sub(r'main\.js\?v=\d+', 'main.js?v=25', content)
    
    with open(filepath, 'w') as f:
        f.write(content)
