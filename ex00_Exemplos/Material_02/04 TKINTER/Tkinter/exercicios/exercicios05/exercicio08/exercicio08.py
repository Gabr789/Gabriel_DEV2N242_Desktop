import tkinter as tk
from exercicios.widgets.botoes import MeuBotao
from exercicios.widgets.labels import MeuLabel
from exercicios.widgets.check import MeuCheckGroup
from tkinter import font

class Ex8_5(tk.Frame):
    def __init__(self, janela):
        super().__init__(janela)

        self.checks = MeuCheckGroup(self, ["Queijo", "Bacon", "Tomate", "Cebola"])
        self.label = MeuLabel(self, "Monte seu lanche")

        MeuBotao(self, "Montar Lanche", comando=self.mostrar)

    def mostrar(self):
        ingredientes = self.checks.pegar_valores()
        self.label.config(text="Lanche: " + ", ".join(ingredientes) if ingredientes else "Nenhum ingrediente")