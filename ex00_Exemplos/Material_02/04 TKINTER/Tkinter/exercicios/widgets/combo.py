import tkinter as tk
from tkinter import ttk

class MeuCombo(ttk.Combobox):
    def __init__(self, tela_pertence, opcoes=(), fonte=("Arial", 12), **kwargs):
        super().__init__(tela_pertence, values=opcoes, **kwargs)
        
       
        font = tk.font.Font(family=fonte[0], size=fonte[1])
        self.option_add("*TCombobox*Listbox.Font", font)  
        self.configure(font=font)  

        self.pack(pady=5)

    def pegar_valor(self):
        return self.get()

    def limpar(self):
        self.set("")