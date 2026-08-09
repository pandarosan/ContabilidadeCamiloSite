import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update .alert-msg and add .toast-container
# Previous .alert-msg CSS is:
"""
.alert-msg {
    animation: slideDownFade 0.4s ease-out forwards;
}
"""

toast_css = """
.toast-container {
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 9999;
    display: flex;
    flex-direction: column;
    gap: 10px;
    max-width: 400px;
    pointer-events: none; /* allows clicking through when empty */
}

.toast-container > div {
    pointer-events: auto; /* make alerts clickable */
    margin-bottom: 0 !important; /* override the inline margin */
}

.alert-msg {
    animation: slideUpFade 0.4s ease-out forwards;
    box-shadow: 0 10px 25px rgba(0,0,0,0.2) !important;
}

@keyframes slideUpFade {
    0% {
        opacity: 0;
        transform: translateY(20px);
    }
    100% {
        opacity: 1;
        transform: translateY(0);
    }
}
"""

# Replace the old alert-msg and slideDownFade with the new toast styles
css = re.sub(r'\.alert-msg\s*\{[^}]*\}', '', css)
css = re.sub(r'@keyframes slideDownFade\s*\{[^}]*100%\s*\{[^}]*\}[^}]*\}', '', css)

# Add the new toast css before the @media print
css = css.replace('/* ========================================================= */\n/* IMPRESSÃO', toast_css + '\n/* ========================================================= */\n/* IMPRESSÃO')

# 2. Update @media print with page-break and font-size
print_fixes = """
    body, html { margin: 0 !important; padding: 0 !important; }
    body, main, .calc-table, .form-control, p, span, div { font-size: 11pt !important; line-height: 1.3 !important; }
    .calc-container-wrapper { page-break-inside: avoid; }
    .calc-table { page-break-inside: avoid; }
"""
# Insert inside @media print {
css = css.replace('@media print {\n', '@media print {\n' + print_fixes)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS updated.")
