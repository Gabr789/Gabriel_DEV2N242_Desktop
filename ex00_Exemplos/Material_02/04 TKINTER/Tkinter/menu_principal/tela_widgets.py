


from Tkinter.imports import *
import tkinter as tk
from tkinter import ttk


class TelaWidgets:
    def __init__(self, master=None):
        self.master = master
        self.janela = tk.Toplevel(master) if master else tk.Tk()
        self.janela.title("Widgets")
        self.janela.geometry("600x600")
        self.janela.configure(bg="white")
        self.janela.resizable(False, False)
        caminho_icone = os.path.join(os.path.dirname(__file__), "../logo.ico")
        if os.path.exists(caminho_icone):
            self.janela.iconbitmap(caminho_icone)
        
        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_janela)

        titulo = tk.Label(self.janela, text="Widgets", font=("Arial", 16), bg="white")
        titulo.pack(pady=10)

        frame_menu = tk.Frame(self.janela, bg="white")
        frame_menu.pack(pady=10)

        tk.Button(frame_menu, text="Widgets Básicos", command=self.mostrar_basicos).pack(side="left", padx=10)
        tk.Button(frame_menu, text="Widgets de Entrada", command=self.mostrar_entrada).pack(side="left", padx=10)
        tk.Button(frame_menu, text="Widgets de Seleção", command=self.mostrar_selecao).pack(side="left", padx=10)
        tk.Button(frame_menu, text="Widgets de Interface", command=self.interface).pack(side="left", padx=10)

        self.frame_conteudo = tk.Frame(self.janela, bg="#f0f0f0", relief="sunken", bd=2)
        self.frame_conteudo.pack(expand=True, fill="both", padx=20, pady=20)

        self.mostrar_mensagem_inicial()

    def fechar_janela(self):
        if self.master:
            self.master.deiconify()  
        self.janela.destroy()

    def limpar_conteudo(self):
        for widget in self.frame_conteudo.winfo_children():
            widget.destroy()

    def mostrar_mensagem_inicial(self):
        self.limpar_conteudo()
        label = tk.Label(self.frame_conteudo, text="Escolha uma categoria de widgets acima.",
                         font=("Arial", 12), bg="#f0f0f0")
        label.pack(expand=True)

    def mostrar_basicos(self):
        self.limpar_conteudo()
        frame_botoes = tk.Frame(self.frame_conteudo, bg="#f0f0f0")
        frame_botoes.pack(anchor='n', pady=10)

        tk.Button(frame_botoes, text="Botão", command=self.abrir_tela_botao).pack(side="left", padx=5)
        tk.Button(frame_botoes, text="Frame", command=self.abrir_tela_frame).pack(side="left", padx=5)
        tk.Button(frame_botoes, text="Label", command=self.abrir_tela_label).pack(side="left", padx=5)

    def mostrar_entrada(self):
        self.limpar_conteudo()
        frame_botoes = tk.Frame(self.frame_conteudo, bg="#f0f0f0")
        frame_botoes.pack(anchor='n', pady=10)

        tk.Button(frame_botoes, text="Entrada", command=self.abrir_tela_entrada).pack(side="left", padx=5)
        tk.Button(frame_botoes, text="Combobox", command=self.abrir_tela_combo).pack(side="left", padx=5)
        tk.Button(frame_botoes, text="Spinbox", command=self.abrir_tela_spin).pack(side="left", padx=5)
        tk.Button(frame_botoes, text="Scale", command=self.abrir_tela_scale).pack(side="left", padx=5)
        tk.Button(frame_botoes, text="Text", command=self.abrir_tela_text).pack(side="left", padx=5)

    def mostrar_selecao(self):
        self.limpar_conteudo()
        frame_botoes = tk.Frame(self.frame_conteudo, bg="#f0f0f0")
        frame_botoes.pack(anchor='n', pady=10)

        tk.Button(frame_botoes, text="Checkbutton", command=self.abrir_tela_check).pack(side="left", padx=5)
        tk.Button(frame_botoes, text="Radiobutton", command=self.abrir_tela_radio).pack(side="left", padx=5)
        tk.Button(frame_botoes, text="Listbox", command=self.abrir_tela_list).pack(side="left", padx=5)

    def interface(self):
        self.limpar_conteudo()
        frame_botoes = tk.Frame(self.frame_conteudo, bg="#f0f0f0")
        frame_botoes.pack(anchor='n', pady=10)

        tk.Button(frame_botoes, text="Menu", command=self.abrir_tela_menu).pack(side="left", padx=5)
       

   
    def abrir_tela_botao(self):
        TelaBotoes(self.janela).iniciar()

    def abrir_tela_frame(self):
        TelaFrame(self.janela).iniciar()

    def abrir_tela_label(self):
        TelaLabel(self.janela).iniciar()

    def abrir_tela_entrada(self):
        TelaEntry(self.janela).iniciar()

    def abrir_tela_combo(self):
        TelaCombobox(self.janela).iniciar()

    def abrir_tela_spin(self):
        TelaSpinbox(self.janela).iniciar()

    def abrir_tela_scale(self):
        TelaScale(self.janela).iniciar()

    def abrir_tela_text(self):
        TelaText(self.janela).iniciar()

    def abrir_tela_check(self):
        TelaCheckbutton(self.janela).iniciar()
    
    def abrir_tela_menu(self):
        TelaMenu(self.janela).iniciar()

    def abrir_tela_radio(self):
        TelaRadiobutton(self.janela).iniciar()

    def abrir_tela_list(self):
        TelaListbox(self.janela).iniciar()

    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()