# Módulo 2: Motor Dinâmico via Planilha Excel (SheetJS)

## 📌 Finalidade
A maior dor dos clientes na área contábil é depender de programadores toda vez que o governo muda uma alíquota ou um teto tributário. 
Para resolver isso, desenvolvemos uma arquitetura que permite ao próprio cliente (leigo em código) atualizar a inteligência do site fazendo upload de uma planilha do Excel via Decap CMS. O front-end lê a planilha em tempo real e se recalcula sozinho.

---

## 🛠️ Roteiro de Utilização (Para o Usuário Humano)
1. **Configuração da Planilha:** O cliente preenche o arquivo modelo (`.xlsx`). O arquivo possui abas específicas (ex: `Tabelas_Referencia` para alíquotas e `Configuracoes` para tetos e regras globais).
2. **Upload:** O cliente entra no painel do Decap CMS, vai em "Configurações do Sistema", apaga a planilha antiga e anexa a nova.
3. **Publicação:** Ao clicar em Publicar, o CMS grava o link do novo arquivo em um arquivo `configuracoes.json`.
4. **Cálculo em Tempo Real:** Quando o visitante entra no site e digita valores, o Javascript baixa a planilha, converte para JSON no navegador e cruza os dados instantaneamente.

---

## ⚙️ A Mágica (Código e Engenharia para a IA)

A solução usa a biblioteca **SheetJS (XLSX)** incluída no cabeçalho HTML:
`<script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js"></script>`

O script abaixo é o coração da leitura e mapeamento de variáveis, blindado contra trocas de nomes de colunas:

### O Código de Leitura (Javascript)
```javascript
// 1. Busca qual é o arquivo Excel mais recente no JSON do CMS
fetch("/data/configuracoes.json")
  .then(res => res.json())
  .then(config => fetch(config.planilha_excel))
  .then(response => response.arrayBuffer())
  .then(data => {
    // 2. Converte o buffer em um "Workbook" do Excel
    const workbook = XLSX.read(data, { type: 'array' });
    
    // 3. Lê a aba "Tabelas_Referencia" e extrai os dados
    if (workbook.SheetNames.includes("Tabelas_Referencia")) {
      const sheetRef = workbook.Sheets["Tabelas_Referencia"];
      const rawData = XLSX.utils.sheet_to_json(sheetRef, { defval: null });
      
      // 4. Mapeamento Inteligente (Bilíngue)
      // Traduz as colunas do cliente (Anexo, Faixa, Limite, AliqNom, Ded) para o motor matemático
      let aliquotasData = [];
      let prevLimite = { 'I': 0, 'II': 0, 'III': 0, 'IV': 0, 'V': 0 };

      // Garante a ordenação matemática obrigatória
      rawData.sort((a, b) => {
        const anexoA = a.Anexo || a.anexo || '';
        const anexoB = b.Anexo || b.anexo || '';
        if (anexoA === anexoB) return (a.Faixa || 0) - (b.Faixa || 0);
        return anexoA.localeCompare(anexoB);
      });

      rawData.forEach(row => {
        const anexo = row.Anexo || row.anexo;
        if (!anexo) return;
        
        let limite = parseFloat(row.Limite !== undefined ? row.Limite : row.rbt12_ate);
        if (isNaN(limite)) limite = 99999999999; // Fallback última faixa

        let aliq = parseFloat(row.AliqNom !== undefined ? row.AliqNom : row.aliquota);
        let ded = parseFloat(row.Ded !== undefined ? row.Ded : row.parcela_deduzir);

        // Constrói o piso da faixa baseando-se no limite da faixa anterior
        let de = row.rbt12_de !== undefined ? parseFloat(row.rbt12_de) : (prevLimite[anexo] + 0.01);
        if (prevLimite[anexo] === 0) de = 0;

        aliquotasData.push({
          anexo: anexo,
          rbt12_de: de,
          rbt12_ate: limite,
          aliquota: aliq,
          parcela_deduzir: ded
        });

        prevLimite[anexo] = limite;
      });
    }
    
    // Agora o aliquotasData está perfeitamente higienizado e pronto para a matemática!
  })
  .catch(err => console.error("Erro ao processar planilha:", err));
```

### Regras de Ouro desta Implementação:
- **Resiliência a Nomenclatura:** Os usuários alteram os nomes das colunas com frequência. O código verifica as colunas *humanas* (`Limite`, `AliqNom`) e as *técnicas* antigas (`rbt12_ate`, `aliquota`), evitando crashes.
- **Tolerância a Omissões:** A base do limite da faixa (`rbt12_de`) não precisa existir na planilha; ela é auto-calculada a partir do teto da faixa anterior.

---

## 🆘 Troubleshooting (Solução de Problemas)

### O Erro "N/A" (Teto vs Faixas)
Se você aumentou o **TETO** máximo da calculadora na aba `Configuracoes` (ex: de 4.800.000 para 5.800.000), o sistema não bloqueará a tela se o cliente faturar 5 milhões. Porém, as alíquotas aparecerão como **N/A**.
**O motivo:** O Javascript cruza os dados e não encontra nenhuma faixa na aba `Tabelas_Referencia` que vá até 5 milhões. 
**A Solução:** Sempre que alterar o Teto Global na aba `Configuracoes`, lembre-se de ir na aba `Tabelas_Referencia` e atualizar o Limite da *última faixa* (Faixa 6) para refletir o novo teto (ou deixar a célula Limite vazia para que ela represente "infinito").
