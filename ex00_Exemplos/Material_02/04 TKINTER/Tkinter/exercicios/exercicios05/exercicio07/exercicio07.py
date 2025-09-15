import tkinter as tk
from exercicios.widgets.botoes import MeuBotao
from exercicios.widgets.labels import MeuLabel
from exercicios.widgets.radio import MeuRadioGroup
from tkinter import font
class Ex7_5(tk.Frame):
    def __init__(self, janela):
        super().__init__(janela)

        self.radios = MeuRadioGroup(self, [("Cartão", "Cartão"), ("Dinheiro", "Dinheiro"), ("Pix", "Pix")])
        self.label = MeuLabel(self, "Selecione a forma de pagamento")

        MeuBotao(self, "Selecionar", comando=self.mostrar)

    def mostrar(self):
        self.label.config(text=f"Pagamento: {self.radios.pegar_valor()}")