import re

html_content = """
<div class="glossary-grid" style="display: grid; gap: 2rem;">
  <!-- Coluna 1 -->
  <div class="glossary-column">
    <h3 style="color: var(--primary-color); margin-bottom: 1.5rem; font-size: 1.2rem; border-bottom: 2px solid var(--secondary-color); padding-bottom: 0.5rem; display: flex; align-items: flex-end; min-height: 3.5rem; width: fit-content;">Perfis Empresariais, Profissionais & Regimes Tributários</h3>
    <div class="accordion">

      <div class="accordion-item">
        <button class="accordion-header">
          <span class="accordion-title">O que é MEI? Regras, Benefícios e Limite de Faturamento</span>
          <span class="accordion-icon">+</span>
        </button>
        <div class="accordion-summary-text">O Microempreendedor Individual (MEI) é o modelo corporativo mais simples e vantajoso para formalizar o seu negócio no Brasil.</div>
        <div class="accordion-content">
          <p>Desenvolvido para pequenos empreendedores, o MEI garante um CNPJ próprio, permissão para emitir notas fiscais e uma das menores cargas tributárias do país.</p>
          <p><strong>Principais Regras e Vantagens do MEI:</strong></p>
          <ul style="margin-left: 1.5rem; margin-bottom: 1rem; list-style-type: disc;">
            <li><strong>Limite de Faturamento:</strong> Até R$ 81.000,00/ano (proporcional aos meses de abertura) ou até R$ 251.000,00/ano para a modalidade MEI Caminhoneiro (transporte de cargas).</li>
            <li><strong>Imposto Único e Fixo:</strong> Tributação mensal simplificada e acessível recolhida por meio de uma única guia, o DAS MEI.</li>
            <li><strong>Contratação de Funcionário:</strong> Permissão legal para registrar 1 empregado, pagando o salário mínimo ou o piso da categoria profissional.</li>
            <li><strong>Direitos Previdenciários (INSS):</strong> Cobertura completa para aposentadoria por idade, auxílio-doença, salário-maternidade e auxílio-reclusão para dependentes.</li>
          </ul>
          <p>⚠️ <strong>Ultrapassou o limite do MEI ou precisa expandir a sua empresa?</strong> Se o seu faturamento exceder os limites permitidos ou a sua operação demandar mais colaboradores, o seu negócio precisa migrar de categoria. Permanecer com o cadastro desatualizado pode gerar multas e complicações com a Receita Federal.</p>
        </div>
      </div>

      <div class="accordion-item">
        <button class="accordion-header">
          <span class="accordion-title">O que é Microempresa (ME)? Limites, Regras e Vantagens</span>
          <span class="accordion-icon">+</span>
        </button>
        <div class="accordion-summary-text">A Microempresa (ME) é a estrutura empresarial ideal para negócios em expansão que superaram os limites do MEI ou exercem atividades que exigem um registro comercial mais amplo.</div>
        <div class="accordion-content">
          <p>É a escolha perfeita para quem busca flexibilidade operacional e segurança jurídica para escalar o faturamento.</p>
          <p><strong>Principais Regras e Características da ME:</strong></p>
          <ul style="margin-left: 1.5rem; margin-bottom: 1rem; list-style-type: disc;">
            <li><strong>Limite de Faturamento:</strong> Permite faturar até R$ 360.000,00 por ano (ou proporcional ao ano de abertura).</li>
            <li><strong>Contratação de Equipe:</strong> Permite contratar até 9 funcionários para setores de Comércio e Serviços, e até 19 funcionários no setor Industrial (valores de referência do IBGE e Sebrae).</li>
            <li><strong>Regimes Tributários Flexíveis:</strong> Opção de enquadramento no Simples Nacional, Lucro Presumido ou Lucro Real, permitindo escolher o modelo com menor impacto fiscal.</li>
            <li><strong>Ampla Variedade de Atividades:</strong> Praticamente todas as atividades econômicas podem ser registradas como ME, permitindo a atuação individual ou em sociedade com sócios.</li>
          </ul>
          <p>🚀 <strong>Seu negócio está pronto para dar o próximo passo?</strong> Abrir uma Microempresa ou realizar a transição correta garante a saúde financeira do seu negócio e evita tributações desnecessárias.</p>
        </div>
      </div>

      <div class="accordion-item">
        <button class="accordion-header">
          <span class="accordion-title">O que é EPP (Empresa de Pequeno Porte)? Limites e Benefícios</span>
          <span class="accordion-icon">+</span>
        </button>
        <div class="accordion-summary-text">A Empresa de Pequeno Porte (EPP) é o formato ideal para negócios consolidados e estruturados que buscam expansão no mercado nacional.</div>
        <div class="accordion-content">
          <p>Esse enquadramento oferece incentivos fiscais estratégicos, maior facilidade de acesso a crédito e vantagens competitivas para empresas de médio porte.</p>
          <p><strong>Principais Regras e Vantagens da EPP:</strong></p>
          <ul style="margin-left: 1.5rem; margin-bottom: 1rem; list-style-type: disc;">
            <li><strong>Limite de Faturamento Anual:</strong> Destinado a empresas com faturamento bruto entre R$ 360.000,01 e R$ 4.800.000,00 por ano.</li>
            <li><strong>Enquadramento Tributário:</strong> Possibilidade de optar pelo Simples Nacional, Lucro Presumido ou Lucro Real, a depender de qual regime reduz mais a carga de impostos.</li>
            <li><strong>Benefícios e Preferências Legais:</strong> Vantagens exclusivas em licitações públicas (compras governamentais) e facilidade de acesso a linhas de crédito bancárias diferenciadas.</li>
            <li><strong>Gestão Contábil Estratégica:</strong> Recomenda-se acompanhamento analítico frequente — com demonstrações como DRE, Balanço Patrimonial e DFC — para garantir conformidade e otimização fiscal.</li>
          </ul>
          <p>📊 <strong>Sua empresa precisa de uma gestão fiscal eficiente para continuar crescendo?</strong> Com um faturamento mais expressivo, a escolha errada do regime tributário pode custar caro.</p>
        </div>
      </div>

      <div class="accordion-item">
        <button class="accordion-header">
          <span class="accordion-title">O que é Empresário Individual (EI)? Entenda os Riscos e Vantagens</span>
          <span class="accordion-icon">+</span>
        </button>
        <div class="accordion-summary-text">O Empresário Individual (EI) é a modalidade em que uma pessoa física exerce atividade empresarial em nome próprio, sem a necessidade de sócios.</div>
        <div class="accordion-content">
          <p>Nessa estrutura, a pessoa física e a empresa formam uma única entidade jurídica, garantindo facilidade de abertura e atuação formal com CNPJ.</p>
          <p><strong>Principais Regras e Funcionamento do EI:</strong></p>
          <ul style="margin-left: 1.5rem; margin-bottom: 1rem; list-style-type: disc;">
            <li><strong>Responsabilidade Ilimitada (Risco Patrimonial):</strong> O principal ponto de atenção do EI é que não há separação entre o patrimônio pessoal e o da empresa. Bens como casa, carro e conta bancária pessoal podem ser penhorados para quitar dívidas do negócio.</li>
            <li><strong>Faturamento Flexível:</strong> Não tem um limite rígido de faturamento próprio como o MEI. O limite depende do regime tributário escolhido (como o Simples Nacional, de até R$ 4,8 milhões/ano).</li>
            <li><strong>Gestão Financeira:</strong> Permite a definição de Pró-Labore (salário do empresário) e a Distribuição de Lucros, que é isenta de Imposto de Renda quando escriturada corretamente e até o limite de altas rendas.</li>
            <li><strong>Contratação e Atividades:</strong> Permite contratar colaboradores conforme a necessidade da operação e abrange uma grande variedade de atividades econômicas.</li>
          </ul>
          <p>⚠️ <strong>Cuidado: Você está protegendo o seu patrimônio pessoal?</strong> Devido ao risco de a pessoa física responder pelas obrigações da empresa, muitas vezes o modelo de EI não é o mais recomendado para quem deseja crescer com segurança. Nesses casos, a transição para formatos como a SLU (Sociedade Limitada Unipessoal) protege seus bens pessoais contra eventuais riscos operacionais ou fiscais.</p>
        </div>
      </div>

      <div class="accordion-item">
        <button class="accordion-header">
          <span class="accordion-title">Profissional Autônomo (CPF): Quando Vale a Pena e Como Evitar Impostos Excessivos</span>
          <span class="accordion-icon">+</span>
        </button>
        <div class="accordion-summary-text">O Profissional Autônomo é aquele que presta serviços de forma independente, utilizando apenas o próprio CPF, sem constituir formalmente uma empresa.</div>
        <div class="accordion-content">
          <p>Trata-se da opção mais simples para quem está começando, mas que exige controle rigoroso para não pagar tributos abusivos.</p>
          <p><strong>Principais Regras e Tributação do Autônomo no CPF:</strong></p>
          <ul style="margin-left: 1.5rem; margin-bottom: 1rem; list-style-type: disc;">
            <li><strong>Tributação Elevada (Carnê-Leão):</strong> Os rendimentos recebidos de pessoas físicas estão sujeitos à tabela progressiva do Imposto de Renda (IRPF), com alíquotas que chegam a 27,5%, além do ISS municipal e do INSS Autônomo (11 ou 20%).</li>
            <li><strong>Ideal para o Nanoempreendedor:</strong> Prestar serviços no CPF vale a pena principalmente para o nanoempreendedor — aquele que possui um volume muito baixo de faturamento eventual ou renda extra —, onde o custo de manter uma estrutura formal supera a economia tributária.</li>
            <li><strong>O "CNPJ Técnico" e a Reforma Tributária:</strong> A partir de 2027, com a entrada em vigor do IBS e da CBS (Reforma Tributária), o uso de um "CNPJ Técnico" ou prestação via CPF exigirá atenção redobrada quanto aos créditos tributários e retenções na fonte, tornando a contabilidade consultiva indispensável.</li>
          </ul>
          <p>⚠️ <strong>Você está rasgando dinheiro ao continuar prestando serviços no CPF?</strong> Em mais de 90% dos casos, quando o faturamento mensal do autônomo ultrapassa R$ 5.000,00, migrar do CPF para uma Pessoa Jurídica (PJ) pode reduzir a carga tributária pela metade.</p>
        </div>
      </div>

      <div class="accordion-item">
        <button class="accordion-header">
          <span class="accordion-title">Profissional Liberal: Como Escolher entre CPF e PJ para Pagar Menos Impostos</span>
          <span class="accordion-icon">+</span>
        </button>
        <div class="accordion-summary-text">O Profissional Liberal é o prestador de serviços com formação técnica ou universitária regulamentada por conselho de classe (CRM, OAB, CREA, CRO, CRC, entre outros).</div>
        <div class="accordion-content">
          <p>Diferente do autônomo genérico, esse profissional possui habilitação legal específica e pode escolher a estrutura ideal para exercer suas atividades.</p>
          <p><strong>Principais Formas de Atuação e Regras Tributárias:</strong></p>
          <ul style="margin-left: 1.5rem; margin-bottom: 1rem; list-style-type: disc;">
            <li><strong>Pessoa Física (CPF):</strong> Atuação direta pagando o Carnê-Leão (alíquotas de até 27,5% de IRPF + INSS + ISS). Indicado apenas para o nanoempreendedor ou recém-formados com faturamento muito baixo e esporádico.</li>
            <li><strong>Pessoa Jurídica (PJ):</strong> Abertura de empresa própria, permitindo enquadramentos como a Sociedade Unipessoal (SLU) ou Sociedade Simples, garantindo separação e proteção do patrimônio pessoal.</li>
            <li><strong>Aproveitamento do Fator R:</strong> No Simples Nacional, os profissionais liberais que mantêm uma folha de pagamento (ou pró-labore) igual ou superior a 28% do faturamento conseguem migrar do Anexo V para o Anexo III, pagando alíquotas iniciais de apenas 6%.</li>
            <li><strong>Impacto da Reforma Tributária (IBS/CBS):</strong> A partir de 2027, a entrada dos novos impostos (IBS e CBS) exigirá um planejamento tributário detalhado. Profissões regulamentadas terão direito a descontos de alíquota de 30% a 60% (como na área da saúde), mas dependerão da correta estruturação do "CNPJ Técnico" para não perder benefícios.</li>
          </ul>
          <p>⚠️ <strong>Você é um profissional qualificado pagando imposto de renda no teto de 27,5%?</strong> Continuar atuando no CPF quando o faturamento ultrapassa R$ 5.000,00/mês é um dos erros financeiros mais caros para profissionais liberais. A migração para uma estrutura PJ bem planejada reduz a carga tributária significativamente e protege seus ganhos.</p>
        </div>
      </div>

      <h3 style="color: var(--primary-color); margin-top: 2rem; margin-bottom: 1.5rem; font-size: 1.2rem; border-bottom: 2px solid var(--secondary-color); padding-bottom: 0.5rem; display: inline-block;">Regimes Tributários e Legislação</h3>

      <div class="accordion-item">
        <button class="accordion-header">
          <span class="accordion-title">O que é Simples Nacional? Como Funciona e Vantagens Tributárias</span>
          <span class="accordion-icon">+</span>
        </button>
        <div class="accordion-summary-text">O Simples Nacional é o regime tributário mais buscado por micro e pequenas empresas no Brasil.</div>
        <div class="accordion-content">
          <p>Criado para desburocratizar a gestão fiscal, ele unifica a arrecadação dos tributos federais, estaduais e municipais em uma única guia de pagamento mensal, a DAS.</p>
          <p><strong>Principais Regras e Funcionamento do Simples Nacional:</strong></p>
          <ul style="margin-left: 1.5rem; margin-bottom: 1rem; list-style-type: disc;">
            <li><strong>Pagamento Unificado (Guia DAS):</strong> Recolhe todos os tributos incidentes sobre a operação da empresa — abrangendo renda, faturamento, consumo e previdência — em um único documento simplificado.</li>
            <li><strong>Limite de Faturamento:</strong> Destinado a empresas que faturam até R$ 4,8 milhões por ano (com sublimite estadual de R$ 3,6 milhões para tributos estaduais e municipais).</li>
            <li><strong>Anexos e Alíquotas Progressivas:</strong> Os impostos são calculados com base em 5 Anexos (divididos por Comércio, Indústria e Serviços) e variam progressivamente conforme o faturamento acumulado dos últimos 12 meses.</li>
            <li><strong>Redução Fiscal pelo Fator R:</strong> Prestadores de serviços enquadrados no Anexo V podem reduzir a alíquota inicial de 15,5% para apenas 6% ao destinar pelo menos 28% da receita bruta para folha de pagamento ou pró-labore.</li>
          </ul>
          <p>⚠️ <strong>Sua empresa está pagando a alíquota correta no Simples Nacional?</strong> Estar no Simples Nacional não garante, sozinho, o menor imposto. O enquadramento na atividade incorreta ou a falta de gestão do Fator R faz com que muitos empresários paguem tributos acima do necessário.</p>
        </div>
      </div>

      <div class="accordion-item">
        <button class="accordion-header">
          <span class="accordion-title">O que é Fator R no Simples Nacional? Como Reduzir Impostos de 15,5% para 6%</span>
          <span class="accordion-icon">+</span>
        </button>
        <div class="accordion-summary-text">O Fator R é um cálculo tributário estratégico do Simples Nacional que permite a empresas prestadoras de serviços migrarem do Anexo V para o Anexo III, reduzindo drasticamente a alíquota inicial de impostos de 15,5% para apenas 6%.</div>
        <div class="accordion-content">
          <p><strong>Como Funciona a Regra do Fator R:</strong></p>
          <ul style="margin-left: 1.5rem; margin-bottom: 1rem; list-style-type: disc;">
            <li><strong>A Regra dos 28%:</strong> Para ter direito à alíquota reduzida no Anexo III, o valor gasto com a folha de pagamento (incluindo salários, encargos e o Pró-Labore dos sócios) deve corresponder a pelo menos 28% do faturamento bruto da empresa nos últimos 12 meses.</li>
            <li><strong>Cálculo Mensal e Dinâmico:</strong> A relação entre folha e faturamento é calculada mensalmente pela contabilidade. Variações na receita podem fazer a empresa alternar entre os anexos se não houver um acompanhamento rigoroso.</li>
            <li><strong>Atividades Beneficiadas:</strong> A regra aplica-se a diversas áreas de serviços regulamentados e intelectuais, como TI, medicina, odontologia, engenharia, arquitetura, consultorias e marketing.</li>
          </ul>
        </div>
      </div>

    </div>
  </div>

  <!-- Coluna 2 -->
  <div class="glossary-column">
    <h3 style="color: var(--primary-color); margin-bottom: 1.5rem; font-size: 1.2rem; border-bottom: 2px solid var(--secondary-color); padding-bottom: 0.5rem; display: flex; align-items: flex-end; min-height: 3.5rem; width: fit-content;">Guias Práticos, Obrigações & Siglas Fiscais</h3>
    <div class="accordion">

      <div class="accordion-item">
        <button class="accordion-header">
          <span class="accordion-title">Abertura e Encerramento de Empresa: Passo a Passo Seguro para o Seu CNPJ</span>
          <span class="accordion-icon">+</span>
        </button>
        <div class="accordion-summary-text">Registrar ou baixar um negócio exige precisão fiscal e jurídica. Seja para tirar o seu projeto do papel ou encerrar uma operação inativa, o acompanhamento profissional garante agilidade no registro e evita que pendências e multas afetem o CPF.</div>
        <div class="accordion-content">
          <p><strong>Como Funciona a Abertura de Empresa:</strong></p>
          <ul style="margin-left: 1.5rem; margin-bottom: 1rem; list-style-type: disc;">
            <li><strong>Viabilidade de Endereço:</strong> Consulta prévia junto à Prefeitura local para verificar a liberação das atividades no local desejado.</li>
            <li><strong>Contrato Social e Registro:</strong> Elaboração do documento constitutivo e registro do negócio na Junta Comercial (JUCESP), Cartório de Pessoas Jurídicas ou OAB.</li>
            <li><strong>CNPJ e Licenciamento:</strong> Emissão do CNPJ na Receita Federal, Inscrição Estadual/Municipal, e obtenção do Alvará de Funcionamento e licenças necessárias (Vigilância Sanitária, Bombeiros, Cetesb, etc.).</li>
          </ul>
          <p><strong>Como Funciona o Encerramento de Empresa:</strong></p>
          <ul style="margin-left: 1.5rem; margin-bottom: 1rem; list-style-type: disc;">
            <li><strong>Distrato Social:</strong> Elaboração do documento oficial de dissolução da sociedade e finalização dos vínculos jurídicos.</li>
            <li><strong>Baixa Integrada nos Órgãos:</strong> Cancelamento do CNPJ e das inscrições no estado e município, além do encerramento das obrigações acessórias.</li>
            <li><strong>Proteção do CPF dos Sócios:</strong> A baixa correta e definitiva impede o acúmulo de multas por declarações omissas de empresas inativas, protegendo o patrimônio pessoal dos proprietários.</li>
          </ul>
          <p>🚀 <strong>Pronto para abrir seu negócio ou precisa regularizar uma empresa inativa?</strong> Não corra o risco de atrasar o início das suas vendas ou de acumular dívidas desnecessárias na Receita Federal por falta de movimentação contábil.</p>
        </div>
      </div>

      <div class="accordion-item">
        <button class="accordion-header">
          <span class="accordion-title">Emissão de Nota Fiscal (NFS-e e NF-e): Dicas para Faturar com Segurança</span>
          <span class="accordion-icon">+</span>
        </button>
        <div class="accordion-summary-text">A emissão de Nota Fiscal é o documento oficial que comprova o faturamento de um negócio e garante a conformidade com a Receita Federal, Estados e Municípios.</div>
        <div class="accordion-content">
          <p>Emitir o documento fiscal correto protege a empresa contra autuações e evita o pagamento de tributos indevidos.</p>
          <p><strong>Principais Tipos de Nota Fiscal e Regras:</strong></p>
          <ul style="margin-left: 1.5rem; margin-bottom: 1rem; list-style-type: disc;">
            <li><strong>NFS-e (Nota Fiscal de Serviços):</strong> Utilizada por prestadores de serviços. É emitida pelo portal da Prefeitura local ou pelo Emissor Nacional de NFS-e. Exige a escolha exata do código de serviço para determinar a alíquota correta.</li>
            <li><strong>NF-e (Nota Fiscal de Mercadorias):</strong> Utilizada no comércio e na indústria para a circulação de produtos. Requer credenciamento prévio na SEFAZ Estadual, uso de Certificado Digital (A1 ou A3) e um sistema emissor adequado para calcular os impostos incidentes.</li>
            <li><strong>A Nota Fiscal na Reforma Tributária:</strong> Com o novo sistema tributário, a emissão da nota fiscal ganha um papel ainda mais crítico ao atuar diretamente como instrumento de confissão de dívida do IBS e da CBS. Além disso, ela se integra ao mecanismo de split payment (retenção e recolhimento automático do imposto no ato do pagamento).</li>
          </ul>
          <p>⚠️ <strong>Cuidado com a Parametrização Incorreta!</strong> Como a nota fiscal passa a ser a confissão direta do débito tributário, emitir documentos com códigos de serviço, NCM, CFOP ou alíquotas erradas pode gerar cobrança automática de impostos indevidos, tributação duplicada e multas imediatas.</p>
        </div>
      </div>

      <div class="accordion-item">
        <button class="accordion-header">
          <span class="accordion-title">Declaração de Imposto de Renda Pessoa Física (DIRPF) para Sócios e Empresários</span>
          <span class="accordion-icon">+</span>
        </button>
        <div class="accordion-summary-text">Empresários e sócios possuem regras específicas na Declaração do Imposto de Renda Pessoa Física (DIRPF).</div>
        <div class="accordion-content">
          <p>A separação adequada dos valores recebidos da empresa é fundamental para garantir a isenção de tributos sobre o seu patrimônio e evitar surpresas com a Receita Federal.</p>
          <p><strong>O que o Empresário deve Declarar no IRPF:</strong></p>
          <ul style="margin-left: 1.5rem; margin-bottom: 1rem; list-style-type: disc;">
            <li><strong>Pró-Labore (Rendimento Tributável):</strong> É a remuneração mensal paga ao sócio pelo seu trabalho na empresa. Incide sobre ele o Imposto de Renda retido na fonte (conforme a tabela do IRPF) e a contribuição do INSS.</li>
            <li><strong>Distribuição de Lucros (Rendimento Isento):</strong> É o repasse do resultado positivo da empresa aos sócios. É totalmente isento de Imposto de Renda, desde que a empresa possua escrituração contábil regular que comprove o lucro apurado.</li>
            <li><strong>Aporte e Empréstimos (Bens e Direitos / Dívidas):</strong> Eventuais empréstimos entre a pessoa física e o CNPJ ou aumentos de capital social devem ser informados detalhadamente para justificar a variação patrimonial.</li>
          </ul>
          <p>⚠️ <strong>Cuidado com o Cruzamento Automatizado de Dados!</strong> A Receita Federal utiliza supercomputadores que cruzam em tempo real as informações declaradas no seu IRPF (CPF) com as declarações enviadas pela empresa (CNPJ), como eFinanceira, DEFIS, ECD e ECF. Divergências entre o lucro informado no CPF e a contabilidade do CNPJ levam a declaração direto para a Malha Fina.</p>
        </div>
      </div>

      <div class="accordion-item">
        <button class="accordion-header">
          <span class="accordion-title">Certidão Negativa de Débitos (CND): O Atestado de Saúde Fiscal da sua Empresa</span>
          <span class="accordion-icon">+</span>
        </button>
        <div class="accordion-summary-text">A Certidão Negativa de Débitos (CND) é o documento oficial que comprova que a sua empresa está 100% em dia com suas obrigações tributárias, fiscais e previdenciárias.</div>
        <div class="accordion-content">
          <p>Funciona como um selo de credibilidade, indispensável para fechar grandes contratos, obter financiamentos bancários e participar de licitações públicas.</p>
          <p><strong>Os Principais Tipos de Certidões Negativas:</strong></p>
          <ul style="margin-left: 1.5rem; margin-bottom: 1rem; list-style-type: disc;">
            <li><strong>CND Federal (Receita Federal e PGFN):</strong> Atesta a ausência de débitos em tributos federais e na Dívida Ativa da União, além de regularidade com a Previdência Social.</li>
            <li><strong>CND Estadual (SEFAZ):</strong> Comprova a regularidade quanto a impostos estaduais (como ICMS).</li>
            <li><strong>CND Municipal (Prefeitura):</strong> Valida a quitação de tributos municipais (como ISS e IPTU comercial).</li>
            <li><strong>CNDT (Justiça do Trabalho):</strong> Atesta que a empresa não possui débitos em processos trabalhistas já julgados.</li>
            <li><strong>CRF do FGTS (Caixa Econômica):</strong> Confirma a regularidade nos recolhimentos do Fundo de Garantia dos colaboradores.</li>
          </ul>
          <p>⚠️ <strong>Não perca oportunidades de vendas por falta de certidão!</strong> Descobrir uma pendência fiscal na hora de assinar um contrato importante ou liberar um empréstimo pode custar caro para o seu negócio. Além disso, irregularidades não identificadas a tempo podem gerar inscrições na Dívida Ativa e bloqueios operacionais.</p>
        </div>
      </div>

      <div class="accordion-item">
        <button class="accordion-header">
          <span class="accordion-title">DASN-SIMEI: Como Fazer a Declaração Anual do MEI Com Assertividade</span>
          <span class="accordion-icon">+</span>
        </button>
        <div class="accordion-summary-text">A DASN-SIMEI (Declaração Anual do Simples Nacional para o Microempreendedor Individual) é a obrigação fiscal anual que consolida todo o faturamento bruto obtido pelo MEI no ano anterior.</div>
        <div class="accordion-content">
          <p>A entrega é obrigatória para manter o CNPJ regularizado e garantir a continuidade dos benefícios previdenciários.</p>
          <p><strong>Principais Regras e Funcionamento da DASN-SIMEI:</strong></p>
          <ul style="margin-left: 1.5rem; margin-bottom: 1rem; list-style-type: disc;">
            <li><strong>Prazo Oficial de Entrega:</strong> Deve ser transmitida até o dia 31 de maio de cada ano, contendo as informações financeiras relativas ao ano anterior.</li>
            <li><strong>Obrigatória Mesmo Sem Faturamento:</strong> Mesmo que o MEI não tenha emitido notas fiscais ou não tenha faturado nenhum valor no período, a declaração deve ser entregue informando R$ 0,00.</li>
            <li><strong>Informações Exigidas:</strong> Discriminação exata da receita bruta total obtida com a venda de mercadorias/produtos e com a prestação de serviços, além de informar se houve contratação de funcionário.</li>
            <li><strong>Penalidades e Riscos:</strong> O atraso gera multa automática, além do risco de bloqueio da emissão de guias DAS, cancelamento do CNPJ e suspensão do acesso a benefícios do INSS (como auxílio-doença e aposentadoria).</li>
          </ul>
          <p>⚠️ <strong>Seu faturamento ultrapassou o limite do MEI durante o ano?</strong> Ao preencher a DASN-SIMEI, caso seja identificado que o seu faturamento ultrapassou o limite permitido (R$ 81 mil/ano ou R$ 251 mil/ano para MEI Caminhoneiro), a sua empresa deverá ser desenquadrada e migrada para a categoria de Microempresa (ME).</p>
        </div>
      </div>

      <div class="accordion-item">
        <button class="accordion-header">
          <span class="accordion-title">eSocial e FGTS Digital: Gestão Trabalhista e Prevenção de Passivos</span>
          <span class="accordion-icon">+</span>
        </button>
        <div class="accordion-summary-text">O eSocial e o FGTS Digital são as plataformas oficiais do Governo Federal para unificar a prestação de informações trabalhistas, previdenciárias e fiscais das empresas.</div>
        <div class="accordion-content">
          <p>A gestão correta desses sistemas é vital para manter a folha de pagamento em dia e proteger a empresa contra autuações e reclamatórias trabalhistas.</p>
          <p><strong>Principais Regras e Eventos Obrigatórios:</strong></p>
          <ul style="margin-left: 1.5rem; margin-bottom: 1rem; list-style-type: disc;">
            <li><strong>Admissões e Desligamentos em Tempo Real:</strong> O registro de novos colaboradores deve ser informado antes do início das atividades, e os desligamentos dentro dos prazos legais do aviso prévio e rescisão.</li>
            <li><strong>Folha de Pagamento e Encargos:</strong> Apuração mensal de salários, férias, 13º salário e envio de eventos periódicos para geração das Guias de Recolhimento do INSS (via DCTFWeb).</li>
            <li><strong>FGTS Digital:</strong> Emissão unificada da guia de FGTS diretamente vinculada ao eSocial, com pagamentos automatizados via Pix para garantir a quitação imediata.</li>
            <li><strong>Eventos de SST (Saúde e Segurança do Trabalho):</strong> Envio obrigatório das condições ambientais de trabalho (laudos LTCAT, PCMSO) e exames ocupacionais (ASO) para evitar multas pesadas do Ministério do Trabalho.</li>
          </ul>
          <p>⚠️ <strong>Falhas no envio das informações geram multas!</strong> O eSocial cruza dados em tempo real. O descumprimento de prazos — seja no envio de um ASO, no registro de um funcionário ou na transmissão da folha — aciona penalidades e expõe a empresa a passivos trabalhistas.</p>
        </div>
      </div>

      <div class="accordion-item">
        <button class="accordion-header">
          <span class="accordion-title">SAT/RAT e PIS/PASEP: Como Reduzir Custos na Folha e Garantir Direitos</span>
          <span class="accordion-icon">+</span>
        </button>
        <div class="accordion-summary-text">A gestão eficiente do Departamento Pessoal vai além do cálculo de salários.</div>
        <div class="accordion-content">
          <p>A correta apuração do SAT/RAT e a transmissão de dados trabalhistas garantem a segurança jurídica da empresa, a proteção contra acidentes de trabalho e o acesso dos colaboradores ao abono salarial do PIS/PASEP.</p>
          <p><strong>Principais Conceitos e Funcionamento:</strong></p>
          <ul style="margin-left: 1.5rem; margin-bottom: 1rem; list-style-type: disc;">
            <li><strong>SAT/RAT (Seguro de Acidente de Trabalho):</strong> É uma alíquota tributária que varia entre 1% e 3% cobrada sobre a folha de pagamento. O percentual é determinado pelo grau de risco da atividade principal da empresa (baixo, médio ou grave).</li>
            <li><strong>Ajuste pelo FAP (Fator Acidentário de Prevenção):</strong> A alíquota do RAT pode ser multiplicada pelo FAP (entre 0,5 e 2,0). Empresas que investem em segurança do trabalho e não registram acidentes pagam metade do imposto; empresas com alto índice de acidentes têm a tributação dobrada.</li>
            <li><strong>Substituição da RAIS pelo eSocial:</strong> As informações que antes eram enviadas na antiga RAIS agora são transmitidas mensalmente via eSocial. O envio correto dos dados da folha é o que garante que os colaboradores recebam o abono salarial do PIS/PASEP sem divergências no governo.</li>
          </ul>
          <p>⚠️ <strong>Sua empresa pode estar pagando mais imposto sobre a folha do que deveria!</strong> O enquadramento incorreto do grau de risco (CNAE) ou o cálculo equivocado do FAP faz com que muitas empresas recolham alíquotas do RAT superiores ao necessário durante anos.</p>
        </div>
      </div>

    </div>
  </div>
</div>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    original = f.read()

pattern = r'<div class="glossary-grid".*?</div>\s*</div>\s*</section>'
replacement = html_content + "\n      </div>\n    </section>"
# The regex above won't easily match nested divs. Let's do string split.

start_str = '<div class="glossary-grid"'
end_str = '</section>'

start_pos = original.find(start_str)
# Find the next </section> after start_pos
end_pos = original.find(end_str, start_pos)

if start_pos != -1 and end_pos != -1:
    new_html = original[:start_pos] + html_content + "\n      " + original[end_pos:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Replaced successfully!")
else:
    print("Could not find boundaries!")
