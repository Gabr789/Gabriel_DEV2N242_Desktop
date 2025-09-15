import tkinter as tk

# Exercício 5 
# Mesmo formato do exercício anterior, mas com a operação de subtração.

class Ex0405:
    def __init__(self, janelaPrincipal=None):
        self.janela = tk.Toplevel(janelaPrincipal) if janelaPrincipal else tk.Tk()
        self.janela.title("Exercício 4")
        self.janela.geometry("600x400")


        def mostrarSubtracao():
            try:
                num1 = float(numero1.get())
                num2 = float(numero2.get())

                if isinstance(num1, (float)) and isinstance(num2, (float)):
                    subtracao = num1 - num2
                    label_subtracao.config(text=f"{num1} - {num2} = {subtracao}")

            except (TypeError, ValueError):
                label_subtracao.config(text="Erro: Preencha os dois campos com números")


        digitacao_num1 = tk.Frame(self.janela)
        digitacao_num1.pack(pady=10)

        digitacao_num2 = tk.Frame(self.janela)
        digitacao_num2.pack(pady=10)

        tk.Label(digitacao_num1, text="Digite o primeiro número:").pack(side="left")

        numero1 = tk.Entry(digitacao_num1, width=30)
        numero1.pack(side="left", padx=5)

        tk.Label(digitacao_num2, text="Digite o segundo número:").pack(side="left")

        numero2 = tk.Entry(digitacao_num2, width=30)
        numero2.pack(side="left", padx=5)

        botao = tk.Button(self.janela, text="Mostrar subtração do primeiro número pelo segundo", command=mostrarSubtracao)
        botao.pack(pady=10)

        label_subtracao = tk.Label(self.janela, text="")
        label_subtracao.pack(pady=10)


    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()