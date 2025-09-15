from Tkinter.imports import *

class TelaInformativa:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Informações sobre Projeto Tkinter")
        self.janela.geometry("600x580")
        # self.janela.configure(bg=Estilos.FUNDO_JANELA) 

        titulo = tk.Label(
            self.janela,
            text="Como funciona um projeto em Tkinter",
            # font=Estilos.FONTE_TITULO,
            # fg=Estilos.COR_TEXTO_TITULO,
            # bg=Estilos.FUNDO_JANELA
        )
        titulo.pack(pady=10)

        texto_explicativo = (
            "O que é Tkinter?\n"
            "Tkinter é a biblioteca padrão de interfaces gráficas do Python.\n"
            "Ela permite criar janelas, botões, campos de texto, menus, entre outros componentes visuais.\n\n"

            "Para mais detalhes, consulte a documentação oficial do Tkinter:\n"
            "https://docs.python.org/3/library/tkinter.html\n\n"

            "Como executar um projeto:\n"
            "Crie um arquivo .py com sua interface.\n"
            "Importe tkinter: import tkinter as tk\n"
            "Crie a janela: janela = tk.Tk()\n"
            "Execute com: python nome_do_arquivo.py\n\n"

            " O que pode ser personalizado em uma janela Tkinter:\n"
            "Título da janela: `.title(\"Seu título\")`\n"
            "Tamanho da janela: `.geometry(\"larguraxaltura\")`\n"
            "Cor de fundo: `.configure(bg=\"cor\")`\n"
            "Ícone da janela: `.iconbitmap(\"caminho_para_icone.ico\")`\n"
            "Impedir redimensionamento: `.resizable(False, False)`\n"
            "Posição inicial: `.geometry(\"400x300+100+200\")`  # x=100, y=200\n"
            "Tela cheia: `.attributes(\"-fullscreen\", True)`\n"
            "Transparência: `.attributes(\"-alpha\", 0.8)`\n"
            "Sempre no topo: `.attributes(\"-topmost\", True)`\n\n"

            "O que pode ser personalizado nos widgets (componentes):\n"
            "Texto: `text=\"Exemplo\"`\n"
            "Fonte: `font=(\"Arial\", 14, \"bold\")`\n"
            "Cor do texto: `fg=\"blue\"`\n"
            "Cor de fundo: `bg=\"white\"`\n"
            "Alinhamento: `.pack()`, `.grid()`, `.place()`\n"
            "Largura/altura: `width=30`, `height=5`\n"
            "Bordas e estilos: `relief=\"raised\"`, `bd=2`\n"
            "Espaçamento interno: `padx`, `pady`\n\n"

            "Exemplo:\n"
            "janela = tk.Tk()\n"
            "janela.title(\"Minha Janela\")\n"
            "janela.geometry(\"400x300+200+150\")\n"
            "janela.configure(bg=\"lightblue\")\n"
            "janela.resizable(False, False)\n"
            "janela.iconbitmap(\"icone.ico\")\n"
            "janela.attributes(\"-alpha\", 0.95)\n"
            "janela.attributes(\"-topmost\", True)\n\n"
            "label = tk.Label(janela, text=\"Olá, Tkinter!\", font=(\"Arial\", 14), fg=\"darkblue\", bg=\"lightblue\")\n"
            "label.pack(pady=20)\n\n"
            "janela.mainloop()"
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
    
    def iniciar(self):
        self.janela.mainloop()
   
    def executar_exemplo(self):
        self.janela.withdraw()  

        nova_janela = tk.Toplevel(self.janela)
        nova_janela.title("Minha Janela")
        nova_janela.geometry("400x300+200+150")
        nova_janela.configure(bg="lightblue")
        nova_janela.resizable(False, False)
        nova_janela.attributes("-alpha", 0.95)
        nova_janela.attributes("-topmost", True)

        label = tk.Label(
            nova_janela,
            text="Olá, Tkinter!",
            font=("Arial", 14),
            fg="darkblue",
            bg="lightblue"
        )
        label.pack(pady=20)

    
        def ao_fechar():
            self.janela.deiconify() 
            nova_janela.destroy()

        nova_janela.protocol("WM_DELETE_WINDOW", ao_fechar)

