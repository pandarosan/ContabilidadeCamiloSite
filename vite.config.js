import { defineConfig } from 'vite';
import { resolve, dirname } from 'path';
import { fileURLToPath } from 'url';
import fs from 'fs';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// Pega todos os arquivos .html na raiz do projeto
const htmlFiles = fs.readdirSync(__dirname).filter(file => file.endsWith('.html'));

const input = {};
htmlFiles.forEach(file => {
  const name = file.replace('.html', '');
  input[name] = resolve(__dirname, file);
});

export default defineConfig({
  build: {
    rollupOptions: {
      input
    }
  }
});
