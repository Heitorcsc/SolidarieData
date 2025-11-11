import tkinter as tk
from tkinter import simpledialog, messagebox
from projeto_clarear.search_report import BuscarPessoa
from db import SessionLocal
from models import Report


class AdicionarPessoa:
    def __init__(self, master):
        self.master = master
        self.validador = self.ValidadorEntrada()
        self.buscar_pessoa = BuscarPessoa(master)

    def solicitar_dados(self):
        contrato = simpledialog.askstring("Novo Contrato", "Digite o número do contrato (Até 12 Dígitos):", parent=self.master)
        doacao = simpledialog.askstring("Nova Doação", "Digite o valor da doação (Até 15 Dígitos):", parent=self.master)
        cpf = simpledialog.askstring("Novo CPF", "Digite o CPF (11 dígitos, opcional):", parent=self.master)
        return contrato, doacao, cpf

    def formatar_dados(self, contrato, doacao, cpf):
        contrato_formatado = self.validador.formatar_entrada(contrato, 12, 'num')
        doacao_formatada = self.validador.formatar_entrada(doacao, 15, 'num')
        cpf_formatado = self.validador.formatar_entrada(cpf, 17, 'num') if cpf else '0' * 17
        return contrato_formatado, doacao_formatada, cpf_formatado

    def adicionar_pessoa(self, owner_id=1):
        contrato, doacao, cpf = self.solicitar_dados()
        if not contrato or not doacao:
            messagebox.showwarning("Aviso", "Contrato e doação são obrigatórios.")
            return

        contrato_formatado, doacao_formatada, cpf_formatado = self.formatar_dados(contrato, doacao, cpf)

        db = SessionLocal()

        # 🔍 Verifica duplicação
        existente = db.query(Report).filter(Report.title == contrato_formatado).first()
        if existente:
            db.close()
            messagebox.showwarning("Duplicação", f"Pessoa já cadastrada com o contrato: {contrato_formatado}")
            return

        # 💾 Cria o novo registro
        novo_relatorio = Report(
            title=contrato_formatado,
            content=f"Doação: {doacao_formatada} | CPF: {cpf_formatado}",
            owner_id=owner_id
        )

        db.add(novo_relatorio)
        db.commit()
        db.close()

        messagebox.showinfo("Adição", f"Pessoa adicionada com sucesso.\n\nContrato: {contrato_formatado}\nDoação: {doacao_formatada}\nCPF: {cpf_formatado}")

    class ValidadorEntrada:
        def formatar_entrada(self, entrada, tamanho, tipo='str'):
            if not entrada:
                return '0' * tamanho
            if tipo == 'num':
                entrada = ''.join(filter(str.isdigit, entrada))
            return entrada.zfill(tamanho)
