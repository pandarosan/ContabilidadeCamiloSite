import os

for file in os.listdir('.'):
    if file.endswith('.html'):
        with open(file, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # We want to replace "por PandaRoSan" with "por PandaRoSan.com.br"
        # But we might have already done it in some files, so let's make sure we don't do "PandaRoSan.com.br.com.br"
        
        html = html.replace('por PandaRoSan.com.br', 'por PandaRoSan')
        html = html.replace('por PandaRoSan', 'por PandaRoSan.com.br')
        
        # We also have "PandaRoSan</a>" which needs to be replaced.
        html = html.replace('PandaRoSan.com.br</a>', 'PandaRoSan</a>')
        html = html.replace('PandaRoSan</a>', 'PandaRoSan.com.br</a>')
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(html)

print('Footers fixed')
