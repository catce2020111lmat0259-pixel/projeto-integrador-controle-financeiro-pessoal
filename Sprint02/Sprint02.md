# Sprint 02

## Objetivo Geral
Dar continuidade ao projeto iniciado na Sprint 1, evoluindo da fase de concepção para planejamento e prototipação funcional.  
Nesta sprint, o grupo realizou o backlog utilizando as histórias HU01, HU02, HU04 e HU09, além de criar protótipos intermediários que representam as principais interações do sistema.

---

## Objetivos Específicos
- Criar novas telas e aperfeiçoar o protótipo iniciado na Sprint 1.  
- Garantir coerência visual entre as telas (cores, fontes, botões, ícones).  
- Representar as histórias de usuário priorizadas.  
- Adicionar interações básicas (links entre telas e botões clicáveis).  

---

## Etapas da Sprint

### Etapa 1 – Planejamento da Sprint (Sprint Planning)
**Objetivo:** Definir o foco da semana e selecionar as histórias de usuário que seriam trabalhadas.  

---

### Etapa 2 – Refinamento das Histórias de Usuário
**Objetivo:** Tornar as histórias mais claras, completas e mensuráveis.  
**Tarefas:**
- Revisar as histórias criadas na Sprint 1 e reescrever as genéricas.  
- Adicionar critérios de aceitação para cada história.  
- Identificar cenários de uso, descrevendo como o usuário poderá interagir com o sistema.  

---

### Etapa 3 – Prototipação Intermediária
**Objetivo:** Criar novas telas e aperfeiçoar o protótipo iniciado na Sprint 1.  
**Tarefas:**
- Desenvolver ao menos duas novas telas.  
- Representar as histórias priorizadas da sprint.  
- Manter coerência visual com a tela inicial.  
- Adicionar interações básicas (links e botões clicáveis).  

---

### Etapa 4 – Cerimônias do Scrum
**Objetivo:** Simular práticas do Scrum para organizar o fluxo de trabalho.  
**Tarefas:**
- Realizar ao menos uma *Daily* (registro breve por mensagem).  
- Conduzir uma *Sprint Review* para apresentar os protótipos criados.  
- Realizar uma *Retrospective* destacando:
  - O que funcionou bem.  
  - O que pode melhorar.  
  - Ajustes para a próxima sprint.  

---

## Detalhamento das Histórias de Usuário e Critérios de Aceitação

### HU01: Inserir receitas manualmente
*"Como usuário do sistema, quero inserir minhas receitas manualmente (ex.: salário, mesada), para acompanhar minha entrada de dinheiro."*

- **CA01 - Cadastro de receita válido:**  
  Dado que o usuário preenche os campos obrigatórios (valor, data, categoria),  
  Quando confirmar o cadastro,  
  Então a receita deve ser registrada com sucesso.  

- **CA02 - Validação de campos obrigatórios:**  
  Dado que o usuário não preenche um ou mais campos obrigatórios,  
  Quando tentar salvar,  
  Então o sistema deve exibir mensagem de erro.  

- **CA03 - Valor inválido:**  
  Dado que o usuário insere um valor negativo ou inválido,  
  Quando tentar salvar,  
  Então o sistema deve impedir o cadastro e informar o erro.  

---

### HU02: Inserir despesas manualmente
*"Como usuário do sistema, quero inserir minhas despesas manualmente (ex.: alimentação, transporte, lazer), para controlar meus gastos."*

- **CA01 - Cadastro de despesa válido:**  
  Dado que o usuário informa valor, data e categoria,  
  Quando confirmar,  
  Então a despesa deve ser registrada.  

- **CA02 - Categoria obrigatória:**  
  Dado que nenhuma categoria foi selecionada,  
  Quando tentar salvar,  
  Então o sistema deve solicitar a seleção.  

- **CA03 - Valor inválido:**  
  Dado que o valor inserido é inválido,  
  Quando salvar,  
  Então o sistema deve bloquear o cadastro.  

---

### HU04: Classificar receitas e despesas por categorias
*"Como usuário do sistema, quero classificar receitas e despesas por categorias, para organizar melhor minhas finanças."*

- **CA01 - Seleção de categoria:**  
  Dado que o usuário está cadastrando um lançamento,  
  Quando escolhe uma categoria,  
  Então o sistema deve associá-la ao registro.  

- **CA02 - Categorias pré-definidas:**  
  Dado que o sistema possui categorias padrão (alimentação, transporte, etc.),  
  Quando o usuário visualizar as opções,  
  Então elas devem estar disponíveis.  

- **CA03 - Categoria personalizada:**  
  Dado que o usuário deseja criar nova categoria,  
  Quando cadastrar,  
  Então ela deve aparecer para uso futuro.  

---

### HU09: Criar e personalizar metas financeiras
*"Como usuário do sistema, quero criar e personalizar metas financeiras, para organizar melhor meus objetivos e acompanhar o progresso em relação aos gastos."*

- **CA01 - Meta criada com sucesso:**  
  Dado que o usuário acessa a tela de metas,  
  Quando ele escreve uma meta personalizada e clica em “Salvar”,  
  Então o sistema deve registrar a meta e exibir a mensagem: “Meta financeira criada com sucesso.”  

- **CA02 - Listagem de metas:**  
  Dado que o usuário já cadastrou metas,  
  Quando ele acessa a tela de metas,  
  Então o sistema deve exibir todas as metas criadas, organizadas por período ou categoria definida pelo usuário.  

- **CA03 - Edição de meta:**  
  Dado que o usuário possui uma meta cadastrada,  
  Quando ele seleciona a opção “Editar” e alterar o texto ou período,  
  Então o sistema deve atualizar a meta e confirmar com a mensagem: “Meta atualizada com sucesso.”  

- **CA04 - Exclusão de meta:**  
  Dado que o usuário possui uma meta cadastrada,  
  Quando ele seleciona a opção “Excluir”,  
  Então o sistema deve remover a meta e confirmar com a mensagem: “Meta excluída com sucesso.”  

- **CA05 - Acompanhamento de metas:**  
  Dado que o usuário possui metas cadastradas,  
  Quando ele acessa a tela de acompanhamento,  
  Então o sistema deve mostrar o status de cada meta (“em andamento”, “concluída”, “não atingida”), conforme os gastos registrados.  

---

## Reuniões Realizadas
- **26/03:** Escolha das histórias de usuário retiradas do Product Backlog.  
- **04/04:** Definição dos papéis de cada integrante para a prototipação.  
- **09/04:** Entrega e finalização da escrita, revisão de conteúdo da Sprint 02 e entrega dos protótipos.  

---

## Entregas da Sprint
- Backlog atualizado com histórias H001, H002, H004 e H009.  
- Protótipos intermediários representando interações principais.  
- Novas telas desenvolvidas e integradas ao protótipo inicial.  
- Registro das cerimônias do Scrum realizadas.  
- Documentação das histórias de usuário e critérios de aceitação.  
- Registro das reuniões realizadas durante a sprint.
