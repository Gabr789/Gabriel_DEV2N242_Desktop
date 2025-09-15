import tkinter as tk

# Exercício 7 
# Insira um Entry, um Label e dois botões um botão mostra o texto digitado. 
# Outro botão limpa o campo e o texto do Label.

class Ex0407:
    def __init__(self, janelaPrincipal=None):
        self.janela = tk.Toplevel(janelaPrincipal) if janelaPrincipal else tk.Tk()
        self.janela.title("Exercício 7")
        self.janela.geometry("600x400")


        def mostrarTexto():
            texto = escrita.get()
            label_texto.config(text=f"Você digitou: {texto}")

        def apagarTexto():
            texto = escrita.get()
            escrita.delete(0, len(texto))

            label_texto.config(text="")


        local_digitacao = tk.Frame(self.janela)
        local_digitacao.pack(pady=20)

        tk.Label(local_digitacao, text="Digite algo:").pack(side="left")

        escrita = tk.Entry(local_digitacao, width=30)
        escrita.pack(side="left", padx=5)

        botao1 = tk.Button(self.janela, text="Mostrar texto escrito", command=mostrarTexto)
        botao1.pack(pady=10)

        botao2 = tk.Button(self.janela, text="Apagar texto do campo e do label", command=apagarTexto)
        botao2.pack(pady=10)

        label_texto = tk.Label(self.janela, text="")
        label_texto.pack(pady=10)


    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()