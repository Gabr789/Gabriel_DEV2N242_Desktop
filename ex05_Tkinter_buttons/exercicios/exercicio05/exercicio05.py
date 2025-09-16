import tkinter as tk

# Exercício 5 
# Crie Radiobuttons com as opções de gênero: Masculino, Feminino, Outro. 
# Mostre a opção escolhida quando o botão Confirmar for clicado.


class Ex0505:
    def __init__(self, janelaPrincipal=None):
        self.janela = tk.Toplevel(janelaPrincipal) if janelaPrincipal else tk.Tk()
        self.janela.title("Exercício 5")
        self.janela.geometry("600x400")

        def confirmar():
            escolha = genero.get()

            if escolha == "__nada__":
                preferencias.config(text="Nenhuma opção escolhida")
            else:
                preferencias.config(text=f"Gênero escolhido: {escolha}")

        local_escolhas = tk.Frame(self.janela)
        local_escolhas.pack(pady=20)

        tk.Label(local_escolhas, text="Escolha um turno:").pack(anchor="w")

        genero = tk.StringVar(value="__nada__")

        tk.Radiobutton(local_escolhas, text="Masculino", variable=genero, value="Masculino").pack(anchor="w")
        tk.Radiobutton(local_escolhas, text="Feminino", variable=genero, value="Feminino").pack(anchor="w")
        tk.Radiobutton(local_escolhas, text="Outro", variable=genero, value="Outro").pack(anchor="w")

        botao = tk.Button(self.janela, text="Confirmar escolha", command=confirmar)
        botao.pack(pady=10)

        preferencias = tk.Label(self.janela, text="")
        preferencias.pack(pady=10)


    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()