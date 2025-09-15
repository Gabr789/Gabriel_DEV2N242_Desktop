import tkinter as tk
from exercicios.widgets.botoes import MeuBotao
from exercicios.widgets.entradas import MeuEntry
from exercicios.widgets.labels import MeuLabel

class Ex4(tk.Frame):
    def __init__(self, janela):
        super().__init__(janela)

     
        self.entry1 = MeuEntry(self)
        self.entry2 = MeuEntry(self)

       
        self.label = MeuLabel(self, " ")

        
        MeuBotao(self, "Somar", comando=self.somar)

    def somar(self):
        try:
            n1 = float(self.entry1.pegar_texto())
            n2 = float(self.entry2.pegar_texto())
            resultado = n1 + n2
            self.label.config(text=f"Resultado: {resultado}")
        except ValueError:
            self.label.config(text="Digite apenas números!")