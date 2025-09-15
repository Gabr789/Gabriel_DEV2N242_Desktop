import tkinter as tk
import os
from tkinter import messagebox
class Lista1:
    def __init__(self, master=None):
        self.janela = tk.Toplevel(master)
        self.janela.title("Nova Janela")
        self.janela.geometry("600x600")
        self.janela.configure(bg="green")
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../../logo.ico")
        if os.path.exists(caminho_icone):
            self.janela.iconbitmap(caminho_icone)

        label = tk.Label(self.janela, text="Exercício 2 - Nova Janela", font=("Arial", 16))
        label.pack(pady=20)

        botao = tk.Button(self.janela, text="Clique aqui", command=lambda: messagebox.showinfo("Erro","Botão clicado",) )
        botao.pack(pady=10)

    def iniciar(self):
        self.janela.mainloop()