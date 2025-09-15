import tkinter as tk
from exercicios.widgets.botoes import MeuBotao
from exercicios.widgets.labels import MeuLabel
from exercicios.widgets.check import MeuCheckGroup

class Ex4_5(tk.Frame):
    def __init__(self, janela):
        super().__init__(janela)

        self.checks = MeuCheckGroup(self, ["Python", "Java", "JavaScript"])
        self.label = MeuLabel(self, "Selecione as linguagens")

        MeuBotao(self, "Confirmar", comando=self.mostrar)

    def mostrar(self):
        linguagens = self.checks.pegar_valores()
        self.label.config(text="Conhece: " + ", ".join(linguagens) if linguagens else "Nenhuma linguagem")