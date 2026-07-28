import json
import os

input_file = '/home/aluno/.gemini/antigravity-ide/brain/f8bac653-9833-40d2-8ebf-f3e14bb9a699/.system_generated/logs/transcript.jsonl'
output_file = '/home/aluno/.projetos/ContabilidadeCamilo/historico_chat.txt'

try:
    with open(input_file, 'r', encoding='utf-8') as fin, \
         open(output_file, 'w', encoding='utf-8') as fout:
        
        fout.write("HISTÓRICO DA CONVERSA - PROJETO CONTABILIDADE CAMILO\n")
        fout.write("="*60 + "\n\n")
        
        for line in fin:
            if not line.strip():
                continue
            data = json.loads(line)
            
            source = data.get('source', '')
            content = data.get('content', '')
            
            if not content:
                continue
                
            if source == 'USER_EXPLICIT' or source == 'USER':
                # Remover tags internas como <USER_REQUEST>
                if '<USER_REQUEST>' in content:
                    content = content.split('<USER_REQUEST>')[1].split('</USER_REQUEST>')[0].strip()
                fout.write(f"Rosangela:\n{content}\n")
                fout.write("-" * 40 + "\n\n")
            elif source == 'MODEL' and data.get('type') == 'PLANNER_RESPONSE':
                fout.write(f"Antigravity (Especialistas):\n{content}\n")
                fout.write("=" * 60 + "\n\n")

    print(f"Arquivo gerado com sucesso em {output_file}")
except Exception as e:
    print(f"Erro ao gerar o arquivo: {e}")
