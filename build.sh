#!/bin/bash
# 1. Executa o script que lê os arquivos Markdown e gera o artigos.json
node build.js

# 2. Cria a pasta de saída para a Cloudflare
rm -rf out
mkdir out

# 3. Copia os arquivos essenciais para a pasta de saída
# (Ignorando pastas de desenvolvimento, node_modules, etc)
cp *.html out/ 2>/dev/null || true
cp *.css out/ 2>/dev/null || true
cp *.js out/ 2>/dev/null || true
cp artigos.json out/ 2>/dev/null || true

# 4. Copia a pasta admin do CMS e a pasta data (configurações)
cp -r admin out/ 2>/dev/null || true
cp -r data out/ 2>/dev/null || true

# 5. MÁGICA DAS IMAGENS: O Decap CMS salva as imagens na pasta 'public'.
# Mas no nosso HTML (Vanilla), nós chamamos as imagens direto na raiz (ex: src="foto.png").
# Então nós copiamos o CONTEÚDO da pasta public direto para a raiz da pasta de saída!
if [ -d "public" ]; then
  cp -r public/* out/ 2>/dev/null || true
fi

echo "Build Vanilla concluído com sucesso na pasta 'out'!"
