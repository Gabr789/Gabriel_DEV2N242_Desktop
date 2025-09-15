import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

import tkinter as tk
from tkinter import scrolledtext
from estilos.estilos import Estilos  

class TelaLabel:
    def __init__(self,master=None):
        self.janela = tk.Toplevel(master) if master else tk.Tk()
        self.janela.title("Informações sobre Labels em Tkinter")
        self.janela.geometry("600x500")
        # self.janela.configure(bg=Estilos.FUNDO_JANELA)
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            self.janela.iconbitmap(caminho_icone)
        titulo = tk.Label(
            self.janela,
            text="Como funcionam os Labels em Tkinter",
            # font=Estilos.FONTE_TITULO,
            # fg=Estilos.COR_TEXTO_TITULO,
            # bg=Estilos.FUNDO_JANELA
        )
        titulo.pack(pady=10)

        texto_explicativo = (
            "O que é um Label em Tkinter?\n"
            "Um Label é um widget usado para exibir texto (ou imagens) em uma interface gráfica.\n"
            "Ele é frequentemente utilizado para títulos, mensagens informativas ou feedbacks.\n\n"

            "Para mais detalhes, consulte a documentação oficial do Label no Tkinter:\n"
            "https://docs.python.org/3/library/tkinter.html#tkinter.Label\n\n"

            "Como criar um Label:\n"
            "label = tk.Label(janela, text=\"Texto aqui\")\n\n"

            "Principais atributos:\n"
            "text: conteúdo textual do label\n"
            "font: fonte do texto\n"
            "bg: cor de fundo\n"
            "fg: cor do texto\n"
            "width/height: tamanho do label\n"
            "anchor: alinhamento do texto\n"
            "justify: alinhamento de múltiplas linhas\n"
            "wraplength: comprimento máximo da linha\n\n"

            "Exemplo:\n"
            "import tkinter as tk\n\n"
            "janela = tk.Tk()\n"
            "label = tk.Label(janela, text=\"Bem-vindo!\", font=(\"Arial\", 12))\n"
            "label.pack(padx=10, pady=10)\n"
            "janela.mainloop()\n"
        )

        area_texto = scrolledtext.ScrolledText(
            self.janela,
            wrap=tk.WORD,
            width=70,
            height=20,
            font=("Arial", 10)
        )
        area_texto.insert(tk.INSERT, texto_explicativo)
        area_texto.config(state='disabled')
        area_texto.pack(padx=10, pady=10)

        botao_executar = tk.Button(
            self.janela,
            text="Executar Exemplo",
            command=self.executar_exemplo,
            # **Estilos.estilo_botao()
        )
        botao_executar.pack(pady=10)

    def executar_exemplo(self):
        nova_janela = tk.Toplevel(self.janela)
        nova_janela.title("Exemplo de Label")
        nova_janela.geometry("300x180")
        nova_janela.configure(bg="#f0f0f0")
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            nova_janela.iconbitmap(caminho_icone)

        label_exemplo = tk.Label(
            nova_janela,
            text="Clique no botão para atualizar o texto",
            font=("Arial", 11),
            fg="black",
            bg="#f0f0f0",
            wraplength=280,
            justify="center"
        )
        label_exemplo.pack(pady=20)

        def atualizar_label():
            label_exemplo.config(text="Texto atualizado com sucesso!", fg="green")

        botao = tk.Button(
            nova_janela,
            text="Atualizar Texto",
            command=atualizar_label,
            font=("Arial", 11),
            bg="blue",
            fg="white"
        )
        botao.pack(pady=10)

   
    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()