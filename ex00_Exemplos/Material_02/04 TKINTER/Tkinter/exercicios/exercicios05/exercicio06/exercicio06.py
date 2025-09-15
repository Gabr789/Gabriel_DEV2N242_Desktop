import tkinter as tk
from exercicios.widgets.botoes import MeuBotao
from exercicios.widgets.labels import MeuLabel
from exercicios.widgets.combo import MeuCombo
from tkinter import font
class Ex6_5(tk.Frame):
    def __init__(self, janela):
        super().__init__(janela)

        self.combo = MeuCombo(self, opcoes=["ADS", "Jogos", "Redes"])
        self.label = MeuLabel(self, "Selecione um curso")

        MeuBotao(self, "Confirmar", comando=self.mostrar)

    def mostrar(self):
        self.label.config(text=f"Curso: {self.combo.pegar_valor()}")