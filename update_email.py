import os

for root, _, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Substituir o email genérico pelo correto
            content = content.replace('contato@contabilidadecamilo.com.br', 'financeiro@contabilidadecamilo.com.br')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

print("Email atualizado em todos os arquivos HTML.")
