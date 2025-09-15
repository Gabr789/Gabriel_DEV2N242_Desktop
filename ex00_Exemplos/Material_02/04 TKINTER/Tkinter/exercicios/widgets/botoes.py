import tkinter as tk

class MeuBotao(tk.Button):
    def __init__(self, tela_pertence, texto, comando=None,**kwargs):
        super().__init__(tela_pertence, text=texto, command=comando, font=("Arial", 10),**kwargs)
        self.pack(pady=5)