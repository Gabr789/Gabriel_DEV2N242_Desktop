import tkinter as tk

class Janela:
    def __init__(self, titulo="Aplicação", tamanho="400x400", master=None,**kwargs):
        if master is None:
            self.janela = tk.Tk(**kwargs)
        else:
            self.janela = tk.Toplevel(master,**kwargs)

        self.janela.title(titulo)
        self.janela.geometry(tamanho)
        self.janela.resizable(False, False)

    def __getattr__(self, attr):
        return getattr(self.janela, attr)