import tkinter as tk

# Exercício 9 
# Ao digitar um número no Entry e clicar no botão, mostre o dobro do número no Label.

class Ex0409:
    def __init__(self, janelaPrincipal=None):
        self.janela = tk.Toplevel(janelaPrincipal) if janelaPrincipal else tk.Tk()
        self.janela.title("Exercício 9")
        self.janela.geometry("600x400")


        def mostrarTexto():
            try:
                num = float(numero.get())
                dobro = num * 2
                label_dobro.config(text=f"Dobro do valor digitado: {dobro}")
            except (TypeError, ValueError):
                label_dobro.config(text="Erro: Preencha o campo com um número")


        local_digitacao = tk.Frame(self.janela)
        local_digitacao.pack(pady=20)

        tk.Label(local_digitacao, text="Digite um número:").pack(side="left")

        numero = tk.Entry(local_digitacao, width=30)
        numero.pack(side="left", padx=5)

        botao = tk.Button(self.janela, text="Mostrar dobro do valor digitado", command=mostrarTexto)
        botao.pack(pady=10)

        label_dobro = tk.Label(self.janela, text="")
        label_dobro.pack(pady=10)


    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()