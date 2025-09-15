import tkinter as tk

class MeuText(tk.Entry):
    def __init__(self, tela_pertence, fonte=("Arial", 12), texto_inicial="", **kwargs):
        super().__init__(tela_pertence, font=fonte, **kwargs)
        
        if texto_inicial:
            self.insert(0, texto_inicial)  
        
        self.pack(pady=5)

    def pegar_valor(self):
        return self.get()

    def limpar(self):
        self.delete(0, tk.END)