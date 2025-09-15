import tkinter as tk

# Exercício 2  
# Crie uma janela com um Entry, um Button e um Label. Ao clicar no botão, o texto 
# digitado deve ser exibido em letras maiúsculas no Label. 

class Ex0402:
    def __init__(self, janelaPrincipal=None):
        self.janela = tk.Toplevel(janelaPrincipal) if janelaPrincipal else tk.Tk()
        self.janela.title("Exercício 2")
        self.janela.geometry("600x400")


        def mostrarTexto():
            texto = escrita.get().upper()
            label_texto.config(text=f"Você digitou: {texto}")


        local_digitacao = tk.Frame(self.janela)
        local_digitacao.pack(pady=20)

        tk.Label(local_digitacao, text="Digite algo:").pack(side="left")

        escrita = tk.Entry(local_digitacao, width=30)
        escrita.pack(side="left", padx=5)

        botao = tk.Button(self.janela, text="Mostrar texto escrito em maiúsculo", command=mostrarTexto)
        botao.pack(pady=10)

        label_texto = tk.Label(self.janela, text="")
        label_texto.pack(pady=10)


    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()