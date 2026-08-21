import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 4.2 Retirar a numeração dos títulos
# Example: <span class="accordion-title">1. Microempreendedor Individual (MEI)</span>
regex_num = r'(<span class="accordion-title">)\d+\.\s+'
html = re.sub(regex_num, r'\1', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Fixed numbering')
