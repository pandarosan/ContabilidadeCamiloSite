import re

# 1. HTML Update
with open('calculadora-simples-nacional.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add a close button to each alert-msg
btn_html = '<button type="button" class="btn-close-toast" style="position: absolute; top: 10px; right: 10px; background: none; border: none; font-size: 1.2rem; cursor: pointer; color: #666;" onclick="moveToast(this.parentElement)">✖</button>\n          <strong>'

html = html.replace('<div id="msg-erro-rbt12" class="alert-msg" style="display: none;', '<div id="msg-erro-rbt12" class="alert-msg" style="position: relative; display: none;')
html = html.replace('<div id="msg-erro-teto" class="alert-msg" style="display: none;', '<div id="msg-erro-teto" class="alert-msg" style="position: relative; display: none;')
html = html.replace('<div id="msg-aviso-sublimite" class="alert-msg" style="display: none;', '<div id="msg-aviso-sublimite" class="alert-msg" style="position: relative; display: none;')

html = html.replace('<strong>Atenção:</strong> A soma', btn_html + 'Atenção:</strong> A soma')
html = html.replace('<strong>Atenção:</strong> O faturamento', btn_html + 'Atenção:</strong> O faturamento')
html = html.replace('<strong>Aviso Importante:</strong>', btn_html + 'Aviso Importante:</strong>')

with open('calculadora-simples-nacional.html', 'w', encoding='utf-8') as f:
    f.write(html)


# 2. JS Update
with open('calculadora-simples.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Add moveToast function globally
move_toast_fn = """
window.moveToast = function(toastEl) {
  const leftContainer = document.getElementById('seo-cta-container');
  if (leftContainer) {
    leftContainer.appendChild(toastEl);
    const closeBtn = toastEl.querySelector('.btn-close-toast');
    if (closeBtn) closeBtn.style.display = 'none'; // hide close btn once moved
    toastEl.style.boxShadow = 'none'; // flatten
    toastEl.style.animation = 'none';
  }
};
"""

if 'window.moveToast' not in js:
    js = move_toast_fn + '\n' + js

# In clearResults, if the toast was moved, move it back to alert-zone and hide it!
clear_results_update = """
      const alertZone = document.getElementById("alert-zone");
      ["msg-erro-rbt12", "msg-erro-teto", "msg-aviso-sublimite"].forEach(id => {
        const el = document.getElementById(id);
        if (el) {
          el.style.display = "none";
          if (alertZone && el.parentElement !== alertZone) {
             alertZone.appendChild(el);
             const closeBtn = el.querySelector('.btn-close-toast');
             if (closeBtn) closeBtn.style.display = 'block';
             el.style.boxShadow = '0 10px 25px rgba(0,0,0,0.2)'; // restore shadow
          }
        }
      });
"""
# Replace the old hide logic in clearResults or just append to clearResults
js = re.sub(r'const ctaResultado = document\.getElementById\("cta-resultado"\);\s*if \(ctaResultado\) ctaResultado\.style\.display = "none";', 
            'const ctaResultado = document.getElementById("cta-resultado");\n      if (ctaResultado) ctaResultado.style.display = "none";\n' + clear_results_update, js)


with open('calculadora-simples.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Toast buttons and JS updated.")
