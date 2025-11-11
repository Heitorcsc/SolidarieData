import bcrypt
from pycpfcnpj import cpfcnpj

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(password: str, password_hash: str) -> bool:
    return bcrypt.checkpw(password.encode(), password_hash.encode())

def is_valid_cnpj(cnpj: str) -> bool:
    
    return cpfcnpj.validate(cnpj)
