import tkinter as tk

# Exercício 8 
# Faça uma janela com Checkbuttons para os ingredientes: Queijo, Bacon, Tomate, 
# Cebola. Ao clicar no botão Montar Lanche, exiba os ingredientes selecionados. 


class Ex08:
    def __init__(self, janelaPrincipal=None):
        self.janela = tk.Toplevel(janelaPrincipal) if janelaPrincipal else tk.Tk()
        self.janela.title("Exercício 8")
        self.janela.geometry("600x400")

        def verificar():
            escolhas = []
            if self.queijo.get():
                escolhas.append("Queijo")
            if self.bacon.get():
                escolhas.append("Bacon")
            if self.tomate.get():
                escolhas.append("Tomate")
            if self.cebola.get():
                escolhas.append("Cebola")
            
            if escolhas:
                preferencias.config(text=f"Você escolheu os ingredientes: " + ", ".join(escolhas))
            else:
                preferencias.config(text="Você não escolheu nenhum ingrediente")

        local_escolhas = tk.Frame(self.janela)
        local_escolhas.pack(pady=20)

        tk.Label(local_escolhas, text="Escolha os ingredientes para o lanche:").pack(anchor="w")

        self.queijo = tk.BooleanVar()
        self.bacon = tk.BooleanVar()
        self.tomate = tk.BooleanVar()
        self.cebola = tk.BooleanVar()

        tk.Checkbutton(local_escolhas, text="Queijo", variable=self.queijo).pack(anchor="w")
        tk.Checkbutton(local_escolhas, text="Bacon", variable=self.bacon).pack(anchor="w")
        tk.Checkbutton(local_escolhas, text="Tomate", variable=self.tomate).pack(anchor="w")
        tk.Checkbutton(local_escolhas, text="Cebola", variable=self.cebola).pack(anchor="w")

        botao = tk.Button(self.janela, text="Montar Lanche", command=verificar)
        botao.pack(pady=10)

        preferencias = tk.Label(self.janela, text="")
        preferencias.pack(pady=10)


    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()

exe = Ex08()
exe.iniciar()