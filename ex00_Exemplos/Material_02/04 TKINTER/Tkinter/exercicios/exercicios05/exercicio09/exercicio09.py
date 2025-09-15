import tkinter as tk
from exercicios.widgets.botoes import MeuBotao
from exercicios.widgets.labels import MeuLabel
from exercicios.widgets.combo import MeuCombo
from exercicios.widgets.radio import MeuRadioGroup
from tkinter import font

class Ex9_5(tk.Frame):
    def __init__(self, janela):
        super().__init__(janela)

        self.combo = MeuCombo(self, opcoes=["Pequena", "Média", "Grande"])
        self.radios = MeuRadioGroup(self, [("Fina", "Fina"), ("Tradicional", "Tradicional")])
        self.label = MeuLabel(self, "Monte sua pizza")

        MeuBotao(self, "Montar Pedido", comando=self.mostrar)

    def mostrar(self):
        tamanho = self.combo.pegar_valor()
        massa = self.radios.pegar_valor()
        self.label.config(text=f"Pizza {tamanho} com massa {massa}" if tamanho and massa else "Escolha tudo primeiro!")