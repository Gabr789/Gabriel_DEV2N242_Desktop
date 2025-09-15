import tkinter as tk

class MeuLabel(tk.Label):
    def __init__(self, tela_pertence, texto="", fonte=("Arial", 12),**kwargs):
        super().__init__(tela_pertence, text=texto, font=fonte,**kwargs)
        self.pack(pady=5)