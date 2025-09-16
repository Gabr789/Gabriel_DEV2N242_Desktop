import tkinter as tk
import os
import sys
from tkinter import messagebox
from estilo02 import Estilos02

# Exercício 2  
# Crie um formulário de login usando Frame, com os campos Usuário e Senha e um 
# botão Entrar. Ao clicar em Entrar, mostre uma mensagem de sucesso se a senha for 
# 1234 ou de erro, se for diferente.


class Ex02:
    def __init__(self, janelaPrincipal=None):
        self.janela = tk.Toplevel(janelaPrincipal) if janelaPrincipal else tk.Tk()
        self.janela.geometry("350x550")
        self.janela.resizable(False, False)
        self.janela.title("Exercício 02")
        self.janela.configure(Estilos02.estiloJanela())

        self.senha = "1234"

        caminho = os.path.dirname(__file__)


        def testar():
            valor = senha.get()
            if valor == self.senha:
                messagebox.showinfo("Logado", "Login realizado com sucesso!")
                sys.exit()
            else:
                messagebox.showerror("Erro", "Senha Incorreta, tente novamente!")


        """Frame de título e avatar"""

        frame = tk.Frame(self.janela, **Estilos02.estiloFrameLogin())
        frame.pack(fill="x")


        self.imagem = tk.PhotoImage(file=caminho + r"\avatar_login.png")

        tk.Label(
            frame,
            image=self.imagem,
            **Estilos02.estiloLabelImagem()
        ).pack(padx=10, pady=50)


        """Frame de login"""

        frame_login = tk.Frame(self.janela, Estilos02.estiloFrame())
        frame_login.pack(fill=tk.BOTH, expand=True)

        tk.Label(
            frame_login,
            text="Login",
            **Estilos02.estiloLabelTitulo()
        ).pack(pady=15)


        """Frame Campos"""

        frame_campos = tk.Frame(frame_login, Estilos02.estiloFrame())
        frame_campos.pack(fill=tk.BOTH, expand=True)


        """Campo usuário"""

        tk.Label(
            frame_campos,
            text="Usuário: ",
            **Estilos02.estiloLabelCampos()
        ).grid(row=1, column=0, padx=4, pady=20)

        usuario = tk.Entry(
            frame_campos,
            **Estilos02.estiloEntry()
        )
        usuario.grid(row=1, column=1)


        """Campo senha"""

        tk.Label(
            frame_campos,
            text="Senha: ",
            **Estilos02.estiloLabelCampos()
        ).grid(row=2, column=0, padx=4, pady=12)

        senha = tk.Entry(
            frame_campos,
            **Estilos02.estiloEntry()
        )
        senha.grid(row=2, column=1)


        """Botão para logar"""

        tk.Button(
            frame_campos,
            text="Entrar",
            **Estilos02.estiloBotao(),
            command=testar
        ).grid(row=3, column=1)


    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()
        

exe02 = Ex02()
exe02.iniciar()