# Manual de desenvolvimento

## Turtoriais básicos

### Tutorial Completo de GitHub: Criando uma Branch a partir de uma Issue

Este tutorial é destinado para iniciantes no GitHub, e vai ensinar como criar uma branch a partir de uma issue. Vamos utilizar o link do projeto fornecido: [projeto_clarear](https://github.com/assistof/projeto_clarear).

### Usando a Página do GitHub

#### Passo 1: Criando uma Issue

1. **Acesse o repositório do projeto:**
   - Vá para [projeto_clarear](https://github.com/assistof/projeto_clarear).
   
2. **Crie uma nova issue:**
   - Clique na aba `Issues` no topo da página.
   - Clique no botão verde `New issue`.
   - Preencha o título e a descrição da issue. Forneça o máximo de detalhes possível sobre o problema ou a nova funcionalidade.
   - Clique em `Submit new issue`.

#### Passo 2: Criando uma Branch a partir da Issue

1. **Acesse a Issue criada:**
   - Após criar a issue, você será redirecionado para a página da issue.
   - Selecione a issue que você acabou de criar ou a issue já existente.

2. **Criar a branch:**
   - No lado direito da página da issue, você verá a seção `Development`.
   - Clique no link `Create a branch` (ou `Create branch`).

   > GitHub automaticamente sugere um nome para a branch baseado no título da issue. O nome geralmente segue o formato `issue-<número-da-issue>`.

3. **Confirme a criação da branch:**
   - Após clicar em `Create branch`, a nova branch será criada e você será redirecionado para a página de commits da nova branch.

#### Passo 3: Trabalhando na Nova Branch

1. **Clone o repositório (se ainda não o fez):**
   - Abra seu terminal ou prompt de comando.
   - Clone o repositório para seu computador:
     ```bash
     git clone https://github.com/assistof/projeto_clarear.git
     ```
   - Navegue para o diretório do projeto:
     ```bash
     cd projeto_clarear
     ```

2. **Troque para a nova branch:**
   - Liste as branches remotas para garantir que a nova branch foi criada:
     ```bash
     git fetch
     git branch -r
     ```
   - Troque para a nova branch:
     ```bash
     git checkout -b issue-<número-da-issue> origin/issue-<número-da-issue>
     ```

3. **Faça suas alterações no código:**
   - Edite os arquivos conforme necessário para resolver a issue ou adicionar a nova funcionalidade.
   - Adicione e commit suas mudanças:
     ```bash
     git add .
     git commit -m "Descrição das mudanças feitas"
     ```

4. **Envie as alterações para o GitHub:**
   - Envie sua branch para o repositório remoto:
     ```bash
     git push origin issue-<número-da-issue>
     ```

#### Passo 4: Criando um Pull Request (PR)

1. **Abra um Pull Request:**
   - Vá para a página do repositório no GitHub.
   - Clique na aba `Pull requests`.
   - Clique no botão `New pull request`.
   - Selecione a branch base (geralmente `main` ou `master`) e a branch comparada (a sua nova branch `issue-<número-da-issue>`).
   - Preencha o título e a descrição do Pull Request.
   - Clique em `Create pull request`.

#### Passo 5: Adicionando Comentários

1. **Comente na Issue:**
   - Vá para a página da issue associada.
   - Adicione um comentário mencionando que você criou um Pull Request para resolver a issue. Exemplo:
     ```
     Criei um Pull Request #<número-do-pr> para resolver esta issue.
     ```

2. **Comente no Pull Request:**
   - Vá para a página do Pull Request.
   - Adicione comentários detalhando suas mudanças ou solicitando revisões.

#### Passo 6: Revisão e Merge

1. **Revisão do Código:**
   - Alguém da equipe deve revisar seu Pull Request.
   - Responda a qualquer feedback e faça ajustes conforme necessário.

2. **Merge do Pull Request:**
   - Uma vez aprovado, você ou um mantenedor do projeto pode fazer o merge do Pull Request.
   - Clique no botão `Merge pull request` e, em seguida, `Confirm merge`.

#### Passo 7: Fechando a Issue

1. **Feche a Issue:**
   - Uma vez que o Pull Request foi merged, vá para a página da issue.
   - Clique no botão `Close issue`.

---

### Usando a CLI do Git

#### Passo 1: Criando uma Issue

1. **Acesse o repositório do projeto:**
   - Vá para [projeto_clarear](https://github.com/assistof/projeto_clarear).
   
2. **Crie uma nova issue:**
   - Clique na aba `Issues` no topo da página.
   - Clique no botão verde `New issue`.
   - Preencha o título e a descrição da issue. Forneça o máximo de detalhes possível sobre o problema ou a nova funcionalidade.
   - Clique em `Submit new issue`.

#### Passo 2: Criando uma Branch a partir da Issue

1. **Clone o repositório (se ainda não o fez):**
   - Abra seu terminal ou prompt de comando.
   - Clone o repositório para seu computador:
     ```bash
     git clone https://github.com/assistof/projeto_clarear.git
     ```
   - Navegue para o diretório do projeto:
     ```bash
     cd projeto_clarear
     ```

2. **Troque para a branch principal:**
   - Para garantir que você está na branch principal (`main` ou `master`):
     ```bash
     git checkout main  # ou 'master' se essa for a branch principal
     ```

3. **Atualize a branch principal:**
   - Antes de criar a nova branch, certifique-se de que a branch principal está atualizada:
     ```bash
     git pull origin main  # ou 'master' se essa for a branch principal
     ```

4. **Crie a nova branch a partir da issue:**
   - Se a issue já foi criada, você pode usar o número da issue para nomear a nova branch:
     ```bash
     git checkout -b issue-<número-da-issue>
     ```
   - Isso cria e muda para a nova branch chamada `issue-<número-da-issue>`.

#### Passo 3: Trabalhando na Nova Branch

1. **Faça suas alterações no código:**
   - Edite os arquivos conforme necessário para resolver a issue ou adicionar a nova funcionalidade.
   - Adicione e commit suas mudanças:
     ```bash
     git add .
     git commit -m "Descrição das mudanças feitas"
     ```

2. **Envie as alterações para o GitHub:**
   - Envie sua branch para o repositório remoto:
     ```bash
     git push origin issue-<número-da-issue>
     ```

#### Passo 4: Criando um Pull Request (PR)

1. **Abra um Pull Request:**
   - No seu terminal, você pode abrir o link para criar um PR:
     ```bash
     gh pr create --base main --head issue-<número-da-issue> --title "Título do PR" --body "Descrição detalhada do PR"
     ```
   - Alternativamente, vá para a página do repositório no GitHub.
   - Clique na aba `Pull requests`.
   - Clique no botão `New pull request`.
   - Selecione a branch base (geralmente `main` ou `master`) e a branch comparada (a sua nova branch `issue-<número-da-issue>`).
   - Preencha o título e a descrição do Pull Request.
   - Clique em `Create pull request`.

#### Passo 5: Adicionando Comentários

1. **Comente na Issue:**
   - Vá para a página da issue associada.
   - Adicione um comentário mencionando que você criou um Pull Request para resolver a issue. Exemplo:
     ```
     Criei um Pull Request #<número-do-pr> para resolver esta issue.
     ```

2. **Comente no Pull Request:**
   - Vá para a página do Pull Request.
   - Adicione comentários detalhando suas mudanças ou solicitando revisões.

#### Passo 6: Revisão e Merge

1. **Revisão do Código:**
   - Alguém da equipe deve revisar seu Pull Request.
   - Responda a qualquer feedback e faça ajustes conforme necessário.

2. **Merge do Pull Request:**
   - Uma vez aprovado, você ou um mantenedor do projeto pode fazer o merge do Pull Request.
   - Clique no botão `Merge pull request` e, em seguida, `Confirm merge`.

#### Passo 7: Fechando a Issue

1. **Feche a Issue:**
   - Uma vez que o Pull Request foi merged, vá para a página da issue.
   - Clique no botão `Close issue`.

---

Parabéns! Você criou com sucesso uma branch a partir de uma issue, fez as mudanças necessárias, criou um Pull Request e fechou a issue. 

Este é um guia básico de como criar e fechar uma branch no projeto.
