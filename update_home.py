import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove (& Fator R) from the title
html = html.replace('Simples Nacional & Fator R', 'Simples Nacional')

# 2. Make the whole card clickable. The card HTML looks like:
# <div class="solution-card text-center">
#   <h3 class="solution-title"><a href="calculadora-simples-nacional.html">Simples Nacional</a></h3>
#   <p class="solution-desc">Simule alíquotas e descubra se sua empresa pode economizar até 60% em impostos.</p>
# </div>
# We can just wrap the whole inner content in an <a> tag, or we can use CSS/JS, or just make the <a> stretch.
# The easiest standard way is to add an absolutely positioned <a> covering the card.
# The card needs `position: relative;`. 
# Or we can just rewrite the card:
old_card = """<div class="solution-card text-center">
          <h3 class="solution-title"><a href="calculadora-simples-nacional.html">Simples Nacional</a></h3>
          <p class="solution-desc">Simule alíquotas e descubra se sua empresa pode economizar até 60% em impostos.</p>
        </div>"""

new_card = """<div class="solution-card text-center" style="position: relative; cursor: pointer;" onclick="window.location.href='calculadora-simples-nacional.html'">
          <h3 class="solution-title"><a href="calculadora-simples-nacional.html" style="text-decoration: none; color: inherit;">Simples Nacional</a></h3>
          <p class="solution-desc">Simule alíquotas e descubra se sua empresa pode economizar até 60% em impostos.</p>
          <a href="calculadora-simples-nacional.html" style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; z-index: 1;"></a>
        </div>"""

# If the title was already replaced, we need to match the new one
old_card_updated = old_card.replace('Simples Nacional & Fator R', 'Simples Nacional')
html = html.replace(old_card_updated, new_card)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("index.html updated.")
