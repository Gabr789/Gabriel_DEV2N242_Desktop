import tkinter as tk
from exercicios.widgets.botoes import MeuBotao
from exercicios.widgets.entradas import MeuEntry
from exercicios.widgets.labels import MeuLabel

class Ex10(tk.Frame):
    def __init__(self, janela):
        super().__init__(janela)
        self.entry1 = MeuEntry(self)
        self.entry2 = MeuEntry(self)
        self.label = MeuLabel(self, " ")
        MeuBotao(self, "Concatenar", comando=self.concatenar)

    def concatenar(self):
        texto1 = self.entry1.pegar_texto()
        texto2 = self.entry2.pegar_texto()
        self.label.config(text=texto1 + texto2)