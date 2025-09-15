import tkinter as tk
from exercicios.widgets.botoes import MeuBotao
from exercicios.widgets.labels import MeuLabel
from exercicios.widgets.radio import MeuRadioGroup

class Ex2_5(tk.Frame):
    def __init__(self, janela):
        super().__init__(janela)

        self.radios = MeuRadioGroup(self, [
            ("Manhã", "Manhã"),
            ("Tarde", "Tarde"),
            ("Noite", "Noite")
        ], tipo="string")

        self.label = MeuLabel(self, " ")
        MeuBotao(self, "Confirmar", comando=self.mostrar)

    def mostrar(self):
        self.label.config(text=f"Turno escolhido: {self.radios.pegar_valor()}")