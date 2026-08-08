# RPA Challenge — Selenium + MongoDB

Automação do **RPA Challenge** desenvolvida em Python com foco em exploração de tecnologias, boas práticas de engenharia de software e construção de uma automação resiliente.

Este projeto também representa uma mudança de abordagem em relação a automações anteriores: em vez de utilizar sempre a mesma ferramenta para resolver os mesmos problemas, a proposta é explorar diferentes tecnologias e estratégias, entendendo seus pontos fortes, limitações e cenários de aplicação.

---

## 🎯 Objetivo

O principal objetivo deste projeto não é apenas concluir o desafio, mas utilizá-lo como um ambiente de experimentação para aprofundar conceitos relacionados a:

- Automação Web com **Selenium**
- Programação Orientada a Objetos
- Page Object Model
- Separação de responsabilidades
- Logging estruturado
- Persistência de dados com **MongoDB**
- Tratamento de exceções
- Resiliência de automações
- Organização e manutenibilidade do código
- Exploração de diferentes estratégias para um mesmo problema

A ideia central é simples:

> **Um problema não precisa ter apenas uma solução.**

Conhecer diferentes abordagens permite tomar decisões técnicas melhores, em vez de simplesmente repetir uma solução que já funcionou anteriormente.

---

## 🧰 Tecnologias

| Tecnologia | Utilização                        |
| ---------- | --------------------------------- |
| Python     | Linguagem principal               |
| Selenium   | Automação do navegador            |
| MongoDB    | Persistência de informações       |
| Logging    | Observabilidade e rastreabilidade |
| UV         | Gerenciamento de dependências     |
| Git        | Versionamento                     |

---

## 🏗️ Arquitetura

A estrutura do projeto busca manter as responsabilidades separadas, evitando concentrar toda a lógica dentro do script responsável pela execução da automação.

```text
rpa-challenge-selenium/
│
├── src/
│   ├── pages/
│   │   └── ...
│   │
│   ├── db/
│   │   └── ...
│   │
│   ├── settings/
│   │   └── ...
│   │
│   └── utils/
│       └── ...
│
├── logs/
│   └── ...
│
├── .env
├── .gitignore
├── pyproject.toml
└── README.md
```

A estrutura pode evoluir conforme novas necessidades surgirem durante o desenvolvimento.

O objetivo não é criar complexidade artificial, mas estabelecer limites claros entre as responsabilidades do sistema.

---

## 🧩 Page Object Model

A interação com a interface do RPA Challenge é encapsulada em Page Objects.

Isso permite separar:

**O que a automação faz**

de

**Como a automação interage com a página.**

Por exemplo:

```python
page.rpa_challenge_page()
page.form_challenge_page()
page.star_challenge_page()
```

Em vez de espalhar seletores e comandos Selenium pelo projeto.

Essa abordagem facilita manutenção e reduz o impacto de alterações na interface.

---

## 🗄️ MongoDB

O MongoDB é utilizado como mecanismo de persistência das informações relevantes da execução.

A utilização do banco permite explorar conceitos como:

- Persistência de execuções
- Armazenamento de resultados
- Histórico
- Rastreabilidade
- Consultas posteriores
- Registro de informações da automação

A camada de acesso ao banco permanece separada das regras de negócio para evitar acoplamento desnecessário.

---

## 📝 Logging

Logging é tratado como parte da arquitetura da automação, e não apenas como uma ferramenta para descobrir erros.

Os logs devem permitir responder perguntas como:

- O que aconteceu?
- Quando aconteceu?
- Em qual etapa?
- Qual registro estava sendo processado?
- A execução foi concluída?
- Onde ocorreu uma falha?

Exemplo conceitual:

```text
INFO  - Automation started
INFO  - Challenge page loaded
INFO  - Form data loaded
INFO  - Processing row 10
INFO  - Row 10 completed successfully
INFO  - Automation finished
```

Em caso de falha:

```text
ERROR - Failed while processing row 10
ERROR - Timeout waiting for form field
```

