import tkinter as tk
from tkinter import messagebox

class JanelaPrincipal:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Menu Principal")
        self.janela.geometry("300x300")

       
        tk.Button(self.janela, text="Entrada de Texto", width=25, command=self.abrir_tela_texto).pack(pady=10)
        tk.Button(self.janela, text="Calculadora", width=25, command=self.abrir_tela_soma).pack(pady=10)
        tk.Button(self.janela, text="Operações com Texto e Números", width=25, command=self.abrir_tela_operacoes).pack(pady=10)
        tk.Button(self.janela, text="Sair", width=25, command=self.janela.quit).pack(pady=10)

    def abrir_tela_texto(self):
        janela_texto = tk.Toplevel()
        janela_texto.title("Entrada de Texto")
        janela_texto.geometry("350x250")

        label = tk.Label(janela_texto, text="Digite algo:")
        label.pack(pady=10)

        entrada = tk.Entry(janela_texto)
        entrada.pack(pady=5)

        resultado = tk.Label(janela_texto, text="")
        resultado.pack(pady=5)

        contador = tk.Label(janela_texto, text="")
        contador.pack(pady=5)

        def mostrar_texto():
            texto = entrada.get()
            if not texto.strip():
                messagebox.showwarning("Aviso", "O campo está vazio.",parent=janela_texto)
                return
            texto_maiusculo = texto.upper()
            resultado.config(text=f"Você digitou: {texto_maiusculo}")
            contador.config(text=f"Número de caracteres: {len(texto)}")

        def limpar():
            entrada.delete(0, tk.END)
            resultado.config(text="")
            contador.config(text="")

        def fechar():
            janela_texto.destroy()

        tk.Button(janela_texto, text="Mostrar Texto", command=mostrar_texto).pack(pady=5)
        tk.Button(janela_texto, text="Limpar", command=limpar).pack(pady=5)
        tk.Button(janela_texto, text="Fechar", command=fechar).pack(pady=5)

    def abrir_tela_soma(self):
        janela_soma = tk.Toplevel()
        janela_soma.title("Calculadora")
        janela_soma.geometry("350x300")

        tk.Label(janela_soma, text="Digite dois números:").pack(pady=10)

        entrada1 = tk.Entry(janela_soma)
        entrada1.pack(pady=5)

        entrada2 = tk.Entry(janela_soma)
        entrada2.pack(pady=5)

        resultado = tk.Label(janela_soma, text="", font=("Arial", 12, "bold"))
        resultado.pack(pady=10)

        def calcular_soma():
            valor1 = entrada1.get().strip()
            valor2 = entrada2.get().strip()
            if not valor1 or not valor2:
                messagebox.showwarning("Aviso", "Preencha os dois campos.",parent=janela_soma)
                return
            try:
                num1 = float(valor1)
                num2 = float(valor2)
                soma = num1 + num2
                resultado.config(text=f"Soma: {soma:.2f}")
            except ValueError:
                messagebox.showerror("Erro", "Digite apenas números válidos.",parent=janela_soma)

        def calcular_subtracao():
            valor1 = entrada1.get().strip()
            valor2 = entrada2.get().strip()
            if not valor1 or not valor2:
                messagebox.showwarning("Aviso", "Preencha os dois campos.",parent=janela_soma)
                return
            try:
                num1 = float(valor1)
                num2 = float(valor2)
                subtracao = num1 - num2
                resultado.config(text=f"Subtração: {subtracao:.2f}")
            except ValueError:
                messagebox.showerror("Erro", "Digite apenas números válidos.",parent=janela_soma)

        def limpar():
            entrada1.delete(0, tk.END)
            entrada2.delete(0, tk.END)
            resultado.config(text="")

        def fechar():
            janela_soma.destroy()

        tk.Button(janela_soma, text="Somar", command=calcular_soma).pack(pady=5)
        tk.Button(janela_soma, text="Subtrair", command=calcular_subtracao).pack(pady=5)
        tk.Button(janela_soma, text="Limpar", command=limpar).pack(pady=5)
        tk.Button(janela_soma, text="Fechar", command=fechar).pack(pady=5)

    def abrir_tela_operacoes(self):
        janela_op = tk.Toplevel()
        janela_op.title("Operações com Texto e Números")
        janela_op.geometry("400x400")

        tk.Label(janela_op, text="Entrada 1:").pack(pady=5)
        entrada1 = tk.Entry(janela_op)
        entrada1.pack(pady=5)

        tk.Label(janela_op, text="Entrada 2 (opcional):").pack(pady=5)
        entrada2 = tk.Entry(janela_op)
        entrada2.pack(pady=5)

        resultado = tk.Label(janela_op, text="", font=("Arial", 11))
        resultado.pack(pady=10)

        def texto_reverso():
            texto = entrada1.get().strip()
            if not texto:
                messagebox.showwarning("Aviso", "Campo vazio!", parent=janela_op)
                return
            reverso = texto[::-1]
            resultado.config(text=f"Texto Reverso: {reverso}")

        def dobro_numero():
            valor = entrada1.get().strip()
            try:
                numero = float(valor)
                resultado.config(text=f"Dobro: {numero * 2:.2f}")
            except ValueError:
                messagebox.showerror("Erro", "Digite um número válido.", parent=janela_op)

        def concatenar():
            texto1 = entrada1.get().strip()
            texto2 = entrada2.get().strip()
            if not texto1 or not texto2:
                messagebox.showwarning("Aviso", "Preencha os dois campos.",parent=janela_op)
                return
            resultado.config(text=f"Concatenado: {texto1 + texto2}")

        def limpar():
            entrada1.delete(0, tk.END)
            entrada2.delete(0, tk.END)
            resultado.config(text="")

        def fechar():
            janela_op.destroy()

        tk.Button(janela_op, text="Texto Reverso", command=texto_reverso).pack(pady=5)
        tk.Button(janela_op, text="Dobro do Número", command=dobro_numero).pack(pady=5)
        tk.Button(janela_op, text="Concatenar Textos", command=concatenar).pack(pady=5)
        tk.Button(janela_op, text="Limpar", command=limpar).pack(pady=5)
        tk.Button(janela_op, text="Fechar", command=fechar).pack(pady=5)

    def iniciar(self):
        self.janela.mainloop()


if __name__ == "__main__":
    app = JanelaPrincipal()
    app.iniciar()