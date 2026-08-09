import re

with open('calculadora-simples-nacional.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Increase logo font-size (2rem -> 2.5rem)
html = html.replace('font-size: 2rem;', 'font-size: 2.5rem;')

# 2. Decrease report title font-size (1.8rem -> 1.5rem)
html = html.replace('font-size: 1.8rem;', 'font-size: 1.5rem;')

# 3. Decrease INFO IMPORTANTES font-size (1.5rem -> 1.3rem)
html = html.replace('font-size: 1.5rem;', 'font-size: 1.3rem;')

with open('calculadora-simples-nacional.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Font sizes updated.")
