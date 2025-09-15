import tkinter as tk
from exercicios.widgets.entradas import MeuEntry
from exercicios.widgets.labels import MeuLabel
from exercicios.widgets.botoes import MeuBotao

class Ex1_7(tk.Frame):
    def __init__(self, janela):
        super().__init__(janela)

      
        frame_info = tk.Frame(self)
        frame_info.pack(pady=10)

        MeuLabel(frame_info, "Nome:")
        self.entry_nome = MeuEntry(frame_info)

        MeuLabel(frame_info, "Idade:")
        self.entry_idade = MeuEntry(frame_info)

       
        frame_botao = tk.Frame(self)
        frame_botao.pack(pady=10)

        MeuBotao(frame_botao, "Exibir", comando=self.exibir)

     
        self.resultado = MeuLabel(self, " ")

    def exibir(self):
        nome = self.entry_nome.pegar_texto()
        idade = self.entry_idade.pegar_texto()
        self.resultado.config(text=f"Nome: {nome}, Idade: {idade}")