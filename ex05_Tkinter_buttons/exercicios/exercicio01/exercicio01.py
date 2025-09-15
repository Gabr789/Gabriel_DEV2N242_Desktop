import tkinter as tk

# Exercício 1 
# Crie uma janela com dois Checkbuttons: Receber notificações por e-mail e receber 
# notificações por SMS. Ao clicar em um botão, exiba no Label quais opções estão 
# marcadas.


class Ex01:
    def __init__(self, janelaPrincipal=None):
        self.janela = tk.Toplevel(janelaPrincipal) if janelaPrincipal else tk.Tk()
        self.janela.title("Exercício 1")
        self.janela.geometry("600x400")

        def verificar():
            escolhas = []
            if self.notificacao_email.get():
                escolhas.append("e-mail")
            if self.notificacao_sms.get():
                escolhas.append("SMS")
            
            if escolhas:
                preferencias.config(text=f"Você escolheu receber notificações por " + " e por ".join(escolhas))
            else:
                preferencias.config(text="Você não receberá notificações")

        local_escolhas = tk.Frame(self.janela)
        local_escolhas.pack(pady=20)

        tk.Label(local_escolhas, text="Escolha por onde quer receber notificações:").pack(anchor="w")

        self.notificacao_email = tk.BooleanVar()
        self.notificacao_sms = tk.BooleanVar()

        tk.Checkbutton(local_escolhas, text="E-mail", variable=self.notificacao_email).pack(anchor="w")
        tk.Checkbutton(local_escolhas, text="SMS", variable=self.notificacao_sms).pack(anchor="w")

        botao = tk.Button(self.janela, text="Confirmar escolha", command=verificar)
        botao.pack(pady=10)

        preferencias = tk.Label(self.janela, text="")
        preferencias.pack(pady=10)


    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()

exe = Ex01()
exe.iniciar()