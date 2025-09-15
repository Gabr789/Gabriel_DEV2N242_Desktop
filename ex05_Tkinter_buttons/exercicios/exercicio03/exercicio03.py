import tkinter as tk
from tkinter import ttk

# Exercício 3 
# Monte uma interface com uma Combobox contendo os seguintes estados: SC, RS, 
# PR. Ao clicar em um botão, mostre o estado selecionado no Label.


class Ex03:
    def __init__(self, janelaPrincipal=None):
        self.janela = tk.Toplevel(janelaPrincipal) if janelaPrincipal else tk.Tk()
        self.janela.title("Exercício 3")
        self.janela.geometry("600x400")

        def confirmar():
            escolha = self.combo.get()

            if escolha:
                preferencias.config(text=f"Estado escolhido: {escolha}")
            else:
                preferencias.config(text="Nenhum estado escolhido")

        local_escolhas = tk.Frame(self.janela)
        local_escolhas.pack(pady=20)

        tk.Label(local_escolhas, text="Escolha um estado:").pack(anchor="w")

        estados = ["SC", "RS", "PR"]

        self.combo = ttk.Combobox(local_escolhas, values=estados, state="readonly")
        self.combo.pack(pady=5)

        botao = tk.Button(self.janela, text="Confirmar escolha", command=confirmar)
        botao.pack(pady=10)

        preferencias = tk.Label(self.janela, text="")
        preferencias.pack(pady=10)


    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()

exe = Ex03()
exe.iniciar()