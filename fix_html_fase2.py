import re

with open('calculadora-irpf.html', 'r', encoding='utf-8') as f:
    irpf_html = f.read()

# Extract the print-only-footer
footer_match = re.search(r'(<div id="print-footer".*?</div>\s*</div>\s*</div>)', irpf_html, re.DOTALL)
if not footer_match:
    # let's try a different regex, maybe the structure is slightly different
    footer_match = re.search(r'(<div id="print-footer".*?)(<script|</body|</footer>)', irpf_html, re.DOTALL)

irpf_footer = footer_match.group(1).strip() if footer_match else ''

# Clean up any trailing tags that might have been caught if we used the second regex
irpf_footer = re.sub(r'</main>.*', '', irpf_footer, flags=re.DOTALL)
irpf_footer = re.sub(r'<footer.*', '', irpf_footer, flags=re.DOTALL)

if irpf_footer:
    with open('calculadora-salario-liquido.html', 'r', encoding='utf-8') as f:
        liq_html = f.read()

    # Find the printFooter in liq_html and replace it
    liq_html = re.sub(r'<footer id="printFooter".*?</footer>', irpf_footer, liq_html, flags=re.DOTALL)

    with open('calculadora-salario-liquido.html', 'w', encoding='utf-8') as f:
        f.write(liq_html)
    print("Replaced successfully!")
else:
    print("Could not find print-footer in irpf.html")
