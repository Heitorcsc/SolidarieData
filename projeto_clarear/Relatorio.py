import tkinter as tk
from tkinter import messagebox
import numpy as np
class Relatorio:
   def __init__(self, master, filename):
       self.master = master
       self.filename = filename
   def ler_dados(self):
       with open(self.filename, 'r', encoding='utf-8') as file:
           return file.readlines()
   def gerar_relatorio(self):
       data_list = self.ler_dados()
       valores_doacoes = []
       for i, linha in enumerate(data_list):
           if linha.startswith('E0'):
               valor_doacao_na_linha = linha[63:72].strip()
               if valor_doacao_na_linha:
                   try:
                       valor_doacao = float(valor_doacao_na_linha) / 100
                       valores_doacoes.append(valor_doacao)
                   except ValueError:
                       print(f"Erro ao converter valor da doação na linha {i + 1}")
       total_doadores = len(valores_doacoes)
       valor_total_doacoes = np.sum(valores_doacoes)
       relatorio_str = f"--- Relatório ---\nTotal de Doadores: {total_doadores}\nValor Total de Doações: {valor_total_doacoes:.2f}"
       messagebox.showinfo("Relatório", relatorio_str)
# Observação: Este código assume que o valor da doação está em uma posição fixa em cada linha que começa com "E0".
# Ajuste os índices e a lógica de conversão de valor conforme necessário para corresponder ao formato do seu arquivo.
