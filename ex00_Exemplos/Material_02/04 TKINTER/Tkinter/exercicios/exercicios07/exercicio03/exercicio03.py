import tkinter as tk
from exercicios.widgets.labels import MeuLabel
from exercicios.widgets.botoes import MeuBotao

class Ex3_7(tk.Frame):
    def __init__(self, janela):
        super().__init__(janela)

        self.label = MeuLabel(self, "Clique no botão para mudar a mensagem.")

        MeuBotao(self, "Mudar Texto", comando=self.mudar_texto)

    def mudar_texto(self):
        self.label.config(text="Texto atualizado com sucesso!")
