from Tkinter.imports import *  

class TelaBotoes:
    def __init__(self,master=None):
        self.janela = tk.Toplevel(master) if master else tk.Tk()
        self.janela.title("Informações sobre Botões em Tkinter")
        self.janela.geometry("600x500")
        # self.janela.configure(bg=Estilos.FUNDO_JANELA)
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            self.janela.iconbitmap(caminho_icone)
            
        titulo = tk.Label(self.janela, text="Widgets", font=("Arial", 16), bg="white")
        titulo.pack(pady=10)
        titulo = tk.Label(
            self.janela,
            text="Como funcionam os botões em Tkinter",
            # font=Estilos.FONTE_TITULO,
            # fg=Estilos.COR_TEXTO_TITULO,
            # bg=Estilos.FUNDO_JANELA
        )
        titulo.pack(pady=10)

        texto_explicativo = (
            "O que é um botão em Tkinter?\n"
            "Botões são widgets que o usuário pode clicar para executar uma ação.\n\n"

            "Para mais detalhes, consulte a documentação oficial do Button no Tkinter:\n"
            "https://docs.python.org/3/library/tkinter.html#tkinter.Button\n\n"

            "Como criar um botão:\n"
            "botao = tk.Button(janela, text=\"Clique aqui\", command=funcao)\n\n"

            "Principais atributos:\n"
            "text: define o texto do botão\n"
            "command: define a função a ser executada ao clicar\n"
            "font: define a fonte do texto\n"
            "bg: cor de fundo\n"
            "fg: cor do texto\n"
            "width/height: largura e altura\n"
            "padx/pady: espaçamento interno\n"
            "relief: estilo da borda (flat, raised, sunken, ridge, groove)\n"
            "bd: espessura da borda\n\n"

            "Exemplo:\n"
            "import tkinter as tk\n\n"
            "def saudacao():\n"
            "    print(\"Olá, mundo!\")\n\n"
            "janela = tk.Tk()\n"
            "botao = tk.Button(janela, text=\"Clique aqui\", command=saudacao,\n"
            "                  font=(\"Arial\", 12), bg=\"blue\", fg=\"white\")\n"
            "botao.pack(padx=10, pady=10)\n"
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
          
        )
        botao_executar.pack(pady=10)

    def executar_exemplo(self):
        nova_janela = tk.Toplevel(self.janela)
        nova_janela.title("Exemplo de Botão")
        nova_janela.geometry("300x180")
        nova_janela.configure(bg="#f0f0f0")
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            nova_janela.iconbitmap(caminho_icone)
        
        label_mensagem = tk.Label(
            nova_janela,
            text="",  
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="green"
        )
        label_mensagem.pack(pady=(0, 10))

        def saudacao():
            print("Olá, mundo!")  
            label_mensagem.config(text="Olá, mundo!") 

        botao = tk.Button(
            nova_janela,
            text="Clique aqui",
            command=saudacao,
            font=("Arial", 12),
            bg="blue",
            fg="white"
        )
        botao.pack(pady=10)

    def iniciar(self):
        self.janela.mainloop()