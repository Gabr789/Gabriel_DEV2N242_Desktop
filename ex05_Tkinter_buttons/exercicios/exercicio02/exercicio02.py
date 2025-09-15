import tkinter as tk

# Exercício 2 
# Crie três Radiobuttons com as opções: Manhã, Tarde, Noite. 
# Ao clicar em um botão de confirmação, mostre no Label o turno escolhido. 


class Ex02:
    def __init__(self, janelaPrincipal=None):
        self.janela = tk.Toplevel(janelaPrincipal) if janelaPrincipal else tk.Tk()
        self.janela.title("Exercício 2")
        self.janela.geometry("600x400")

        def confirmar():
            escolha = turno.get()

            if escolha == "__nada__":
                preferencias.config(text="Nenhuma opção escolhida")
            else:
                preferencias.config(text=f"Turno escolhido: {escolha}")

        local_escolhas = tk.Frame(self.janela)
        local_escolhas.pack(pady=20)

        tk.Label(local_escolhas, text="Escolha um turno:").pack(anchor="w")

        turno = tk.StringVar(value="__nada__")

        tk.Radiobutton(local_escolhas, text="Manhã", variable=turno, value="Manhã").pack(anchor="w")
        tk.Radiobutton(local_escolhas, text="Tarde", variable=turno, value="Tarde").pack(anchor="w")
        tk.Radiobutton(local_escolhas, text="Noite", variable=turno, value="Noite").pack(anchor="w")

        botao = tk.Button(self.janela, text="Confirmar escolha", command=confirmar)
        botao.pack(pady=10)

        preferencias = tk.Label(self.janela, text="")
        preferencias.pack(pady=10)


    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()

exe = Ex02()
exe.iniciar()