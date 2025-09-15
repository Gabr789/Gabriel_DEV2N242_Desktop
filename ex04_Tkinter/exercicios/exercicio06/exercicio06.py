import tkinter as tk

# Exercício 6 
# Faça um campo de texto Entry e um botão. Se o usuário clicar no botão sem digitar 
# nada, mostre "Campo vazio!" no Label.

class Ex0406:
    def __init__(self, janelaPrincipal=None):
        self.janela = tk.Toplevel(janelaPrincipal) if janelaPrincipal else tk.Tk()
        self.janela.title("Exercício 6")
        self.janela.geometry("600x400")


        def mostrarTexto():
            texto = escrita.get()
            if texto:
                label_texto.config(text=f"Campo preenchido!\nVocê digitou: {texto}")
            else:
                label_texto.config(text="Campo vazio!")


        local_digitacao = tk.Frame(self.janela)
        local_digitacao.pack(pady=20)

        tk.Label(local_digitacao, text="Digite algo:").pack(side="left")

        escrita = tk.Entry(local_digitacao, width=30)
        escrita.pack(side="left", padx=5)

        botao = tk.Button(self.janela, text="Mostrar texto escrito", command=mostrarTexto)
        botao.pack(pady=10)

        label_texto = tk.Label(self.janela, text="")
        label_texto.pack(pady=10)


    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()