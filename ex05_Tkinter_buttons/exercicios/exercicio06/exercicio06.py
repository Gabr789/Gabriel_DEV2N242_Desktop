import tkinter as tk
from tkinter import ttk

# Exercício 6 
# Monte uma Combobox com os cursos: ADS, Jogos, Redes. 
# Permita que o usuário selecione um curso e, ao clicar no botão, exiba o texto curso 
# selecionado.


class Ex0506:
    def __init__(self, janelaPrincipal=None):
        self.janela = tk.Toplevel(janelaPrincipal) if janelaPrincipal else tk.Tk()
        self.janela.title("Exercício 6")
        self.janela.geometry("600x400")

        def confirmar():
            escolha = self.combo.get()

            if escolha:
                preferencias.config(text=f"Curso escolhido: {escolha}")
            else:
                preferencias.config(text="Nenhum curso escolhido")

        local_escolhas = tk.Frame(self.janela)
        local_escolhas.pack(pady=20)

        tk.Label(local_escolhas, text="Escolha um curso:").pack(anchor="w")

        cursos = ["ADS", "Jogos", "Redes"]

        self.combo = ttk.Combobox(local_escolhas, values=cursos, state="readonly")
        self.combo.pack(pady=5)

        botao = tk.Button(self.janela, text="Confirmar escolha", command=confirmar)
        botao.pack(pady=10)

        preferencias = tk.Label(self.janela, text="")
        preferencias.pack(pady=10)


    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()