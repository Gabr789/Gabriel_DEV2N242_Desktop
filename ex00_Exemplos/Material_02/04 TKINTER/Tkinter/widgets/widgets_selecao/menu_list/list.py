import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
class TelaListbox:
    def __init__(self, master=None):
        self.janela = tk.Toplevel(master) if master else tk.Tk()
        self.janela.title("Listbox")
        self.janela.geometry("600x550")
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            self.janela.iconbitmap(caminho_icone)
        titulo = tk.Label(
            self.janela,
            text="Como funcionam os Listboxes",
            font=("Arial", 12, "bold")
        )
        titulo.pack(pady=10)

        texto_explicativo = (
            "O que é um Listbox?\n"
            "Um Listbox é um componente gráfico que apresenta uma lista de itens\n"
            "para seleção pelo usuário. Pode permitir seleção única ou múltipla.\n\n"
            "Para mais detalhes, consulte a documentação oficial do Tkinter:\n"
            "https://docs.python.org/3/library/tkinter.html#tkinter.Listbox\n\n"
            "Situações comuns de uso incluem:\n"
            "- Listar opções para seleção\n"
            "- Exibir listas de itens\n"
            "- Seleção de múltiplos itens com Ctrl/Shift\n\n"
            "Como criar um Listbox:\n"
            "- Crie o widget Listbox\n"
            "- Insira itens usando o método insert\n"
            "- Configure o modo de seleção (única, múltipla)\n\n"
            "Principais atributos e métodos:\n"
            "- insert(posição, item): insere itens\n"
            "- get(início, fim): obtém itens selecionados\n"
            "- curselection(): retorna índices selecionados\n"
            "- selectmode: SINGLE (Único), BROWSE (Navegar), MULTIPLE (Múltiplo), EXTENDED (Estendido)\n"
            "- bind(): associa eventos (ex: seleção)\n"
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

       
        tk.Button(frame_botoes, text="SINGLE (Único)", command=self.exemplo_single).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="BROWSE (Navegar)", command=self.exemplo_browse).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="MULTIPLE (Múltiplo)", command=self.exemplo_multiple).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="EXTENDED (Estendido)", command=self.exemplo_extended).pack(side=tk.LEFT, padx=5)

    def criar_janela_listbox(self, modo, nome, explicacao, tamanho):
        nova_janela = tk.Toplevel(self.janela)
        nova_janela.title(f"Exemplo Listbox - {nome}")
        nova_janela.geometry(tamanho)
        nova_janela.configure(bg="#f0f0f0")
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            nova_janela.iconbitmap(caminho_icone)

        tk.Label(
            nova_janela,
            text=explicacao,
            bg="#f0f0f0",
            font=("Arial", 10),
            justify=tk.LEFT,
            wraplength=int(tamanho.split("x")[0]) - 20
        ).pack(padx=10, pady=10)

        tk.Label(
            nova_janela,
            text=f"Selecione uma ou mais frutas ({nome}):",
            bg="#f0f0f0",
            font=("Arial", 11)
        ).pack(pady=5)

        listbox = tk.Listbox(nova_janela, selectmode=modo, font=("Arial", 11))
        frutas = ["Maçã", "Banana", "Laranja", "Manga", "Uva", "Abacaxi"]
        for fruta in frutas:
            listbox.insert(tk.END, fruta)
        listbox.pack(pady=5, fill=tk.BOTH, expand=True)

        resultado = tk.Label(nova_janela, text="", bg="#f0f0f0", font=("Arial", 11), fg="green")
        resultado.pack(pady=10)

        def mostrar_selecionados():
            selecionados = [listbox.get(i) for i in listbox.curselection()]
            if selecionados:
                resultado.config(text="Você selecionou: " + ", ".join(selecionados))
            else:
                resultado.config(text="Nenhuma fruta selecionada.")

        tk.Button(nova_janela, text="Confirmar", command=mostrar_selecionados).pack(pady=5)

    def exemplo_single(self):
        
        self.criar_janela_listbox(
            tk.SINGLE,
            "SINGLE (Único)",
            "Modo SINGLE: Permite selecionar apenas um item por vez.\nIdeal para quando você quer que o usuário escolha apenas uma opção.",
            "400x400"
        )

    def exemplo_browse(self):
        self.criar_janela_listbox(
            tk.BROWSE,
            "BROWSE (Navegar)",
            "Modo BROWSE: Muito parecido com SINGLE, mas permite\nque o usuário navegue com o mouse na lista sem selecionar imediatamente.",
            "400x400"
        )

    def exemplo_multiple(self):
        self.criar_janela_listbox(
            tk.MULTIPLE,
            "MULTIPLE (Múltiplo)",
            "Modo MULTIPLE: Permite selecionar múltiplos itens\nindependentemente, clicando em cada um (Ctrl+clique para múltiplos).",
            "400x400"
        )

    def exemplo_extended(self):
        self.criar_janela_listbox(
            tk.EXTENDED,
            "EXTENDED (Estendido)",
            "Modo EXTENDED: Permite seleção múltipla contínua,\nusando Shift+clique para selecionar intervalos e Ctrl para múltiplos itens isolados.",
           "400x400"
        )

    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()

