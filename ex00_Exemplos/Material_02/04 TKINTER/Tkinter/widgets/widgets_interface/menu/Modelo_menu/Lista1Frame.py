import tkinter as tk
from tkinter import messagebox
class TelaLista1Frame(tk.Frame):
    def __init__(self, master):
        super().__init__(master) 

        
        label = tk.Label(self, text="Exercício 1 - Lista 1", font=("Arial", 16))
        label.pack(pady=20)

        botao = tk.Button(self, text="Clique aqui", command=lambda: messagebox.showinfo("Erro","Botão clicado",) )
        botao.pack(pady=10)