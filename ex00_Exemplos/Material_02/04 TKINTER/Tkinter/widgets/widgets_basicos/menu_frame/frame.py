from Tkinter.imports import *   
class TelaFrame:
    def __init__(self, master=None):
        self.janela = tk.Toplevel(master) if master else tk.Tk()
        self.janela.title("Frame")
        self.janela.geometry("600x500")
        # self.janela.configure(bg=Estilos.FUNDO_JANELA)
        
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            self.janela.iconbitmap(caminho_icone)

        titulo = tk.Label(
            self.janela,
            text="Como funcionam os Frames em Tkinter",
            # font=Estilos.FONTE_TITULO,
            # bg=Estilos.FUNDO_JANELA
        )
        titulo.pack(pady=10)

        texto_explicativo = (
            "O que é um Frame?\n"
            "O Frame é um contêiner usado para agrupar e organizar outros widgets dentro de uma interface Tkinter.\n"
            "É muito útil para criar seções visuais, alinhar componentes ou organizar a interface em blocos.\n\n"

            "Documentação oficial:\n"
            "https://docs.python.org/3/library/tkinter.html#tkinter.Frame\n\n"

            "Como criar um Frame:\n"
            "frame = tk.Frame(janela)\n\n"

            "Atributos comuns:\n"
            "- bg: cor de fundo\n"
            "- bd: largura da borda\n"
            "- relief: estilo da borda (flat, raised, sunken, ridge, groove)\n"
            "- width/height: tamanho do frame (opcional)\n"
            "- padx/pady: espaçamento interno\n\n"

            "Exemplo de código:\n"
            "import tkinter as tk\n\n"
            "janela = tk.Tk()\n"
            "frame = tk.Frame(janela, bg='lightblue', bd=2, relief='groove')\n"
            "frame.pack(padx=10, pady=10)\n\n"
            "tk.Label(frame, text='Nome:').pack()\n"
            "tk.Entry(frame).pack()\n\n"
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
            command=self.executar_exemplo
        )
        botao_executar.pack(pady=10)

    def executar_exemplo(self):
        nova_janela = tk.Toplevel(self.janela)
        nova_janela.title("Exemplo de Frame")
        nova_janela.geometry("350x200")
        nova_janela.configure(bg="#f0f0f0")
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            nova_janela.iconbitmap(caminho_icone)
        

        frame_login = tk.Frame(nova_janela, bg="#e0e0ff", bd=2, relief="ridge", padx=10, pady=10)
        frame_login.pack(pady=20)

        tk.Label(frame_login, text="Usuário:", bg="#e0e0ff").grid(row=0, column=0, sticky="e", pady=5)
        entry_usuario = tk.Entry(frame_login)
        entry_usuario.grid(row=0, column=1, pady=5)

        tk.Label(frame_login, text="Senha:", bg="#e0e0ff").grid(row=1, column=0, sticky="e", pady=5)
        entry_senha = tk.Entry(frame_login, show="*")
        entry_senha.grid(row=1, column=1, pady=5)

        def verificar_login():
            usuario = entry_usuario.get()
            senha = entry_senha.get()

            if senha == "1234":  
                self.abrir_tela_sucesso()
            else:
                messagebox.showerror("Erro de login", "Senha incorreta!", parent=nova_janela)

        tk.Button(frame_login, text="Entrar", command=verificar_login).grid(row=2, columnspan=2, pady=10)

    def abrir_tela_sucesso(self):
        janela_sucesso = tk.Toplevel(self.janela)
        janela_sucesso.title("Bem-vindo")
        janela_sucesso.geometry("250x150")
        tk.Label(janela_sucesso, text="Login realizado com sucesso!", font=("Arial", 12), fg="green").pack(expand=True)

    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()