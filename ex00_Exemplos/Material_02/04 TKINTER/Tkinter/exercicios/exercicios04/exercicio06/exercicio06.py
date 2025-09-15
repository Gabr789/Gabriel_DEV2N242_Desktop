import tkinter as tk
from exercicios.widgets.botoes import MeuBotao
from exercicios.widgets.entradas import MeuEntry
from exercicios.widgets.labels import MeuLabel

class Ex6(tk.Frame):
    def __init__(self, janela):
        super().__init__(janela)
        self.entry = MeuEntry(self)
        self.label = MeuLabel(self, " ")
        MeuBotao(self, "Verificar", comando=self.verificar)

    def verificar(self):
        if self.entry.pegar_texto().strip() == "":
            self.label.config(text="Campo vazio!")
        else:
            self.label.config(text="Preenchido")