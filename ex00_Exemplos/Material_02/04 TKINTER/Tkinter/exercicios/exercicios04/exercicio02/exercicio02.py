import tkinter as tk
from exercicios.widgets.botoes import MeuBotao
from exercicios.widgets.entradas import MeuEntry
from exercicios.widgets.labels import MeuLabel

class Ex2(tk.Frame):
    def __init__(self, janela):
        super().__init__(janela)
        self.entry = MeuEntry(self)
        self.label = MeuLabel(self, "Digite algo")

        MeuBotao(self, "mostrar maiúsculas", comando=self.mostrar_maiusculo)

    def mostrar_maiusculo(self):
        self.label.config(text=self.entry.pegar_texto().upper())
