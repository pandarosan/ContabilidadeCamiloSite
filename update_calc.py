import re

# 1. Update HTML
with open('calculadora-simples-nacional.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make sure we have a container on the left for the moved toast
seo_end_str = 'A Contabilidade Camilo disponibiliza ao lado uma ferramenta de cálculo do Simples Nacional:</p>\n\n        '
if 'id="seo-cta-container"' not in html:
    html = html.replace(seo_end_str, seo_end_str + '<div id="seo-cta-container"></div>\n        ')

# Add the Print Header 2 before info-importantes
info_str = '<div class="info-importantes'
print_header_2 = """
      <!-- PRINT HEADER PAGE 2 -->
      <div class="print-header" style="display: none; text-align: center; margin-bottom: 2rem;">
        <div style="font-size: 2rem; font-weight: bold; color: var(--primary-color); margin-bottom: 1rem;">Contabilidade <span style="color: #d4af37;">Camilo</span></div>
        <h2 style="color: var(--primary-color); margin: 0; font-size: 1.8rem;">Anexo - Informações Importantes</h2>
      </div>
"""
if 'PRINT HEADER PAGE 2' not in html:
    html = html.replace(info_str, print_header_2 + '\n      ' + info_str)

with open('calculadora-simples-nacional.html', 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Update JS to add Close button and Move logic
with open('calculadora-simples.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the showMessage logic to include a close button
show_msg_func = """function mostrarMensagem(id, exibir) {
  const msg = document.getElementById(id);
  if (msg) {
    if (exibir) {
      msg.style.display = 'block';
      // Mover de volta para a toast-container caso tenha sido movida para a esquerda
      const toastContainer = document.getElementById('alert-zone');
      if (msg.parentElement !== toastContainer) {
        toastContainer.appendChild(msg);
      }
      
      // Adicionar botão de fechar se não existir
      if (!msg.querySelector('.btn-close-toast')) {
        const closeBtn = document.createElement('button');
        closeBtn.innerHTML = '✖';
        closeBtn.className = 'btn-close-toast';
        closeBtn.style.cssText = 'position: absolute; top: 10px; right: 10px; background: none; border: none; font-size: 1.2rem; cursor: pointer; color: #666;';
        closeBtn.onclick = function() {
           // Mover para debaixo do CTA na esquerda
           const leftContainer = document.getElementById('seo-cta-container');
           if (leftContainer) {
              leftContainer.appendChild(msg);
           }
        };
        msg.style.position = 'relative'; // Ensure absolute close btn works
        msg.appendChild(closeBtn);
      }
    } else {
      msg.style.display = 'none';
      // Retornar ao container original ao ocultar
      const toastContainer = document.getElementById('alert-zone');
      if (msg.parentElement !== toastContainer) {
        toastContainer.appendChild(msg);
      }
    }
  }
}"""

# Inject the new showMessage function using regex
js = re.sub(r'function mostrarMensagem\(id, exibir\) \{[\s\S]*?\n\}', show_msg_func, js)

with open('calculadora-simples.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("HTML and JS updated.")
