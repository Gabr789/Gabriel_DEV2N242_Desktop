import tkinter as tk
from tkinter import scrolledtext
from estilos.estilos import Estilos  
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
class TelaEntry:
    def __init__(self,master=None):
        self.janela = tk.Toplevel(master) if master else tk.Tk()
        self.janela.title("Informações sobre Entry em Tkinter")
        self.janela.geometry("600x500")
        # self.janela.configure(bg=Estilos.FUNDO_JANELA)
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            self.janela.iconbitmap(caminho_icone)
        titulo = tk.Label(
            self.janela,
            text="Como funcionam os campos de entrada (Entry)",
            # font=Estilos.FONTE_TITULO,
            # fg=Estilos.COR_TEXTO_TITULO,
            # bg=Estilos.FUNDO_JANELA
        )
        titulo.pack(pady=10)

        texto_explicativo = (
            "O que é um Entry em Tkinter?\n"
            "O widget Entry é usado para criar campos de entrada de texto de uma linha.\n\n"

            "Para mais detalhes, consulte a documentação oficial do Entry no Tkinter:\n"
            "https://docs.python.org/3/library/tkinter.html#tkinter.Entry\n\n"

            "Como criar um Entry:\n"
            "entrada = tk.Entry(janela)\n\n"

            "Principais atributos:\n"
            "width: define a largura do campo\n"
            "font: define a fonte e tamanho do texto\n"
            "fg: cor do texto (foreground)\n"
            "bg: cor de fundo (background)\n"
            "show: usado para ocultar caracteres (ex: senha)\n\n"

            "Métodos úteis:\n"
            "get(): retorna o texto digitado\n"
            "insert(posição, texto): insere texto na posição desejada\n"
            "delete(início, fim): remove texto\n\n"

            "Exemplo:\n"
            "import tkinter as tk\n\n"
            "def mostrar():\n"
            "    texto = campo.get()\n"
            "    print(f\"Você digitou: {texto}\")\n\n"
            "janela = tk.Tk()\n"
            "campo = tk.Entry(janela, width=30, font=(\"Arial\", 12))\n"
            "campo.pack(pady=10)\n"
            "botao = tk.Button(janela, text=\"Enviar\", command=mostrar)\n"
            "botao.pack(pady=10)\n"
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
        def mostrar_texto():
            texto = campo.get()
            print(f"Você digitou: {texto}")
            label_resultado.config(text=f"Você digitou: {texto}")

        nova_janela = tk.Toplevel(self.janela)
        nova_janela.title("Exemplo de Entry")
        nova_janela.geometry("350x200")
        nova_janela.configure(bg="#f0f0f0")
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            nova_janela.iconbitmap(caminho_icone)

        campo = tk.Entry(nova_janela, width=30, font=("Arial", 12))
        campo.pack(pady=10)

        botao = tk.Button(nova_janela, text="Enviar", command=mostrar_texto)
        botao.pack(pady=10)

        label_resultado = tk.Label(nova_janela, text="", font=("Arial", 12))
        label_resultado.pack(pady=10)

    def iniciar(self):
        self.janela.mainloop()
