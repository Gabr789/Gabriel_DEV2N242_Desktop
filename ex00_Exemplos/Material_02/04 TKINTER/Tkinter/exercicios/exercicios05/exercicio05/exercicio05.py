import tkinter as tk
from exercicios.widgets.botoes import MeuBotao
from exercicios.widgets.labels import MeuLabel
from exercicios.widgets.check import MeuCheckGroup
from exercicios.widgets.radio import MeuRadioGroup

class Ex5_5(tk.Frame):
    def __init__(self, janela):
        super().__init__(janela)

        self.radios = MeuRadioGroup(self, [("Masculino", "M"), ("Feminino", "F"), ("Outro", "Outro")])
        self.label = MeuLabel(self, "Selecione o gênero")

        MeuBotao(self, "Confirmar", comando=self.mostrar)

    def mostrar(self):
        self.label.config(text=f"Gênero: {self.radios.pegar_valor()}")