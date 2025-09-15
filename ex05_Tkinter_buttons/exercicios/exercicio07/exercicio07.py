import tkinter as tk

# Exercício 7 
# Crie uma interface com Radiobuttons para forma de pagamento: Cartão, Dinheiro, 
# PixUm botão Selecionar Ao clicar, mostre a forma de pagamento escolhida no Label.


class Ex07:
    def __init__(self, janelaPrincipal=None):
        self.janela = tk.Toplevel(janelaPrincipal) if janelaPrincipal else tk.Tk()
        self.janela.title("Exercício 7")
        self.janela.geometry("600x400")

        def confirmar():
            escolha = forma_pagamento.get()

            if escolha == "__nada__":
                preferencias.config(text="Nenhuma opção escolhida")
            else:
                preferencias.config(text=f"Forma de pagamento escolhida: {escolha}")

        local_escolhas = tk.Frame(self.janela)
        local_escolhas.pack(pady=20)

        tk.Label(local_escolhas, text="Escolha uma forma de pagamento:").pack(anchor="w")

        forma_pagamento = tk.StringVar(value="__nada__")

        tk.Radiobutton(local_escolhas, text="Cartão", variable=forma_pagamento, value="Cartão").pack(anchor="w")
        tk.Radiobutton(local_escolhas, text="Dinheiro", variable=forma_pagamento, value="Dinheiro").pack(anchor="w")
        tk.Radiobutton(local_escolhas, text="Pix", variable=forma_pagamento, value="Pix").pack(anchor="w")

        botao = tk.Button(self.janela, text="Confirmar escolha", command=confirmar)
        botao.pack(pady=10)

        preferencias = tk.Label(self.janela, text="")
        preferencias.pack(pady=10)


    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()

exe = Ex07()
exe.iniciar()