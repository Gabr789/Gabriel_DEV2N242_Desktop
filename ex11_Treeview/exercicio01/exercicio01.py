"""
Exercício 1 
Crie uma interface com um Treeview simples que liste alguns itens. 
Adicione um campo de texto Entry e um botão para inserir novos itens na lista. 
Inclua também um botão para excluir o item selecionado.
"""

import tkinter as tk
from tkinter import messagebox
from estilo01 import Estilos01


class Ex1101:
    def __init__(self, master=None):
        self.janela = tk.Toplevel(master) if master else tk.Tk()
        self.janela.title("Exercício 1")
        self.janela.geometry("600x700")
        self.janela.config(**Estilos01.estiloJanela())


    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()