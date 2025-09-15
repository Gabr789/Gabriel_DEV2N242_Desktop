import tkinter as tk
from tkinter import messagebox
from exercicios.widgets.janela import Janela
from exercicios.widgets.labels import MeuLabel
from exercicios.widgets.botoes import MeuBotao
from exercicios.tela.tela import TelaWidgets
from exercicios.tela.tela_exec_05 import Tela05


class MenuListas:
    def __init__(self, master=None):
        self.master = master  
        self.janela = Janela(titulo="Menu Principal", tamanho="400x400", master=master)

        MeuLabel(self.janela, "Escolha a lista de exercícios", fonte=("Arial", 14))
        MeuBotao(self.janela, "Lista 04", comando=self.abrir_lista_widgets)
        MeuBotao(self.janela, "Lista 05", comando=self.abrir_lista_interacoes)
        MeuBotao(self.janela, "Lista 07", comando=self.abrir_lista_layouts)

        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_janela)
        

    def fechar_janela(self):
        self.janela.withdraw()  
        if self.master and self.master.winfo_exists():
            self.master.deiconify()

    def abrir_lista_widgets(self):  
        self.janela.withdraw()
        tela = TelaWidgets(master=self.janela)  
        self.janela.wait_window(tela.janela)   
        self.janela.deiconify()                

    def abrir_lista_interacoes(self):
        self.janela.withdraw()
        tela = Tela05(master=self.janela)
        self.janela.wait_window(tela.janela)
        self.janela.deiconify()

    def abrir_lista_layouts(self):
        messagebox.showinfo("Aguarde", "Lista 06 ainda não implementada!")

    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()