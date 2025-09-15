import tkinter as tk
from exercicios.widgets.labels import MeuLabel
from exercicios.widgets.botoes import MeuBotao
from exercicios.widgets.scale_vertical import MeuScaleVertical

class Ex6_7(tk.Frame):
    def __init__(self, janela):
        super().__init__(janela)

        self.scale = MeuScaleVertical(self, de=0, ate=50)
        MeuBotao(self, "Exibir", comando=self.exibir)

        self.resultado = MeuLabel(self, " ")

    def exibir(self):
        valor = self.scale.pegar_valor()
        self.resultado.config(text=f"Altura escolhida: {valor}")
