import tkinter as tk

class MeuEntry(tk.Entry):
    def __init__(self, tela_pertence,**kwargs):
        super().__init__(tela_pertence, font=("Arial", 12),**kwargs)
        self.pack(pady=5)

    def pegar_texto(self):
        return self.get()

    def limpar(self):
        self.delete(0, tk.END)

    def apenas_numeros(self):
        vcmd = (self.register(self._validar_numero), "%S")
        self.config(validate="key", validatecommand=vcmd)

    def apenas_letras(self):
        vcmd = (self.register(self._validar_letra), "%S")
        self.config(validate="key", validatecommand=vcmd)

    def _validar_numero(self, char):
        return char.isdigit() 

    def _validar_letra(self, char):
        return char.isalpha()  