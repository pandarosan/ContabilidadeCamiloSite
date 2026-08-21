import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 4.1 Remover item [13. Guia DAS (Documento de Arrecadação do Simples)]
regex_guia = r'<div class="accordion-item">[\s\S]*?<span class="accordion-title">13\. Guia DAS \(Documento de Arrecadação do Simples\)</span>[\s\S]*?</div>\s*</div>'
html = re.sub(regex_guia, '', html)

# 4.2 Retirar a numeração dos títulos
regex_num = r'(<span class="accordion-title">)\d+\.\s+'
html = re.sub(regex_num, r'\1', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Fixed index.html')
