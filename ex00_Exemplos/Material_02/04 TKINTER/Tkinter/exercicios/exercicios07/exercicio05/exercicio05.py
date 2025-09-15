import tkinter as tk
from exercicios.widgets.labels import MeuLabel
from exercicios.widgets.botoes import MeuBotao
from exercicios.widgets.scale_horizontal import MeuScaleHorizontal

class Ex5_7(tk.Frame):
    def __init__(self, janela):
        super().__init__(janela)

        self.scale = MeuScaleHorizontal(self, de=0, ate=100)
        MeuBotao(self, "Mostrar Valor", comando=self.mostrar)

        self.resultado = MeuLabel(self, " ")

    def mostrar(self):
        valor = self.scale.pegar_valor()
        self.resultado.config(text=f"Valor selecionado: {valor}")