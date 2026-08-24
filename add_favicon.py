import os
import glob
import re

html_files = glob.glob('**/*.html', recursive=True)
# Exclude the "out" directory since it is built from the source files
html_files = [f for f in html_files if not f.startswith('out/')]

favicon_tag = '<link rel="icon" type="image/png" href="/Favicon-Contabilidade-Camilo.png">'
og_tag = '<meta property="og:image" content="https://contabilidadecamilo.com.br/Imagem-Compartilhamento-Contabilidade-Camilo.jpg">'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    # Remove existing favicon or og:image tags if they exist to avoid duplicates
    # This regex is simplistic but should work for typical <link rel="icon"...> and <meta property="og:image"...>
    content = re.sub(r'<link[^>]*rel=["\']icon["\'][^>]*>\n?', '', content)
    content = re.sub(r'<meta[^>]*property=["\']og:image["\'][^>]*>\n?', '', content)
    
    # Also update style.css version
    content = re.sub(r'href="/style\.css(\?v=\d+)?"', 'href="/style.css?v=5"', content)
    
    # Find </head> to inject right before it
    head_end_pos = content.find('</head>')
    if head_end_pos != -1:
        # inject the tags
        injection = f"  {favicon_tag}\n  {og_tag}\n"
        content = content[:head_end_pos] + injection + content[head_end_pos:]
        modified = True
        
    if modified:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")

print("Done.")
