import os
import tkinter as tk
from tkinter import scrolledtext

class TelaScale:
    def __init__(self, master=None):
        self.janela = tk.Toplevel()
        self.janela.title("Scale (Controle Deslizante)")
        self.janela.geometry("600x500")
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            self.janela.iconbitmap(caminho_icone)
        titulo = tk.Label(
            self.janela,
            text="Como funciona o widget Scale",
            font=("Arial", 12, "bold")
        )
        titulo.pack(pady=10)

        texto_explicativo = (
            "O que é um Scale?\n"
            "O widget Scale (ou controle deslizante) permite ao usuário selecionar um valor\n"
            "dentro de um intervalo definido. Ele pode ser orientado horizontalmente ou verticalmente.\n\n"
            "É ideal para selecionar:\n"
            "- Volume\n"
            "- Brilho\n"
            "- Tamanhos ou porcentagens\n"
            "- Qualquer valor numérico com controle mais visual\n\n"
            "Sintaxe básica:\n"
            "scale = tk.Scale(janela, from_=0, to=100, orient=tk.HORIZONTAL)\n\n"
            "Principais argumentos:\n"
            "- from_: valor inicial do intervalo\n"
            "- to: valor final do intervalo\n"
            "- orient: orientação do controle (tk.HORIZONTAL ou tk.VERTICAL)\n"
            "- resolution: define o passo (ex: 0.1)\n"
            "- tickinterval: mostra marcas com espaçamento fixo\n"
            "- length: comprimento do controle\n"
            "- command: função chamada quando o valor muda\n\n"
            "Mais detalhes: https://docs.python.org/3/library/tkinter.html#tkinter.Scale\n"
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

        tk.Button(frame_botoes, text="Scale Horizontal", command=self.exemplo_horizontal).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="Scale Vertical", command=self.exemplo_vertical).pack(side=tk.LEFT, padx=5)

    def exemplo_horizontal(self):
        nova_janela = tk.Toplevel(self.janela)
        nova_janela.title("Exemplo: Scale Horizontal")
        nova_janela.geometry("400x200")
        nova_janela.configure(bg="#f0f0f0")
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            nova_janela.iconbitmap(caminho_icone)

        tk.Label(
            nova_janela,
            text="Volume de Áudio:",
            font=("Arial", 11),
            bg="#f0f0f0"
        ).pack(pady=10)

        valor = tk.IntVar()

        scale = tk.Scale(nova_janela, from_=0, to=100, orient=tk.HORIZONTAL, variable=valor)
        scale.pack(pady=5)

        resultado = tk.Label(nova_janela, text="", bg="#f0f0f0", font=("Arial", 10), fg="blue")
        resultado.pack(pady=10)

        def confirmar():
            resultado.config(text=f"Volume: {valor.get()}%")

        tk.Button(nova_janela, text="Confirmar", command=confirmar).pack(pady=5)

    def exemplo_vertical(self):
        nova_janela = tk.Toplevel(self.janela)
        nova_janela.title("Exemplo: Scale Vertical")
        nova_janela.geometry("300x300")
        nova_janela.configure(bg="#f0f0f0")
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            nova_janela.iconbitmap(caminho_icone)

        tk.Label(
            nova_janela,
            text="Brilho da Tela:",
            font=("Arial", 11),
            bg="#f0f0f0"
        ).pack(pady=10)

        valor = tk.IntVar()

        scale = tk.Scale(
            nova_janela,
            from_=0,
            to=100,
            orient=tk.VERTICAL,
            variable=valor,
            length=200
        )
        scale.pack()

        resultado = tk.Label(nova_janela, text="", bg="#f0f0f0", font=("Arial", 10), fg="green")
        resultado.pack(pady=10)

        def confirmar():
            resultado.config(text=f"Brilho: {valor.get()}%")

        tk.Button(nova_janela, text="Confirmar", command=confirmar).pack(pady=5)

    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()