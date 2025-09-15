import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
class TelaText:
    def __init__(self, master=None):
        self.janela = tk.Toplevel(master) if master else tk.Tk()
        self.janela.title("Text")
        self.janela.geometry("600x500")
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            self.janela.iconbitmap(caminho_icone)
        titulo = tk.Label(
            self.janela,
            text="Como funciona o Text",
            font=("Arial", 12, "bold")
        )
        titulo.pack(pady=10)

        texto_explicativo = (
            "O que é o widget Text?\n"
            "O widget Text do Tkinter é uma área de entrada de texto de múltiplas linhas.\n"
            "Ele permite ao usuário digitar ou exibir grandes quantidades de texto formatado.\n\n"
            "Principais características:\n"
            "- Permite múltiplas linhas de entrada\n"
            "- Suporta formatação de texto (tags, cores, fontes)\n"
            "- Pode ser usado para criar editores de texto simples\n\n"
            "Alguns métodos úteis:\n"
            "- insert(pos, texto): insere texto na posição indicada (ex: '1.0')\n"
            "- get(início, fim): obtém o texto entre duas posições (ex: '1.0', 'end')\n"
            "- delete(início, fim): remove texto entre posições\n"
            "- config(state='disabled'): torna o Text somente leitura\n\n"
            "Para mais detalhes, consulte a documentação oficial:\n"
            "https://docs.python.org/3/library/tkinter.html#text-widgets\n"
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

        tk.Button(frame_botoes, text="Text Editável", command=self.exemplo_editavel).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="Text Somente Leitura", command=self.exemplo_somente_leitura).pack(side=tk.LEFT, padx=5)

    def exemplo_editavel(self):
        nova_janela = tk.Toplevel(self.janela)
        nova_janela.title("Exemplo: Text Editável")
        nova_janela.geometry("400x350")
        nova_janela.configure(bg="#f0f0f0")
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            nova_janela.iconbitmap(caminho_icone)

        tk.Label(
            nova_janela,
            text="Digite um texto abaixo:",
            bg="#f0f0f0",
            font=("Arial", 11)
        ).pack(pady=5)

        text_area = tk.Text(nova_janela, width=50, height=10, font=("Arial", 10))
        text_area.pack(pady=5)

        resultado = tk.Label(nova_janela, text="", font=("Arial", 10), bg="#f0f0f0", fg="green")
        resultado.pack(pady=10)

        def mostrar_texto():
            conteudo = text_area.get("1.0", tk.END).strip()
            if conteudo:
                resultado.config(text="Texto inserido:\n" + conteudo)
            else:
                messagebox.showwarning("Aviso", "O campo de texto está vazio.", parent=nova_janela)

        tk.Button(nova_janela, text="Mostrar Texto", command=mostrar_texto).pack(pady=5)

    def exemplo_somente_leitura(self):
        nova_janela = tk.Toplevel(self.janela)
        nova_janela.title("Exemplo: Text Somente Leitura")
        nova_janela.geometry("400x300")
        nova_janela.configure(bg="#f0f0f0")
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            nova_janela.iconbitmap(caminho_icone)

        tk.Label(
            nova_janela,
            text="Este é um campo de texto somente leitura:",
            bg="#f0f0f0",
            font=("Arial", 11)
        ).pack(pady=5)

        texto_pre_definido = (
            "Este campo é somente leitura.\n"
            "Você pode usar essa configuração para exibir logs, mensagens ou textos\n"
            "sem permitir alterações pelo usuário."
        )

        text_area = tk.Text(nova_janela, width=50, height=8, font=("Arial", 10))
        text_area.insert("1.0", texto_pre_definido)
        text_area.config(state='disabled') 
        text_area.pack(pady=5)

    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()

