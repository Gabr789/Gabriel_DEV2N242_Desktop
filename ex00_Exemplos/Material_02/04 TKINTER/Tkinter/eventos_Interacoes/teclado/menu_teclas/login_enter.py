import tkinter as tk
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

class TelaLoginEnter:
    def __init__(self, master=None):
        self.janela = tk.Toplevel(master) if master else tk.Tk()
        self.janela.title("Login com Enter")
        self.janela.geometry("400x300")
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            self.janela.iconbitmap(caminho_icone)

        titulo = tk.Label(
            self.janela,
            text="Login com Tecla Enter",
            font=("Arial", 14, "bold")
        )
        titulo.pack(pady=15)

 
        frame_form = tk.Frame(self.janela)
        frame_form.pack(pady=10)

        tk.Label(frame_form, text="Usuário:", font=("Arial", 11)).grid(row=0, column=0, sticky="e", pady=5)
        self.entry_usuario = tk.Entry(frame_form, font=("Arial", 11), width=25)
        self.entry_usuario.grid(row=0, column=1, pady=5)

        tk.Label(frame_form, text="Senha:", font=("Arial", 11)).grid(row=1, column=0, sticky="e", pady=5)
        self.entry_senha = tk.Entry(frame_form, show="*", font=("Arial", 11), width=25)
        self.entry_senha.grid(row=1, column=1, pady=5)

       
        self.botao_login = tk.Button(self.janela, text="Entrar", font=("Arial", 11), command=self.realizar_login)
        self.botao_login.pack(pady=10)

        
        self.label_resultado = tk.Label(self.janela, text="", font=("Arial", 11), fg="green")
        self.label_resultado.pack()

      
        self.entry_usuario.bind("<Return>", self.acionar_login)
        self.entry_senha.bind("<Return>", self.acionar_login)

    def acionar_login(self, event):
        self.realizar_login()

    def realizar_login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()

        if usuario == "admin" and senha == "1234":
            self.label_resultado.config(text="Login bem-sucedido!", fg="green")
        else:
            self.label_resultado.config(text="Usuário ou senha incorretos.", fg="red")

    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()

if __name__ == "__main__":
    app = TelaLoginEnter()
    app.iniciar()