import tkinter as tk
from tkinter import filedialog, messagebox
import csv

class ExportarCSV:
    def __init__(self, master, filename):
        self.master = master
        self.filename = filename

    def ler_dados(self):
        data_list = []
        with open(self.filename, 'r', encoding='utf-8') as file:
            for linha in file:
                if linha.startswith('E0'):
                    data_list.append(linha.strip().split())  # Divide a linha em partes e adiciona à lista
        return data_list

    def exportar_para_csv(self):
        data_list = self.ler_dados()
        filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")], parent=self.master)
        if filename:
            with open(filename, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=';')
                for pessoa in data_list:
                    writer.writerow(pessoa)  # Escreve cada pessoa como uma linha no arquivo CSV
            messagebox.showinfo("Exportação", f"Dados exportados com sucesso para {filename}")

# Observação: O código acima está dividindo cada linha em partes baseadas em espaços. Dependendo do formato exato do seu arquivo,
# você pode precisar ajustar a lógica de divisão da linha para corresponder ao formato do seu arquivo.
