


import tkinter as tk
from exercicios.exercicios04.exercicio01.exercicio01 import Ex1
from exercicios.exercicios04.exercicio02.exercicio02 import Ex2
from exercicios.exercicios04.exercicio03.exercicio03 import Ex3
from exercicios.widgets.janela import Janela
from exercicios.widgets.labels import MeuLabel
from exercicios.widgets.botoes import MeuBotao
from exercicios.widgets.frames import MeuFrame

class TelaWidgets:
    def __init__(self, master=None):
        self.janela = Janela(titulo="Menu Principal", tamanho="600x600", master=master)

        MeuLabel(self.janela, "Escolha a lista de exercícios", fonte=("Arial", 14)).pack(pady=10)

        
        frame_botoes = tk.Frame(self.janela)
        frame_botoes.pack(pady=10)

        MeuBotao(frame_botoes, "Lista 04: Exercício 01", comando=lambda: self.abrir_exercicio(Ex1)).pack(side="left", padx=5)
        MeuBotao(frame_botoes, "Lista 04: Exercício 02", comando=lambda: self.abrir_exercicio(Ex2)).pack(side="left", padx=5)
        MeuBotao(frame_botoes, "Lista 04: Exercício 03", comando=lambda: self.abrir_exercicio(Ex3)).pack(side="left", padx=5)
       
        self.frame_conteudo = MeuFrame(self.janela)
        self.frame_conteudo.pack(expand=True, fill="both", pady=20)

    def abrir_exercicio(self, exercicio_cls):
        for widget in self.frame_conteudo.winfo_children():
            widget.destroy()
        exercicio = exercicio_cls(self.frame_conteudo)
        exercicio.pack(expand=True, fill="both")

    def iniciar(self):
        try:
            self.janela.mainloop()
        except KeyboardInterrupt:
            pass