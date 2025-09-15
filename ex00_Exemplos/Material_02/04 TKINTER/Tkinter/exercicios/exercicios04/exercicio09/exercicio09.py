import tkinter as tk
from exercicios.widgets.botoes import MeuBotao
from exercicios.widgets.entradas import MeuEntry
from exercicios.widgets.labels import MeuLabel

class Ex9(tk.Frame):
    def __init__(self, janela):
        super().__init__(janela)
        self.entry = MeuEntry(self)
        self.label = MeuLabel(self, " ")
        MeuBotao(self, "Dobrar", comando=self.dobrar)

    def dobrar(self):
        try:
            numero = float(self.entry.pegar_texto())
            self.label.config(text=f"Dobro: {numero * 2}")
        except ValueError:
            self.label.config(text="Digite um número válido!")