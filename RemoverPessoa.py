import tkinter as tk
from tkinter import simpledialog, messagebox

class RemoverPessoa:
    def __init__(self, master, filename):
        self.master = master
        self.filename = filename

    def ler_dados(self):
        """Lê os dados do arquivo e retorna uma lista de linhas."""
        with open(self.filename, 'r', encoding='utf-8') as file:
            return file.readlines()

    def escrever_dados(self, data_list):
        """Escreve a lista de dados de volta no arquivo."""
        with open(self.filename, 'w', encoding='utf-8') as file:
            file.writelines(data_list)

    def validar_contrato(self, contrato):
        """Verifica se o contrato tem 12 dígitos numéricos."""
        return contrato.isdigit() and len(contrato) == 12

    def remover_pessoa(self):
        contrato = simpledialog.askstring("Remover Pessoa", "Digite o número do contrato (12 dígitos):", parent=self.master)
        
        if contrato:
            contrato = contrato.zfill(12)  # Preenche com zeros à esquerda até completar 12 dígitos

            # Validação do contrato
            if not self.validar_contrato(contrato):
                messagebox.showerror("Erro", "Número de contrato inválido. Deve conter exatamente 12 dígitos numéricos.")
                return

            data_list = self.ler_dados()
            nova_lista = []
            pessoa_encontrada = False

            for i, linha in enumerate(data_list):
                contrato_na_linha = linha[30:43].strip()  # Ajuste os índices conforme necessário
                cpf_na_linha = linha[154:166].strip()  # Assumindo que o CPF está nessa posição

                if contrato_na_linha == contrato:
                    pessoa_encontrada = True
                    detalhes = f"Contrato: {contrato}\nCPF: {cpf_na_linha if cpf_na_linha else 'CPF não encontrado'}"
                    
                    # Primeira confirmação
                    confirmar = messagebox.askyesno("Confirmação", f"Você deseja remover esta pessoa?\n\n{detalhes}")
                    
                    if confirmar:
                        # Segunda confirmação
                        confirmar_final = messagebox.askyesno("Confirmação Final", f"Tem certeza de que deseja remover a pessoa?\n\n{detalhes}")
                        
                        if confirmar_final:
                            continue  # Não adiciona essa linha à nova lista, removendo a pessoa
                        else:
                            messagebox.showinfo("Cancelamento", "Remoção cancelada.")
                            return
                    else:
                        messagebox.showinfo("Cancelamento", "Remoção cancelada.")
                        return
                else:
                    nova_lista.append(linha)

            if pessoa_encontrada:
                self.escrever_dados(nova_lista)
                messagebox.showinfo("Remoção", "Pessoa removida com sucesso.")
            else:
                messagebox.showinfo("Resultado", "Pessoa não encontrada.")
        else:
            messagebox.showinfo("Cancelamento", "Operação cancelada.")
