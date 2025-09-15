import tkinter as tk
from exercicios.widgets.botoes import MeuBotao
from exercicios.widgets.labels import MeuLabel
from exercicios.widgets.combo import MeuCombo
from exercicios.widgets.radio import MeuRadioGroup
from exercicios.widgets.check import MeuCheckGroup
from tkinter import font

class Ex10_5(tk.Frame):
    def __init__(self, janela):
        super().__init__(janela)

        self.combo = MeuCombo(self, opcoes=["ADS", "Jogos", "Redes"])
        self.radios = MeuRadioGroup(self, [("Manhã", "Manhã"), ("Tarde", "Tarde"), ("Noite", "Noite")])
        self.checks = MeuCheckGroup(self, ["Participa do Discord", "Gosta de programação"])

        MeuBotao(self, "Enviar", comando=self.mostrar)

    def mostrar(self):
        curso = self.combo.pegar_valor()
        turno = self.radios.pegar_valor()
        opcoes = ", ".join(self.checks.pegar_valores())

        nova = tk.Toplevel(self)
        MeuLabel(nova, f"Curso: {curso}")
        MeuLabel(nova, f"Turno: {turno}")
        MeuLabel(nova, f"Opções: {opcoes if opcoes else 'Nenhuma'}")