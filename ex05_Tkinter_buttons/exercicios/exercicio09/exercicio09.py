import tkinter as tk
from tkinter import ttk

# Exercício 9 
# Use uma Combobox para selecionar o tamanho da pizza: Pequena, Média, Grande. 
# Use Radiobuttons para tipo de massa: Fina, Tradicional 
# Ao clicar em Montar Pedido, exiba no Label algo como 
# Pizza Média com massa Fina


class Ex09:
    def __init__(self, janelaPrincipal=None):
        self.janela = tk.Toplevel(janelaPrincipal) if janelaPrincipal else tk.Tk()
        self.janela.title("Exercício 9")
        self.janela.geometry("600x400")

        def confirmar():
            escolha_tamanho = self.combo.get()
            escolha_tipo = tipo_massa.get()

            if escolha_tamanho and escolha_tipo:
                preferencias.config(text=f"Pizza {escolha_tamanho} com massa {escolha_tipo}")
            else:
                preferencias.config(text="Escolha o tamanho e o tipo de massa da pizza")


        local_escolhas = tk.Frame(self.janela)
        local_escolhas.pack(pady=20)


        tk.Label(local_escolhas, text="Escolha o tamanho da pizza:").pack(anchor="w")

        tamanhos_pizza = ["Pequena", "Média", "Grande"]

        self.combo = ttk.Combobox(local_escolhas, values=tamanhos_pizza, state="readonly")
        self.combo.pack(pady=10, anchor="w")



        tk.Label(local_escolhas, text="Escolha o tipo de massa:").pack(pady=10, anchor="w")

        tipo_massa = tk.StringVar(value="__nada__")

        tk.Radiobutton(local_escolhas, text="Fina", variable=tipo_massa, value="Fina").pack(anchor="w")
        tk.Radiobutton(local_escolhas, text="Tradicional", variable=tipo_massa, value="Tradicional").pack(anchor="w")



        botao = tk.Button(self.janela, text="Montar pedido", command=confirmar)
        botao.pack(pady=10)

        preferencias = tk.Label(self.janela, text="")
        preferencias.pack(pady=10)


    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()

exe = Ex09()
exe.iniciar()