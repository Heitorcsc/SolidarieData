import tkinter as tk
from tkinter import simpledialog, messagebox
from db import SessionLocal
from models import Report


class BuscarPessoa:
    def __init__(self, master):
        self.master = master

    def buscar_pessoa(self):
        contrato = simpledialog.askstring("Buscar Pessoa", "Digite o número do contrato:", parent=self.master)
        if not contrato:
            messagebox.showinfo("Cancelamento", "Operação cancelada.")
            return

        contrato = contrato.zfill(12)

        db = SessionLocal()
        resultado = db.query(Report).filter(Report.title == contrato).first()
        db.close()

        if resultado:
            msg = f"""
Pessoa encontrada!
Contrato: {resultado.title}
Conteúdo: {resultado.content}
ID do dono: {resultado.owner_id}
"""
            messagebox.showinfo("Resultado", msg)
        else:
            messagebox.showinfo("Resultado", "Pessoa não encontrada.")
