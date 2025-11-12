import os # Precisamos disto para ler as variáveis de ambiente
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# --- LÓGICA DE DEPLOY ---
# 1. Procura pela URL do banco de dados na nuvem (que o Render vai definir)
DATABASE_URL_PRODUCAO = os.environ.get('DATABASE_URL')

# 2. Se não encontrar (estamos a testar no nosso PC), usa o SQLite local
if DATABASE_URL_PRODUCAO:
    # Corrige a URL do Render para ser compatível com SQLAlchemy
    # (O Render usa "postgres://", o SQLAlchemy 1.4+ prefere "postgresql://")
    if DATABASE_URL_PRODUCAO.startswith("postgres://"):
        DATABASE_URL_PRODUCAO = DATABASE_URL_PRODUCAO.replace("postgres://", "postgresql://", 1)
    
    SQLALCHEMY_DATABASE_URL = DATABASE_URL_PRODUCAO
else:
    # Se estiver a rodar localmente, continua a usar o ficheiro projeto.db
    print("Aviso: A correr em modo local. A usar banco de dados SQLite.")
    SQLALCHEMY_DATABASE_URL = "sqlite:///./projeto.db" 
# --- FIM DA LÓGICA ---

# A configuração do engine agora usa a URL que definimos acima
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    # O connect_args é específico do SQLite, só o usamos se não estivermos na produção
    connect_args={"check_same_thread": False} if "sqlite" in SQLALCHEMY_DATABASE_URL else {}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Função para criar as tabelas (não muda)
def init_db():
    Base.metadata.create_all(bind=engine)