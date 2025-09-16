import tkinter as tk

# Exercício 4 
# Crie Checkbuttons para escolher linguagens que o usuário conhece: Python, Java, 
# JavaScript. Ao clicar em um botão, exiba todas as opções marcadas no Label.


class Ex0504:
    def __init__(self, janelaPrincipal=None):
        self.janela = tk.Toplevel(janelaPrincipal) if janelaPrincipal else tk.Tk()
        self.janela.title("Exercício 4")
        self.janela.geometry("600x400")

        def verificar():
            escolhas = []
            if self.python.get():
                escolhas.append("Python")
            if self.java.get():
                escolhas.append("Java")
            if self.javascript.get():
                escolhas.append("JavaScript")
            
            if escolhas:
                preferencias.config(text=f"Você escolheu as linguagens: " + ", ".join(escolhas))
            else:
                preferencias.config(text="Você não escolheu nenhuma linguagem")

        local_escolhas = tk.Frame(self.janela)
        local_escolhas.pack(pady=20)

        tk.Label(local_escolhas, text="Escolha as linguagens que você conhece:").pack(anchor="w")

        self.python = tk.BooleanVar()
        self.java = tk.BooleanVar()
        self.javascript = tk.BooleanVar()

        tk.Checkbutton(local_escolhas, text="Python", variable=self.python).pack(anchor="w")
        tk.Checkbutton(local_escolhas, text="Java", variable=self.java).pack(anchor="w")
        tk.Checkbutton(local_escolhas, text="JavaScript", variable=self.javascript).pack(anchor="w")

        botao = tk.Button(self.janela, text="Confirmar escolha", command=verificar)
        botao.pack(pady=10)

        preferencias = tk.Label(self.janela, text="")
        preferencias.pack(pady=10)


    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()