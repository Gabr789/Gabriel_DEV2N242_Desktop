import tkinter as tk
from exercicios.widgets.check import MeuCheckGroup
from exercicios.widgets.labels import MeuLabel
from exercicios.widgets.botoes import MeuBotao

class Ex7_7(tk.Frame):
    def __init__(self, janela):
        super().__init__(janela)

        self.checks = MeuCheckGroup(self, ["Python", "Java", "JavaScript"])
        MeuBotao(self, "Confirmar", comando=self.mostrar)

        self.resultado = MeuLabel(self, " ")

    def mostrar(self):
        valores = self.checks.pegar_valores()
        self.resultado.config(text=", ".join(valores) if valores else "Nenhuma opção marcada")