import tkinter as tk
from exercicios.widgets.entradas import MeuEntry
from exercicios.widgets.botoes import MeuBotao
from exercicios.widgets.labels import MeuLabel

class Ex1(tk.Frame):
    def __init__(self, janela):
        super().__init__(janela)

        self.entry = MeuEntry(self,bg="#f0f0f0",fg="black",relief="solid", bd=2)      
        self.label = MeuLabel(self, " ")

        MeuBotao(self, "Mostrar", comando=self.mostrar)

    def mostrar(self):
        self.label.config(text=self.entry.pegar_texto())