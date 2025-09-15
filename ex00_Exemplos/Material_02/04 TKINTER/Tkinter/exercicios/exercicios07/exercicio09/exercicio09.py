import tkinter as tk
from exercicios.widgets.combo import MeuCombo
from exercicios.widgets.labels import MeuLabel
from exercicios.widgets.botoes import MeuBotao

class Ex9_7(tk.Frame):
    def __init__(self, janela):
        super().__init__(janela)

        self.combo = MeuCombo(self, ["ADS", "Jogos", "Redes"])
        MeuBotao(self, "Selecionar Curso", comando=self.selecionar)

        self.resultado = MeuLabel(self, " ")

    def selecionar(self):
        curso = self.combo.pegar_valor()
        self.resultado.config(text=f"Curso selecionado: {curso}" if curso else "Nenhum curso escolhido")
