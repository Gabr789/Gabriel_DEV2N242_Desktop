import tkinter as tk
from exercicios.widgets.botoes import MeuBotao
from exercicios.widgets.labels import MeuLabel
from exercicios.widgets.janela import Janela
class Ex1_5(tk.Frame):
    def __init__(self, janela):
        super().__init__(janela, bg="white")

       
        self.email_var = tk.BooleanVar()
        self.sms_var = tk.BooleanVar()

     
        self.chk1 = tk.Checkbutton(self, text="Receber notificações por e-mail", variable=self.email_var, bg="white")
        self.chk1.pack(anchor="w", pady=2)

        self.chk2 = tk.Checkbutton(self, text="Receber notificações por SMS", variable=self.sms_var, bg="white")
        self.chk2.pack(anchor="w", pady=2)

        MeuBotao(self, "Confirmar", comando=self.mostrar)
        self.label = MeuLabel(self, "Selecione as opções")

    def mostrar(self):
        selecionados = []
        if self.email_var.get():
            selecionados.append("E-mail")
        if self.sms_var.get():
            selecionados.append("SMS")
        self.label.config(text="Selecionados: " + ", ".join(selecionados) if selecionados else "Nenhuma opção marcada")


