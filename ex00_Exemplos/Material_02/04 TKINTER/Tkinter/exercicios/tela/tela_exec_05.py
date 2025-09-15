import tkinter as tk
from exercicios.exercicios05.exercicio01.exercicio01 import Ex1_5

from exercicios.widgets.janela import Janela
from exercicios.widgets.labels import MeuLabel
from exercicios.widgets.botoes import MeuBotao
from exercicios.widgets.frames import MeuFrame

class Tela05:
    def __init__(self, master=None):
        self.janela = Janela(titulo="Menu Principal", tamanho="600x600", master=master)

        MeuLabel(self.janela, "Escolha a lista de exercícios", fonte=("Arial", 14)).pack(pady=10)

       
        frame_botoes = tk.Frame(self.janela)
        frame_botoes.pack(pady=10)

        MeuBotao(frame_botoes, "Lista 05: Exercício 01", comando=lambda: self.abrir_exercicio(Ex1_5)).pack(side="left", padx=5)
      
       
        self.frame_conteudo = MeuFrame(self.janela)
        self.frame_conteudo.pack(expand=True, fill="both", pady=20)

    def abrir_exercicio(self, exercicio_cls):
        for widget in self.frame_conteudo.winfo_children():
            widget.destroy()
        exercicio = exercicio_cls(self.frame_conteudo)
        exercicio.pack(expand=True, fill="both")

    def iniciar(self):
        self.janela.mainloop()