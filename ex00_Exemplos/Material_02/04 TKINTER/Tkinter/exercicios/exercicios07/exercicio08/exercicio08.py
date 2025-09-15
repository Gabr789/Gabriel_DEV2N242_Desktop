import tkinter as tk
from exercicios.widgets.radio import MeuRadioGroup
from exercicios.widgets.labels import MeuLabel
from exercicios.widgets.botoes import MeuBotao

class Ex8_7(tk.Frame):
    def __init__(self, janela):
        super().__init__(janela)

        self.radios = MeuRadioGroup(self, [("Masculino", "M"), ("Feminino", "F"), ("Outro", "O")])
        MeuBotao(self, "Selecionar", comando=self.selecionar)

        self.resultado = MeuLabel(self, " ")

    def selecionar(self):
        valor = self.radios.pegar_valor()
        self.resultado.config(text=f"Gênero: {valor}" if valor else "Nenhum selecionado")