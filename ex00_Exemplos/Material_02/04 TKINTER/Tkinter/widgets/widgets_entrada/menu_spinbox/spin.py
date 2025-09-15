import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
class TelaSpinbox:
    def __init__(self, master=None):
        self.janela = tk.Toplevel(master) if master else tk.Tk()
        self.janela.title("Spinbox")
        self.janela.geometry("600x500")
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            self.janela.iconbitmap(caminho_icone)
        titulo = tk.Label(
            self.janela,
            text="Como funciona o widget Spinbox",
            font=("Arial", 12, "bold")
        )
        titulo.pack(pady=10)

        texto_explicativo = (
            "O que é um Spinbox?\n"
            "O Spinbox é um widget do Tkinter que permite ao usuário selecionar um valor\n"
            "numérico ou de uma lista de opções, utilizando setas para cima e para baixo.\n\n"
            "É útil para selecionar:\n"
            "- Quantidades numéricas\n"
            "- Anos, meses ou dias\n"
            "- Faixas de valores definidas\n"
            "- Opções fixas de uma lista\n\n"
            "Sintaxe básica:\n"
            "spin = tk.Spinbox(janela, from_=1, to=10)\n"
            "spin = tk.Spinbox(janela, values=(\"Pequeno\", \"Médio\", \"Grande\"))\n\n"
            "Principais argumentos:\n"
            "- from_, to: valores numéricos de início e fim\n"
            "- values: tupla/lista de opções fixas\n"
            "- increment: define o passo entre os valores\n"
            "- command: função chamada quando o valor muda\n\n"
            "Mais detalhes: https://docs.python.org/3/library/tkinter.html#tkinter.Spinbox\n"
        )

        area_texto = scrolledtext.ScrolledText(
            self.janela,
            wrap=tk.WORD,
            width=70,
            height=15,
            font=("Arial", 10)
        )
        area_texto.insert(tk.INSERT, texto_explicativo)
        area_texto.config(state='disabled')
        area_texto.pack(padx=10, pady=10)

        frame_botoes = tk.Frame(self.janela)
        frame_botoes.pack(pady=10)

        tk.Button(frame_botoes, text="Spinbox Numérico", command=self.exemplo_numerico).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="Spinbox por Lista", command=self.exemplo_lista).pack(side=tk.LEFT, padx=5)

    def exemplo_numerico(self):
        nova_janela = tk.Toplevel(self.janela)
        nova_janela.title("Exemplo: Spinbox Numérico")
        nova_janela.geometry("300x200")
        nova_janela.configure(bg="#f0f0f0")
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            nova_janela.iconbitmap(caminho_icone)
        tk.Label(
            nova_janela,
            text="Escolha sua idade:",
            font=("Arial", 11),
            bg="#f0f0f0"
        ).pack(pady=10)

        spin = tk.Spinbox(nova_janela, from_=0, to=120, font=("Arial", 11), width=10)
        spin.pack(pady=5)

        resultado = tk.Label(nova_janela, text="", bg="#f0f0f0", font=("Arial", 10), fg="green")
        resultado.pack(pady=10)

        def mostrar_valor():
            idade = spin.get()
            resultado.config(text=f"Idade selecionada: {idade} anos")

        tk.Button(nova_janela, text="Confirmar", command=mostrar_valor).pack(pady=5)

    def exemplo_lista(self):
        nova_janela = tk.Toplevel(self.janela)
        nova_janela.title("Exemplo: Spinbox com Lista de Opções")
        nova_janela.geometry("300x200")
        nova_janela.configure(bg="#f0f0f0")
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            nova_janela.iconbitmap(caminho_icone)

        tamanhos = ("Pequeno", "Médio", "Grande", "Extra Grande")

        tk.Label(
            nova_janela,
            text="Selecione um tamanho de camisa:",
            font=("Arial", 11),
            bg="#f0f0f0"
        ).pack(pady=10)

        spin = tk.Spinbox(nova_janela, values=tamanhos, font=("Arial", 11), width=15)
        spin.pack(pady=5)

        resultado = tk.Label(nova_janela, text="", bg="#f0f0f0", font=("Arial", 10), fg="blue")
        resultado.pack(pady=10)

        def mostrar_valor():
            tamanho = spin.get()
            resultado.config(text=f"Tamanho selecionado: {tamanho}")

        tk.Button(nova_janela, text="Confirmar", command=mostrar_valor).pack(pady=5)

    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()

