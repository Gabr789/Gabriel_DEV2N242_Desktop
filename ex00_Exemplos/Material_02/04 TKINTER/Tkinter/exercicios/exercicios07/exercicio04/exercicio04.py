import tkinter as tk
from exercicios.widgets.text import MeuText
from exercicios.widgets.labels import MeuLabel
from exercicios.widgets.botoes import MeuBotao

class Ex4_7(tk.Frame):
    def __init__(self, janela):
        super().__init__(janela)

        self.texto = MeuText(self, altura=5, largura=30)
        MeuBotao(self, "Mostrar", comando=self.mostrar)
        self.resultado = MeuLabel(self, " ")

    def mostrar(self):
        conteudo = self.texto.pegar_texto()
        self.resultado.config(text=conteudo)