Isso transforma o log em uma ferramenta de **observabilidade e diagnóstico**.

---

## 🛡️ Resiliência

Uma automação robusta não deve depender de um único comportamento esperado da aplicação.

Durante o desenvolvimento, diferentes estratégias podem ser exploradas para situações como:

- Elementos que demoram para aparecer
- Alterações no DOM
- Timeouts
- Falhas de interação
- Dados inesperados
- Exceções de navegador
- Indisponibilidade temporária
- Reexecução de etapas

A intenção não é simplesmente adicionar `try/except` em todo o código.

Resiliência significa entender **qual é a falha**, **qual é a causa** e **qual estratégia é adequada para aquele cenário**.

---

## 🔬 Uma solução não é a única solução

Um dos principais objetivos deste projeto é explorar diferentes maneiras de resolver um mesmo problema.

Por exemplo, diante da necessidade de aguardar um elemento:

```text
Sleep
   ↓
Implicit Wait
   ↓
Explicit Wait
   ↓
Expected Conditions
   ↓
Estratégia de retry
```

Todas podem resolver determinados cenários, mas não necessariamente são equivalentes.

O objetivo é compreender:

- Quando utilizar cada abordagem
- Quais são seus impactos
- Quais são suas limitações
- Como elas afetam a estabilidade
- Qual delas torna o código mais previsível

O mesmo princípio vale para arquitetura, persistência, tratamento de erros, localização de elementos e gerenciamento do fluxo da automação.

---

## 🧠 Por que explorar diferentes tecnologias?

Conhecer apenas uma ferramenta pode tornar o desenvolvedor eficiente em determinado cenário, mas também pode criar dependência de uma única abordagem.

Já conhecer diferentes ferramentas permite comparar decisões.

Neste projeto, por exemplo, o Selenium não está sendo utilizado porque é necessariamente "melhor" que outras ferramentas.

Ele está sendo utilizado porque **conhecer outra abordagem também faz parte do aprendizado**.

A experiência anterior com outras ferramentas de automação passa a servir como referência para comparação.

O objetivo é desenvolver a capacidade de responder:

> "Qual solução faz mais sentido para este problema?"

e não:

> "Qual ferramenta eu já conheço?"

---

## 🚀 Execução

Clone o projeto:

```bash
git clone <repository-url>
cd rpa-challenge-selenium
```

Instale as dependências:

```bash
uv sync
```

Configure as variáveis de ambiente necessárias no `.env`.

## 📌 Princípios utilizados

Durante o desenvolvimento, alguns princípios são considerados:

- **Single Responsibility Principle**
- **Separation of Concerns**
- **DRY**
- **KISS**
- **Fail Fast**
- **Explicit over implicit**
- Baixo acoplamento
- Alta coesão
- Código legível
- Tratamento adequado de exceções
- Observabilidade
- Manutenibilidade

O objetivo é evitar a criação de uma automação que apenas "funciona".

A intenção é construir uma automação que também seja **compreensível, observável, testável e evolutiva**.

---

## 📈 Próximos passos

- [ ] Evoluir Page Objects
- [ ] Implementar camada de serviços
- [ ] Estruturar Repository Pattern para MongoDB
- [ ] Melhorar logging
- [ ] Explorar estratégias de retry
- [ ] Melhorar tratamento de exceções
- [ ] Adicionar configurações por ambiente
- [ ] Avaliar diferentes estratégias de espera
- [ ] Documentar decisões técnicas

---

## 👨‍💻 Sobre o projeto

Este projeto faz parte de uma série de experimentações voltadas para **RPA, Python e Engenharia de Software**.

Mais do que resolver um desafio de automação, a proposta é utilizar problemas conhecidos para experimentar novas tecnologias, comparar abordagens e desenvolver soluções cada vez mais robustas.

> **Conhecer uma solução é útil. Conhecer diferentes soluções e saber quando utilizar cada uma é engenharia.**
