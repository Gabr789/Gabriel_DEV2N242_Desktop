import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from estilos.estilos import Estilos  
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

class TelaCombobox:
    def __init__(self, master=None):
        self.janela = tk.Toplevel(master) if master else tk.Tk()
        self.janela.title("Combobox")
        self.janela.geometry("600x500")
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            self.janela.iconbitmap(caminho_icone)


        titulo = tk.Label(
            self.janela,
            text="Como funcionam as Comboboxes",
            font=("Arial", 12, "bold")
        )
        titulo.pack(pady=10)

        texto_explicativo = (
            "O que é uma Combobox?\n"
            "Uma Combobox (ou caixa combinada) é um componente gráfico que permite ao usuário\n"
            "selecionar uma opção a partir de uma lista suspensa. Ela pode funcionar como um menu\n"
            "de seleção, onde apenas uma escolha é possível.\n\n"

            "Para mais detalhes, consulte a documentação oficial da Combobox no ttk:\n"
            "https://docs.python.org/3/library/tkinter.ttk.html#ttk.Combobox\n\n"

            "Situações comuns de uso incluem:\n"
            "- Seleção de país, estado ou cidade\n"
            "- Escolha de temas, cores ou configurações\n"
            "- Qualquer seleção entre várias opções conhecidas\n\n"

            "Como criar uma Combobox:\n"
            "Use o módulo ttk (interface moderna do Tkinter) para criar uma Combobox.\n"
            "Associe a Combobox a uma variável e defina uma lista de valores para ela.\n\n"

            "Exemplo básico:\n"
            "import tkinter as tk\n"
            "from tkinter import ttk\n\n"
            "janela = tk.Tk()\n"
            "opcoes = [\"Python\", \"Java\", \"C++\"]\n"
            "combo = ttk.Combobox(janela, values=opcoes)\n"
            "combo.pack()\n"
            "janela.mainloop()\n\n"

            "Principais atributos e métodos:\n"
            "- values: define a lista de opções\n"
            "- current(): define ou obtém o índice selecionado\n"
            "- get(): obtém o valor selecionado\n"
            "- state: pode ser \"readonly\" para impedir digitação manual\n"
            "- bind(): associa eventos (ex: seleção)\n\n"

            "Exemplo com função associada:\n"
            "def mostrar():\n"
            "    selecao = combo.get()\n"
            "    print(f\"Você escolheu: {selecao}\")\n\n"
            "combo = ttk.Combobox(janela, values=[\"Sim\", \"Não\"], state=\"readonly\")\n"
            "combo.bind(\"<<ComboboxSelected>>\", lambda e: mostrar())\n"
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
            command=self.executar_exemplo
        )
        botao_executar.pack(pady=10)

    def executar_exemplo(self):
        nova_janela = tk.Toplevel(self.janela)
        nova_janela.title("Exemplo de Combobox")
        nova_janela.geometry("300x200")
        nova_janela.configure(bg="#f0f0f0")
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            nova_janela.iconbitmap(caminho_icone)

        tk.Label(
            nova_janela,
            text="Escolha sua linguagem favorita:",
            bg="#f0f0f0",
            font=("Arial", 11)
        ).pack(pady=10)

        opcoes = ["Python", "Java", "C#", "JavaScript"]
        self.combo = ttk.Combobox(nova_janela, values=opcoes, state="readonly", font=("Arial", 10))
        self.combo.pack(pady=5)

        resultado = tk.Label(nova_janela, text="", bg="#f0f0f0", font=("Arial", 11), fg="blue")
        resultado.pack(pady=10)

        def mostrar():
            escolha = self.combo.get()
            if escolha:
                resultado.config(text=f"Sua escolha: {escolha}")
            else:
                resultado.config(text="Nenhuma opção selecionada.")

        tk.Button(nova_janela, text="Confirmar", command=mostrar).pack(pady=5)

    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()