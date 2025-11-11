# Em backend/ver_usuarios.py

from db import SessionLocal, init_db
from models import User

def listar_usuarios():
    # Garante que o DB e a tabela existam
    init_db() 
    
    db = SessionLocal()
    try:
        print("--- Listando todos os usuários cadastrados ---")
        
        # 1. Busca todos os usuários no banco
        usuarios = db.query(User).all()
        
        if not usuarios:
            print("Nenhum usuário cadastrado.")
            return

        # 2. Imprime o ID e o CNPJ de cada um
        for user in usuarios:
            print(f"ID: {user.id} | CNPJ: {user.cnpj}")
            
        print("-----------------------------------------------")

    finally:
        db.close()

# Isso faz o script rodar quando você o chama
if __name__ == "__main__":
    listar_usuarios()