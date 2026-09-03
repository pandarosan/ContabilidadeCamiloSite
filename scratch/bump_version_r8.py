import glob
import re

for filepath in glob.glob('*.html'):
    with open(filepath, 'r') as f:
        content = f.read()
    
    content = re.sub(r'style\.css\?v=\d+', 'style.css?v=24', content)
    content = re.sub(r'main\.js\?v=\d+', 'main.js?v=24', content)
    
    with open(filepath, 'w') as f:
        f.write(content)
