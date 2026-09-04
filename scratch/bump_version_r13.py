import glob
import re

for filepath in glob.glob('*.html'):
    with open(filepath, 'r') as f:
        content = f.read()
    
    content = re.sub(r'style\.css\?v=\d+', 'style.css?v=30', content)
    
    with open(filepath, 'w') as f:
        f.write(content)
