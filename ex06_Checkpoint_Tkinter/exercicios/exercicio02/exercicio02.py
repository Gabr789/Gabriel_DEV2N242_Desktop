import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from .estilo02 import Estilos02


# Desafio 2 
# Crie uma interface com uma Combobox para o tamanho da pizza: Pequena, Média, 
# Grande, Radiobuttons para o tipo de massa: Fina, Tradicional, e Checkbuttons para 
# ingredientes: Queijo, Calabresa, Tomate, Cebola. 
# Adicione também Radiobuttons para a forma de pagamento: Dinheiro, Cartão, Pix. 
# Ao clicar no botão Finalizar Pedido, exiba no Label o pedido completo com as 
# escolhas feitas. 



class Ex0602:
    def __init__(self, master=None):
        self.janela = tk.Toplevel(master) if master else tk.Tk()
        self.janela.title("Exercício 2")
        self.janela.geometry("600x800")
        self.janela.config(**Estilos02.estiloJanela())


        def verificarTamanho(tamanho):
            return bool(tamanho)
        
        def verificarTipoMassa(tipo_massa):
            return tipo_massa != "__nada__"

        def verificarFormaPagamento(forma_pagamento):
            return forma_pagamento != "__nada__"


        def finalizarPedido():
            tamanho = self.tamanho.get().lower()
            tipo_massa = self.tipo_massa.get()
            forma_pagamento = self.forma_pagamento.get()
            ingredientes = []

            if self.queijo.get():
                ingredientes.append("queijo")
            if self.calabresa.get():
                ingredientes.append("calabresa")
            if self.tomate.get():
                ingredientes.append("tomate")
            if self.cebola.get():
                ingredientes.append("cebola")


            if not verificarTamanho(tamanho):
                messagebox.showerror("Erro", "Escolha um tamanho para a pizza")

            elif not verificarTipoMassa(tipo_massa):
                messagebox.showerror("Erro", "Escolha um tipo de massa para a pizza")

            elif not verificarFormaPagamento(forma_pagamento):
                messagebox.showerror("Erro", "Escoha uma forma de pagamento")

            else:
                mensagem = (
                    "Pedido realizado com sucesso!\n"
                    f"Você pediu uma pizza {tamanho}, "
                    f"com massa {tipo_massa}.\n"
                    )
                if ingredientes:
                    mensagem += "Ingredientes: " + ", ".join(ingredientes) + ".\n"
                mensagem += f"Você pagará com {forma_pagamento}."

                messagebox.showinfo("Perfil Criado", mensagem)




        """Frame"""

        frame_principal = tk.Frame(self.janela, **Estilos02.estiloFrame())
        frame_principal.pack(pady=50)




        """Tamanho"""

        tk.Label(
            frame_principal,
            **Estilos02.estiloLabel(),
            text="Escolha o tamanho da pizza:"
            ).pack(pady=(20, 10), padx=40, anchor="w")


        tamanhos = ["Pequena", "Média", "Grande"]

        self.tamanho = ttk.Combobox(
            frame_principal,
            **Estilos02.estiloCombo(),
            values=tamanhos,
            state="readonly"
            )
        self.tamanho.pack(padx=40, anchor="w")




        """Tipo de massa"""

        tk.Label(
            frame_principal,
            **Estilos02.estiloLabel(),
            text="Escolha o tipo de massa da pizza:"
        ).pack(pady=(20, 10), padx=40, anchor="w")


        self.tipo_massa = tk.StringVar(value="__nada__")

        tk.Radiobutton(
            frame_principal,
            **Estilos02.estiloRadio(),
            text="Fina",
            variable=self.tipo_massa,
            value="fina"
        ).pack(padx=40, anchor="w")

        tk.Radiobutton(
            frame_principal,
            **Estilos02.estiloRadio(),
            text="Tradicional",
            variable=self.tipo_massa,
            value="tradicional"
        ).pack(padx=40, anchor="w")




        """Ingredientes"""

        tk.Label(
            frame_principal,
            **Estilos02.estiloLabel(),
            text="Escolha os ingredientes:"
        ).pack(pady=(30, 10), padx=40, anchor="w")


        self.queijo = tk.BooleanVar()
        self.calabresa = tk.BooleanVar()
        self.tomate = tk.BooleanVar()
        self.cebola = tk.BooleanVar()

        tk.Checkbutton(
            frame_principal,
            **Estilos02.estiloCheck(),
            text="Queijo",
            variable=self.queijo
        ).pack(padx=40, anchor="w")
        
        tk.Checkbutton(
            frame_principal,
            **Estilos02.estiloCheck(),
            text="Calabresa",
            variable=self.calabresa
        ).pack(padx=40, anchor="w")

        tk.Checkbutton(
            frame_principal,
            **Estilos02.estiloCheck(),
            text="Tomate",
            variable=self.tomate
        ).pack(padx=40, anchor="w")

        tk.Checkbutton(
            frame_principal,
            **Estilos02.estiloCheck(),
            text="Cebola",
            variable=self.cebola
        ).pack(padx=40, anchor="w")




        """Forma de Pagamento"""

        tk.Label(
            frame_principal,
            **Estilos02.estiloLabel(),
            text="Escolha a forma de pagamento:"
        ).pack(pady=(30, 10), padx=40, anchor="w")


        self.forma_pagamento = tk.StringVar(value="__nada__")

        tk.Radiobutton(
            frame_principal,
            **Estilos02.estiloRadio(),
            text="Dinheiro",
            variable=self.forma_pagamento,
            value="dinheiro"
        ).pack(padx=40, anchor="w")

        tk.Radiobutton(
            frame_principal,
            **Estilos02.estiloRadio(),
            text="Cartão",
            variable=self.forma_pagamento,
            value="cartão"
        ).pack(padx=40, anchor="w")

        tk.Radiobutton(
            frame_principal,
            **Estilos02.estiloRadio(),
            text="Pix",
            variable=self.forma_pagamento,
            value="pix"
        ).pack(padx=40, anchor="w")




        """Botão Finalizar Pedido"""

        tk.Button(
            frame_principal,
            **Estilos02.estiloButton(),
            text="Finalizar Pedido",
            command=finalizarPedido
            ).pack(pady=30, padx=40, anchor="e")



    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()