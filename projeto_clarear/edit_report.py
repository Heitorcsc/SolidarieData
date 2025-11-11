import tkinter as tk
from tkinter import simpledialog, messagebox
import re
from projeto_clarear.backend.add_report import editar_pessoa_no_db  # nova função no banco


class EditarPessoa:
    def __init__(self, master):
        self.master = master

    def perguntar_opcao_alteracao(self):
        def selecionar_opcao(opcao):
            nonlocal resposta
            resposta = opcao
            dialogo.destroy()

        resposta = None
        dialogo = tk.Toplevel(self.master)
        dialogo.title("Escolha")

        largura, altura = 300, 200
        tela_largura = dialogo.winfo_screenwidth()
        tela_altura = dialogo.winfo_screenheight()
        pos_x = (tela_largura // 2) - (largura // 2)
        pos_y = (tela_altura // 2) - (altura // 2)
        dialogo.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

        tk.Label(dialogo, text="Você deseja alterar a doação ou o CPF?").pack(padx=20, pady=20)
        tk.Button(dialogo, text="Alterar Doação", command=lambda: selecionar_opcao("doacao")).pack(padx=10, pady=5)
        tk.Button(dialogo, text="Alterar CPF", command=lambda: selecionar_opcao("cpf")).pack(padx=10, pady=5)
        tk.Button(dialogo, text="Cancelar", command=lambda: selecionar_opcao("cancelar")).pack(padx=10, pady=5)

        dialogo.grab_set()
        dialogo.wait_window()
        return resposta

    def confirmar_alteracoes(self, contrato, nova_doacao, novo_cpf):
        confirmacao = tk.Toplevel(self.master)
        confirmacao.title("Confirmar Alterações")

        largura, altura = 300, 200
        tela_largura = confirmacao.winfo_screenwidth()
        tela_altura = confirmacao.winfo_screenheight()
        pos_x = (tela_largura // 2) - (largura // 2)
        pos_y = (tela_altura // 2) - (altura // 2)
        confirmacao.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

        tk.Label(confirmacao, text=f"Confirme as alterações:\n\n"
                                   f"Contrato: {contrato}\n"
                                   f"Nova Doação: {nova_doacao}\n"
                                   f"Novo CPF: {novo_cpf}").pack(padx=20, pady=20)

        def confirmar():
            confirmacao.resultado = True
            confirmacao.destroy()

        def cancelar():
            confirmacao.resultado = False
            confirmacao.destroy()

        tk.Button(confirmacao, text="Confirmar", command=confirmar).pack(padx=10, pady=5)
        tk.Button(confirmacao, text="Cancelar", command=cancelar).pack(padx=10, pady=5)

        confirmacao.grab_set()
        confirmacao.wait_window()

        return getattr(confirmacao, "resultado", False)

    def editar_pessoa(self):
        contrato = simpledialog.askstring("Editar Pessoa", "Digite o número do contrato (12 dígitos):", parent=self.master)
        if not contrato:
            messagebox.showinfo("Cancelamento", "Operação Cancelada.")
            return

        contrato = contrato.zfill(12)
        opcao_alteracao = self.perguntar_opcao_alteracao()

        if opcao_alteracao == "cancelar" or not opcao_alteracao:
            messagebox.showinfo("Cancelamento", "Operação Cancelada.")
            return

        nova_doacao, novo_cpf = None, None

        if opcao_alteracao == "doacao":
            nova_doacao = simpledialog.askstring("Nova Doação", "Digite o valor da doação (15 dígitos):", parent=self.master)
            if not nova_doacao or not nova_doacao.isdigit() or len(nova_doacao) != 15:
                messagebox.showerror("Erro", "O valor da doação deve ter exatamente 15 dígitos numéricos.")
                return

        elif opcao_alteracao == "cpf":
            novo_cpf = simpledialog.askstring("Novo CPF", "Digite o CPF (11 dígitos, opcional):", parent=self.master)
            novo_cpf = re.sub(r"\D", "", novo_cpf or "")
            if len(novo_cpf) != 11:
                messagebox.showerror("Erro", "O CPF deve ter exatamente 11 dígitos numéricos.")
                return

        if not self.confirmar_alteracoes(contrato, nova_doacao, novo_cpf):
            messagebox.showinfo("Cancelamento", "Alterações canceladas.")
            return

        sucesso = editar_pessoa_no_db(contrato, nova_doacao, novo_cpf)
        if sucesso:
            messagebox.showinfo("Sucesso", "Pessoa atualizada no banco de dados com sucesso.")
        else:
            messagebox.showerror("Erro", "Pessoa não encontrada no banco de dados.")
