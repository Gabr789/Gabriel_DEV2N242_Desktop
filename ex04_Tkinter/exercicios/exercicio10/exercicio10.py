import tkinter as tk

# Exercício 10  
# Use dois campos Entry. Ao clicar no botão, mostre a junção dos dois textos no Label.  

class Ex0410:
    def __init__(self, janelaPrincipal=None):
        self.janela = tk.Toplevel(janelaPrincipal) if janelaPrincipal else tk.Tk()
        self.janela.title("Exercício 10")
        self.janela.geometry("600x400")


        def mostrarTextoJunto():
            texto1 = escrita1.get()
            texto2 = escrita2.get()
            textos_juntos = texto1 + texto2
            
                
            label_texto.config(text=f"Você digitou: {textos_juntos}")


        local_digitacao = tk.Frame(self.janela)
        local_digitacao.pack(pady=20)

        tk.Label(local_digitacao, text="Digite algo:").pack(side="left")

        escrita1 = tk.Entry(local_digitacao, width=30)
        escrita1.pack(side="left", padx=5)

        escrita2 = tk.Entry(local_digitacao, width=30)
        escrita2.pack(side="left", padx=5)

        botao = tk.Button(self.janela, text="Mostrar junção dos textos nos campos", command=mostrarTextoJunto)
        botao.pack(pady=10)

        label_texto = tk.Label(self.janela, text="")
        label_texto.pack(pady=10)


    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()