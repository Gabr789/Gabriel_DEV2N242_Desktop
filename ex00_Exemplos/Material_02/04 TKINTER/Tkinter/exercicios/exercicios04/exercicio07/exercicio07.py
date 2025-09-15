import tkinter as tk
from exercicios.widgets.botoes import MeuBotao
from exercicios.widgets.entradas import MeuEntry
from exercicios.widgets.labels import MeuLabel

class Ex7(tk.Frame):
    def __init__(self, janela):
        super().__init__(janela)
        self.entry = MeuEntry(self)
        self.label = MeuLabel(self, " ")

        MeuBotao(self, "Mostrar", comando=self.mostrar)
        MeuBotao(self, "Limpar", comando=self.limpar)

    def mostrar(self):
        self.label.config(text=self.entry.pegar_texto())

    def limpar(self):
        self.entry.limpar()
        self.label.config(text=" ")