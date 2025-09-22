# pip install pillow
from tkinter import *
from tkinter import messagebox
import os
from PIL import Image, ImageTk
from Tkinter.menu_principal.principal import MenuPrincipal  


class TelaLogin:
    def __init__(self, banco):
        self.banco = banco  
        self.janela = Tk()
        self.janela.title("Login")
        self.janela.geometry("300x400")
        self.janela.resizable(False, False)
        self.janela.configure(bg="white")
        self.tentativas = 0
        self.definir_icone()
        self.carregar_logo()
        self.criar_campos_login()
        self.criar_botoes()

    def definir_icone(self):
        caminho = os.path.join(os.path.dirname(__file__), "../logo.ico")
        if os.path.exists(caminho):
            self.janela.iconbitmap(caminho)

    def carregar_logo(self):
        caminho = os.path.join(os.path.dirname(__file__), "imagens/squirtle-sax-squirtle.gif")
        if not os.path.exists(caminho):
            return
        
        ext = os.path.splitext(caminho)[1].lower()

        self.label_imagem = Label(self.janela, bg="white")
        self.label_imagem.pack(pady=(15, 5))

        if ext == ".gif":
            self.carregar_gif(caminho)
        else:
            self.carregar_imagem_estatica(caminho)

    def carregar_gif(self, caminho):
        gif = Image.open(caminho)
        self.frames, self.duracoes = [], []

        try:
            while True:
                frame = gif.copy().resize((60, 60), Image.Resampling.LANCZOS)  
                self.frames.append(ImageTk.PhotoImage(frame))  
                self.duracoes.append(gif.info.get("duration", 100))  
                gif.seek(len(self.frames))  
        except EOFError:
            pass

        self.frame_atual = 0
        self.animar()

    def carregar_imagem_estatica(self, caminho):
        img = Image.open(caminho).resize((60, 60), Image.Resampling.LANCZOS)
        self.imagem = ImageTk.PhotoImage(img)
        self.label_imagem.config(image=self.imagem)

    def criar_campos_login(self):
        Label(self.janela, text="Usuário:", bg="white").pack(pady=(10, 5))
        self.entrada_usuario = Entry(self.janela, highlightthickness=1, highlightbackground="blue")
        self.entrada_usuario.pack(padx=20)

        Label(self.janela, text="Senha:", bg="white").pack(pady=(10, 5))
        self.entrada_senha = Entry(self.janela, show="*", highlightthickness=1, highlightbackground="blue")
        self.entrada_senha.pack(padx=20)

    def criar_botoes(self):
        Button(self.janela, text="Entrar", command=self.validar_login,
               bg="blue", fg="white").pack(pady=(20, 5))
        
        Button(self.janela, text="Cadastrar", command=self.abrir_cadastro,
               bg="green", fg="white").pack(pady=(5, 20))

    def animar(self):
        self.label_imagem.config(image=self.frames[self.frame_atual])
        self.frame_atual = (self.frame_atual + 1) % len(self.frames)
        self.janela.after(self.duracoes[self.frame_atual], self.animar)

    def validar_login(self):
        usuario = self.entrada_usuario.get().strip()
        senha = self.entrada_senha.get().strip()

        if not usuario and not senha:
            self.erro_login("Quê isso, Amigo! Preencha os campos de usuário e senha!")
            return
        elif not usuario:
            self.erro_login("Amigo, preencha o usuário!")
            return
        elif not senha:
            self.erro_login("Amigo, preencha a senha!")
            return

        if self.banco.validar_credenciais(usuario, senha):
            self.janela.withdraw()
            app = MenuPrincipal(self.janela)
            app.iniciar()
        else:
            self.erro_login("Usuário ou senha incorretos, Amigo!")

    def erro_login(self, mensagem):
        self.tentativas += 1
        if self.tentativas >= 3:
            messagebox.showerror("Erro", "Amigo, dá uma olhada na linha 75 de login.py")
            self.tentativas = 0
        else:
            messagebox.showerror("Erro", mensagem)

    def abrir_cadastro(self):
        cadastro = Toplevel(self.janela)
        cadastro.title("Cadastrar Usuário")
        cadastro.geometry("300x250")
        cadastro.configure(bg="white")
        cadastro.resizable(False, False)

        caminho_icone = os.path.join(os.path.dirname(__file__), "../logo.ico")
        if os.path.exists(caminho_icone):
            cadastro.iconbitmap(caminho_icone)

        Label(cadastro, text="Novo Usuário:", bg="white").pack(pady=(15, 5))
        entrada_novo_usuario = Entry(cadastro, highlightthickness=1, highlightbackground="green")
        entrada_novo_usuario.pack(padx=20)

        Label(cadastro, text="Nova Senha:", bg="white").pack(pady=(10, 5))
        entrada_nova_senha = Entry(cadastro, show="*", highlightthickness=1, highlightbackground="green")
        entrada_nova_senha.pack(padx=20)

        def salvar_usuario():
            novo_usuario = entrada_novo_usuario.get().strip()
            nova_senha = entrada_nova_senha.get().strip()

            if not novo_usuario or not nova_senha:
                messagebox.showerror("Erro", "Preencha usuário e senha!")
                return

            try:
                self.banco.salvar_usuario(novo_usuario, nova_senha)
                messagebox.showinfo("Sucesso", f"Usuário '{novo_usuario}' cadastrado com sucesso!")
                cadastro.destroy()
            except ValueError as e:
                messagebox.showerror("Erro", str(e))

        Button(cadastro, text="Salvar", command=salvar_usuario,
               bg="green", fg="white").pack(pady=20)

    def iniciar(self):
        self.janela.mainloop()