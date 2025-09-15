
import tkinter as tk
from exercicios.widgets.botoes import MeuBotao
from exercicios.widgets.labels import MeuLabel
from exercicios.widgets.combo import MeuCombo

class Ex3_5(tk.Frame):
    def __init__(self, janela):
        super().__init__(janela)

        self.combo = MeuCombo(self, opcoes=["SC", "RS", "PR"])
        self.label = MeuLabel(self, "Selecione um estado")

        MeuBotao(self, "Mostrar", comando=self.mostrar)

    def mostrar(self):
        self.label.config(text=f"Estado: {self.combo.pegar_valor()}")




