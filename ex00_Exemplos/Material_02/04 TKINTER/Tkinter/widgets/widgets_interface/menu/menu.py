import tkinter as tk
from tkinter import scrolledtext, messagebox
import os
from .Modelo_menu.modelo import ModeloMenu
class TelaMenu:
    def __init__(self, master=None):
        self.janela = tk.Toplevel(master)  
        self.janela.title("Menu")
        self.janela.geometry("600x500")

        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            self.janela.iconbitmap(caminho_icone)

       
        titulo = tk.Label(
            self.janela,
            text="Como funcionam os Menus no Tkinter",
            font=("Arial", 12, "bold")
        )
        titulo.pack(pady=10)

    
        texto_explicativo = (
            "O que é um Menu?\n"
            "Um Menu é um widget especial no Tkinter usado para criar barras de menu, submenus e itens de menu.\n"
            "Menus permitem que você organize comandos e opções de forma hierárquica.\n\n"
            "Exemplo básico de criação de menu:\n"
            "import tkinter as tk\n\n"
            "root = tk.Tk()\n"
            "barra_menu = tk.Menu(root)\n"
            "menu_arquivo = tk.Menu(barra_menu, tearoff=0)\n"
            "menu_arquivo.add_command(label='Novo', command=lambda: print('Novo'))\n"
            "barra_menu.add_cascade(label='Arquivo', menu=menu_arquivo)\n"
            "root.config(menu=barra_menu)\n"
            "root.mainloop()\n\n"
            "Menus podem ter:\n"
            "- Comandos (add_command)\n"
            "- Separadores (add_separator)\n"
            "- Submenus (add_cascade)\n"
            "- Desativar/ativar itens\n\n"
            "Situações comuns de uso:\n"
            "- Barra de menus de aplicativos\n"
            "- Opções de configuração\n"
            "- Acesso rápido a funções do programa\n"
        )

        area_texto = scrolledtext.ScrolledText(
            self.janela,
            wrap=tk.WORD,
            width=70,
            height=20,
            font=("Arial", 10)
        )
        area_texto.insert(tk.INSERT, texto_explicativo)
        area_texto.config(state='disabled')
        area_texto.pack(padx=10, pady=10)

       
        frame_botoes = tk.Frame(self.janela)
        frame_botoes.pack(pady=10)

       
        btn_menu_simples = tk.Button(
            frame_botoes,
            text="Exemplo Menu Simples",
            command=self.exemplo_menu_simples,
            width=20
        )
        btn_menu_simples.grid(row=0, column=0, padx=10)

        
        btn_submenu = tk.Button(
            frame_botoes,
            text="Exemplo Submenu",
            command=self.exemplo_submenu,
            width=20
        )
        btn_submenu.grid(row=0, column=1, padx=10)

        btn_submenu_for = tk.Button(
            frame_botoes,
            text="Exemplo for",
            command=self.exemplo_submenu_for,
            width=20
        )
        btn_submenu_for.grid(row=0, column=2, padx=10)

    def exemplo_menu_simples(self):
        nova_janela = tk.Toplevel(self.janela)
        nova_janela.title("Menu Simples")
        nova_janela.geometry("300x200")

        barra_menu = tk.Menu(nova_janela)
        menu_arquivo = tk.Menu(barra_menu, tearoff=0)
        menu_arquivo.add_command(label="Novo", command=lambda: messagebox.showinfo("Menu", "Novo clicado"))
        menu_arquivo.add_command(label="Abrir", command=lambda: messagebox.showinfo("Menu", "Abrir clicado"))
        barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo)
        nova_janela.config(menu=barra_menu)

    def exemplo_submenu(self):
        nova_janela = tk.Toplevel(self.janela)
        nova_janela.title("Submenu")
        nova_janela.geometry("300x200")

        barra_menu = tk.Menu(nova_janela)
        menu_arquivo = tk.Menu(barra_menu, tearoff=0)

        
        submenu_novo = tk.Menu(menu_arquivo, tearoff=0)
        submenu_novo.add_command(label="Projeto", command=lambda: messagebox.showinfo("Submenu", "Projeto clicado"))
        submenu_novo.add_command(label="Arquivo", command=lambda: messagebox.showinfo("Submenu", "Arquivo clicado"))

        menu_arquivo.add_cascade(label="Novo", menu=submenu_novo)
        menu_arquivo.add_command(label="Abrir", command=lambda: messagebox.showinfo("Menu", "Abrir clicado"))

        barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo)
        nova_janela.config(menu=barra_menu)
    def exemplo_submenu_for(self):
        ModeloMenu(self.janela).iniciar()

    def iniciar(self):
        self.janela.mainloop()