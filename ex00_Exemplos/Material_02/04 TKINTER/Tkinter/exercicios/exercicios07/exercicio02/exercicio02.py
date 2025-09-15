import tkinter as tk
from exercicios.widgets.entradas import MeuEntry
from exercicios.widgets.labels import MeuLabel
from exercicios.widgets.botoes import MeuBotao

class Ex2_7(tk.Frame):
    def __init__(self, janela):
        super().__init__(janela)

        frame_form = tk.Frame(self)
        frame_form.pack(pady=10)

        MeuLabel(frame_form, "Usuário:")
        self.entry_user = MeuEntry(frame_form)

        MeuLabel(frame_form, "Senha:")
        self.entry_senha = MeuEntry(frame_form, show="*")

        MeuBotao(self, "Entrar", comando=self.verificar)

        self.resultado = MeuLabel(self, " ")

    def verificar(self):
        senha = self.entry_senha.pegar_texto()
        if senha == "1234":
            self.resultado.config(text="Login realizado com sucesso!", fg="green")
        else:
            self.resultado.config(text="Senha incorreta!", fg="red")