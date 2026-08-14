# Módulo 4: Otimização de Conversão (CRO) e Vendas

## 📌 Finalidade
Este manual documenta as decisões de design, psicologia de usuário e arquitetura de funil (Fase 4) implementadas nas calculadoras do site da Contabilidade Camilo. O objetivo é maximizar a captação de leads, garantindo ao mesmo tempo uma experiência fluida, profissional e confiável.

---

## 🧠 Psicologia e Experiência do Usuário (UX)

### 1. O Botão "Calcular Impostos" (Efeito Psicológico)
Mesmo com o sistema realizando cálculos instantâneos via JavaScript a cada número digitado (auto-calculate on blur/change), **o botão "Calcular Impostos" foi mantido propositalmente na interface**.
- **Justificativa:** O público-alvo (empresários e contadores mais conservadores) sente a necessidade de "finalizar" uma ação e submeter os dados para obter um resultado oficial. Remover o botão causa a sensação de que o sistema "adivinhou" ou não processou adequadamente. 
- **Otimização de Fluxo:** Implementamos um atalho em que pressionar `Enter` avança automaticamente para o próximo campo e, no último campo, dispara o cálculo ou apenas reforça o resultado.

### 2. A Dança do Balão (CTA Dinâmico)
O Call-to-Action (CTA) foi desenhado para ser persistente, mas não obstrutivo.
- **Desktop:** Ele flutua suavemente e possui um botão de fechar (✖). Se fechado, ele se aloja discretamente no final da coluna esquerda.
- **Mobile:** O CTA reconhece o espaço da tela e se posiciona *abaixo* da calculadora. Isso impede que o balão cubra o teclado numérico ou a tabela de inputs, o que arruinaria a experiência de digitação.
- **Na Calculadora IRPF:** O card de CTA na lateral só aparece **após** a realização do cálculo, instigando o usuário com a mensagem sobre "Adicional de Alta Renda", gerando urgência para falar com um especialista.

### 3. "Relatórios Oficiais" em PDF
A funcionalidade de impressão (`window.print()`) foi rigorosamente estilizada usando `@media print` no CSS.
- **Simples Nacional:** Produz um relatório formal de 2 folhas. A primeira com o demonstrativo matemático e a segunda com avisos legais importantes, logo destacada e layout de "Documento Oficial".
- **IRPF:** Otimizado intensamente (redução de paddings, margens e fontes) para caber estritamente em **1 única página**, preservando o rodapé fixo de direitos autorais e contatos. Isso transmite profissionalismo e facilita o compartilhamento no WhatsApp.

---

## ⚙️ Parametrização e Configuração das Calculadoras

A arquitetura das calculadoras foi projetada para que a equipe da Contabilidade Camilo tenha **autonomia total** sem precisar alterar código.

### 1. Atualização de Regras (Upload de Excel)
Através do Decap CMS, em "Configurações do Sistema", é possível fazer o upload de planilhas (`.xlsx`) com as regras tributárias.
- **Simples Nacional (`calculadora_simples`):** Lê a aba `Tabelas_Referencia` para alíquotas dos Anexos e `Configuracoes` para o teto global (ex: 4.8M).
- **IRPF (`calculadora_irpf`):** Lê a aba `Tabelas_Referencia` para as faixas progressivas (limites, alíquotas, deduções) e a aba `Configuracoes` para o teto de isenção, valor por dependente e parâmetros do novo PL de Alta Renda.

### 2. FAQ Dinâmico e SEO (Schema.org)
A seção de Perguntas Frequentes (FAQ) da calculadora de IRPF foi construída em formato "Accordion" (sanfona).
- **Usabilidade:** Permite agrupar muito texto sem poluir a tela.
- **SEO Técnico:** Cada pergunta e resposta está envelopada com marcações JSON-LD do `Schema.org (FAQPage)`. Isso permite que o Google exiba as perguntas diretamente na página de resultados de busca (Rich Snippets), atraindo tráfego orgânico nacional.

---

## 🚦 Diretrizes Futuras (Regra dos 30 Segundos)
Sempre que uma nova ferramenta for adicionada ao site:
1. **Compressão:** Qualquer imagem ou PDF embarcado deve passar pela "regra dos 30 segundos" — se demorar mais que isso num 3G, o usuário abandona. Use WebP para imagens.
2. **Campos Obrigatórios:** Reduza ao máximo. Nas calculadoras, os únicos bloqueios reais são os campos que impossibilitam a matemática.
3. **Tom de Voz:** Os relatórios impressos devem sempre usar o termo "Estimativa" ou "Simulação", protegendo o escritório legalmente de variações tributárias.
