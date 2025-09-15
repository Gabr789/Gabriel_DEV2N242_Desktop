import tkinter as tk
from estilo01 import Estilos01

# Exercício 1
# Crie uma janela com dois frames: Um frame para informações pessoais: campos 
# Nome e Idade 
# Um frame com um botão Exibir, que ao ser clicado, mostra os dados em um Label 
# abaixo.

class Ex01:
    def __init__(self, janelaPrincipal=None):
        self.janela = tk.Toplevel(janelaPrincipal) if janelaPrincipal else tk.Tk()
        self.janela.geometry("1500x900")
        self.janela.minsize(800, 700)
        self.janela.title("Exercício 01")
        self.janela.configure(bg="#bdbfcf")


        def exibir():
            texto.config(text=f"Você digitou:\n\n{escrita.get()}")


        """Frame Enunciado"""

        frame_enunciado = tk.Frame(
            self.janela,
            width=600,
            height=200,
            highlightbackground="black",
            highlightthickness=3
        )
        frame_enunciado.pack_propagate(False)
        frame_enunciado.pack(pady=20)

        enunciado = tk.Text(frame_enunciado, wrap="word", font=("Arial", 10))
        enunciado.insert(
            "1.0",
            "\n Exercício 01\n\n"
            "   Crie uma janela com dois frames:\n\n"
            "   Um frame para informações pessoais (campos: Nome e Idade)\n\n"
            "   Um frame com um botão Exibir que, ao ser clicado, mostra os dados em um Label abaixo"
        )
        enunciado.pack(fill="both")
        enunciado.config(state="disabled")


        """Frame 1"""

        frame1 = tk.Frame(self.janela, Estilos01.estiloFrame())
        frame1.pack_propagate(False)
        frame1.pack(pady=20)

        tk.Label(
            frame1,
            Estilos01.estiloLabel(),
            text="Digite algo:"
        ).pack(side="left", padx=15)

        escrita = tk.Entry(frame1, Estilos01.estiloEntry(), width=40)
        escrita.pack(side="left", padx=15)


        """Frame 2"""

        frame2 = tk.Frame(self.janela, Estilos01.estiloFrame(), height=250)
        frame2.pack_propagate(False)
        frame2.pack(pady=20)

        botao = tk.Button(
            frame2,
            text="Exibir Texto Escrito",
            command=exibir,
            **Estilos01.estiloBotao()
        )
        botao.pack(pady=15)

        texto = tk.Label(
            frame2,
            **Estilos01.estiloLabel(),
            wraplength=400,
            text="",
            justify="left"
        )
        texto.pack(pady=5)



    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()

exe = Ex01()
exe.iniciar()