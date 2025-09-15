import tkinter as tk
from exercicios.widgets.botoes import MeuBotao
from exercicios.widgets.entradas import MeuEntry
from exercicios.widgets.labels import MeuLabel

class Ex8(tk.Frame):
    def __init__(self, janela):
        super().__init__(janela)
        self.entry = MeuEntry(self)
        self.label = MeuLabel(self, " ")
        MeuBotao(self, "Inverter", comando=self.inverter)

    def inverter(self):
        texto = self.entry.pegar_texto()
        self.label.config(text=texto[::-1])