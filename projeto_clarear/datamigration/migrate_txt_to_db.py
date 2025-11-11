from db import init_db, SessionLocal
from models import User, Report

init_db()
db = SessionLocal()

with open("../Setembro.txt", "r", encoding="utf-8") as f:
    for line in f:
        # exemplo: pegar contrato, doacao, cpf com slicing correto
        contrato = line[30:42].strip()   # ajuste conforme seu formato real
        doacao = line[53:68].strip()
        cpf = line[150:167].strip()
        # Aqui você decide como mapear esses campos em reports/users
        # Exemplo: criar um relatório com título = contrato
        rpt = Report(title=f"Contrato {contrato}", content=f"Doação: {doacao} CPF: {cpf}")
        db.add(rpt)
db.commit()
db.close()
