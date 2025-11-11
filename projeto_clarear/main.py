import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import os
from projeto_clarear.backend.add_report import AdicionarPessoa
from projeto_clarear.search_report import BuscarPessoa
from RemoverPessoa import RemoverPessoa
from projeto_clarear.edit_report import EditarPessoa
from Relatorio import Relatorio
from ExportarCSV import ExportarCSV
from Sair import Sair
from tkinter import ttk

class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25

        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")

        label = tk.Label(self.tooltip, text=self.text, background="lightyellow", relief="solid", borderwidth=1)
        label.pack()

    def hide_tooltip(self, event):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None
            
class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title('Login - Programa Clarear')
        #print("vidaloka")

        # Obtendo as dimensões da tela
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Definindo o tamanho da janela
        window_width = 640
        window_height = 380
        
         # Calculando a posição para centralizar a janela
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        
        # Configurando geometria da janela
        self.root.geometry(f'{window_width}x{window_height}+{x}+{y}')
        
        self.create_login()
        self.setup_close_confirmation()
        
        # Carregar e definir o ícone da janela
        #self.load_window_icon('caminho_para_o_icone.ico')  # Substitua pelo caminho do seu arquivo de ícone
        

    def load_window_icon(self, icon_path):
        try:
            self.root.iconbitmap(icon_path)  # Para Windows, usando arquivo .ico
            # Em sistemas que não suportam .ico, você pode usar:
            # img = tk.PhotoImage(file='caminho_para_imagem.png')
            # self.root.iconphoto(True, img)
        except Exception as e:
            print(f"Erro ao carregar o ícone da janela: {e}")


    def create_login(self):
        self.load_logo()

        self.username_label = tk.Label(self.root, text='Usuário:')
        self.username_label.pack(pady=10)

        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(self.root, text='Senha:')
        self.password_label.pack(pady=10)

        self.password_entry = tk.Entry(self.root, show='*')
        self.password_entry.pack(pady=5)

        self.login_button = tk.Button(self.root, text='Entrar', command=self.login)
        self.login_button.pack(pady=10)

    def load_logo(self):
        logo_path = 'logo.ico'
        if os.path.exists(logo_path):
            try:
                logo_image = Image.open(logo_path).resize((160, 120), Image.LANCZOS)
                self.logo_photo = ImageTk.PhotoImage(logo_image)
                logo_label = tk.Label(self.root, image=self.logo_photo)
                logo_label.pack(pady=10)
            except Exception as e:
                messagebox.showwarning('Aviso', f'Erro ao carregar o logo: {str(e)}')

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == 'admin' and password == 'admin':
            self.selecionar_arquivo()
        else:
            messagebox.showerror('Erro', 'Credenciais inválidas!')

    def selecionar_arquivo(self):
        filename = filedialog.askopenfilename(title='Selecione o arquivo de dados', filetypes=[('Text Files', '*.txt'), ('CSV Files', '*.csv')])
        if filename:
            self.open_main_menu(filename)
        else:
            messagebox.showerror("Erro", "Nenhum arquivo selecionado. A aplicação será encerrada.")
            self.root.destroy()

    def open_main_menu(self, filename):
        self.root.destroy()
        root = tk.Tk()
        app = MainMenu(root, filename)
        root.mainloop()

    def setup_close_confirmation(self):
        self.root.protocol("WM_DELETE_WINDOW", self.confirm_close)

    def confirm_close(self):
        result = messagebox.askquestion('Fechar', 'Deseja fechar a aplicação?')
        if result == 'yes':
            self.root.destroy()

class MainMenu:
    def __init__(self, root, filename):
        self.root = root
        self.root.title('Menu Principal - Programa Clarear')
        
        # Obtendo as dimensões da tela
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Definindo o tamanho da janela
        window_width = 640
        window_height = 380
        
         # Calculando a posição para centralizar a janela
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        
        # Configurando geometria da janela
        
        self.root.geometry(f'{window_width}x{window_height}+{x}+{y}')
        
        self.filename = filename

        self.create_menu()
        self.setup_close_confirmation()

    def create_menu(self):
        menu_frame = tk.Frame(self.root)
        menu_frame.pack(pady=20)

        label = tk.Label(menu_frame, text='Selecione uma opção:')
        label.pack()

        ttk.Button(menu_frame, text='Adicionar Pessoa', command=self.adicionar_pessoa).pack(pady=10)
        ttk.Button(menu_frame, text='Buscar Pessoa', command=self.buscar_pessoa).pack(pady=10)
        ttk.Button(menu_frame, text='Remover Pessoa', command=self.remover_pessoa).pack(pady=10)
        ttk.Button(menu_frame, text='Editar Pessoa', command=self.editar_pessoa).pack(pady=10)
        ttk.Button(menu_frame, text='Relatório', command=self.gerar_relatorio).pack(pady=10)
        ttk.Button(menu_frame, text='Exportar para CSV', command=self.exportar_para_csv).pack(pady=10)
        ttk.Button(menu_frame, text='Sair', command=self.sair_do_programa).pack(pady=10)

        # Adicionar dicas de ferramentas aos botões
        ToolTip(ttk.Button(menu_frame, text='Adicionar Pessoa'), 'Adicione uma nova pessoa')
        ToolTip(ttk.Button(menu_frame, text='Buscar Pessoa'), 'Busque informações de uma pessoa')
        ToolTip(ttk.Button(menu_frame, text='Remover Pessoa'), 'Remova uma pessoa')
        ToolTip(ttk.Button(menu_frame, text='Editar Pessoa'), 'Edite informações de uma pessoa')
        ToolTip(ttk.Button(menu_frame, text='Relatório'), 'Gere um relatório')
        ToolTip(ttk.Button(menu_frame, text='Exportar para CSV'), 'Exporte os dados para um arquivo CSV')
        ToolTip(ttk.Button(menu_frame, text='Sair'), 'Sair do programa')


    def adicionar_pessoa(self):
        AdicionarPessoa(self.root, self.filename).adicionar_pessoa()

    def buscar_pessoa(self):
        BuscarPessoa(self.root, self.filename).buscar_pessoa()

    def remover_pessoa(self):
        RemoverPessoa(self.root, self.filename).remover_pessoa()

    def editar_pessoa(self):
        EditarPessoa(self.root, self.filename).editar_pessoa()

    def gerar_relatorio(self):
        Relatorio(self.root, self.filename).gerar_relatorio()

    def exportar_para_csv(self):
        ExportarCSV(self.root, self.filename).exportar_para_csv()

    def sair_do_programa(self):
        Sair(self.root).sair_do_programa()

    def setup_close_confirmation(self):
        self.root.protocol("WM_DELETE_WINDOW", self.confirm_close)

    def confirm_close(self):
        result = messagebox.askquestion('Fechar', 'Deseja fechar a aplicação?')
        if result == 'yes':
            self.root.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    login = LoginWindow(root)
    root.mainloop()
