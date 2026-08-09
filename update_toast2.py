import re

# JS Update
with open('calculadora-simples.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Remove the clear_results_update if it was added
js = js.replace("""      const alertZone = document.getElementById("alert-zone");
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
""", "")

# Add resetToasts() globally
reset_toasts_fn = """
window.resetToasts = function() {
  const alertZone = document.getElementById("alert-zone");
  ["msg-erro-rbt12", "msg-erro-teto", "msg-aviso-sublimite"].forEach(id => {
    const el = document.getElementById(id);
    if (el) {
      if (alertZone && el.parentElement !== alertZone) {
         alertZone.appendChild(el);
         const closeBtn = el.querySelector('.btn-close-toast');
         if (closeBtn) closeBtn.style.display = 'block';
         // Restore original styling
         el.style.boxShadow = '0 4px 6px -1px rgba(0, 0, 0, 0.1)';
         el.style.display = 'none'; // reset to hidden when moved back
      }
    }
  });
};
"""

if 'window.resetToasts' not in js:
    js = js.replace('window.moveToast = function', reset_toasts_fn + '\nwindow.moveToast = function')

# Call resetToasts at the beginning of calcularImpostos
if 'window.resetToasts();' not in js:
    js = js.replace('const calcularImpostos = () => {\n    if (aliquotasData.length === 0) {', 'const calcularImpostos = () => {\n    window.resetToasts();\n    if (aliquotasData.length === 0) {')


with open('calculadora-simples.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("JS reset logic updated.")
