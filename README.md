🏥 SolidarieData - Sistema de Prontuários para ONGs

O SolidarieData é uma aplicação web segura, construída em Python (Flask) e SQLAlchemy, desenhada para ajudar ONGs médicas a gerir prontuários de pacientes de forma digital, segura e eficiente.

Este sistema permite que ONGs se registem, façam login e administrem um banco de dados de pacientes, incluindo fichas de anamnese detalhadas e um histórico de acompanhamento médico contínuo, facilitando o acesso e a gestão da informação de saúde.

✨ Funcionalidades Principais

Autenticação de ONGs: Sistema de registo e login seguro para ONGs, baseado em CNPJ, email e senha com hash (bcrypt).

Gestão de Pacientes (CRUD): Criação, visualização, atualização e exclusão de prontuários de pacientes.

Prontuário Detalhado: Formulário de criação de paciente que combina dados cadastrais (baseado na Ficha de Observações) e uma ficha de anamnese completa (baseada na Ficha Médica).

Acompanhamento Médico: Os profissionais podem adicionar novas observações ao prontuário de um paciente, criando um histórico médico cronológico.

Acesso Rápido: Dashboard principal com lista de pacientes em ordem alfabética e uma barra de busca para filtrar por nome ou telefone.

Interface Moderna: Interface limpa construída com Tailwind CSS, incluindo um Modo Noturno (Dark Mode) ☀️/🌙 persistente.

🛠️ Tecnologias Utilizadas

Backend: Python 3

Framework: Flask

Banco de Dados (ORM): SQLAlchemy

Servidor (Deploy): Gunicorn

Base de Dados (Local): SQLite

Base de Dados (Produção): PostgreSQL (pronto para deploy no Render)

Autenticação: passlib[bcrypt] para hashing de senhas.

Frontend: Tailwind CSS, HTML5, JavaScript.

🚀 Como Executar Localmente

Siga estes passos para configurar e executar o projeto no seu computador.

1. Pré-requisitos

Python 3.7 ou superior

pip (gestor de pacotes do Python)

Git

2. Configuração do Ambiente

Clonar o repositório:

git clone [URL_DO_SEU_REPOSITORIO_AQUI]
cd [NOME_DA_PASTA_DO_PROJETO]


Navegar para o backend:
O código principal está na pasta backend.

cd backend


Criar e Ativar um Ambiente Virtual (Venv):
É crucial para isolar as dependências do projeto.

# Criar o venv
python -m venv venv

# Ativar no Windows (PowerShell/CMD)
.\venv\Scripts\activate

# Ativar no macOS/Linux
source venv/bin/activate


Instalar as Dependências:
(Se não tiveres um requirements.txt, cria-o primeiro com pip freeze > requirements.txt.)

pip install -r requirements.txt


Se o ficheiro não existir, instala manualmente:

pip install Flask SQLAlchemy passlib[bcrypt]


3. Executar a Aplicação

Garantir que a Base de Dados está limpa:
Como o app.py usa init_db(), ele irá criar o ficheiro projeto.db automaticamente. Se tiveres problemas, apaga o projeto.db e tenta novamente.

Executar o servidor Flask:

python app.py


Aceder ao Site:
A aplicação estará a correr em http://127.0.0.1:5000/.

Primeiro Acesso:

Abre http://127.0.0.1:5000/register no teu navegador para cadastrar a tua primeira ONG.

Depois, acede a http://127.0.0.1:5000/login para entrar no sistema.

☁️ Deploy na Nuvem

Este projeto está configurado para um deploy fácil na plataforma Render. (Ver o ficheiro INSTRUCOES_DEPLOY.md [INSTRUCOES_DEPLOY.md] para o guia passo a passo).

👥 Autores

Caio Porto

Guilherme Valadares

Heitor Campos

Maria Eduarda

Maria Júlia
