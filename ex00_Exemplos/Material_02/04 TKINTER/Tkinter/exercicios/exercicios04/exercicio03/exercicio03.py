import tkinter as tk
from exercicios.widgets.botoes import MeuBotao
from exercicios.widgets.entradas import MeuEntry
from exercicios.widgets.labels import MeuLabel

class Ex3(tk.Frame):
    def __init__(self, janela):
        super().__init__(janela)
        self.entry = MeuEntry(self)
        self.label = MeuLabel(self, " ")

        MeuBotao(self, "número de caracteres", comando=self.numerocaracteres)

    def numerocaracteres(self):
        self.label.config(text=len(self.entry.pegar_texto()))
