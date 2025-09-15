import tkinter as tk

class MeuScaleHorizontal(tk.Scale):
    def __init__(self, tela_pertence, de=0, ate=100, fonte=("Arial", 11), **kwargs):
        super().__init__(tela_pertence, from_=de, to=ate,
                         orient=tk.HORIZONTAL, font=fonte, **kwargs)
        self.pack(pady=5)

    def pegar_valor(self):
        return self.get()

    def definir_valor(self, valor):
        self.set(valor)

    def limpar(self):
        self.set(0)