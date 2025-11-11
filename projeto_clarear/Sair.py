
import tkinter as tk
from tkinter import messagebox

class Sair:
    def __init__(self, master):
        self.master = master

    def sair_do_programa(self):
        if messagebox.askyesno("Sair", "Você tem certeza que deseja sair?"):
            self.master.destroy()
