import tkinter as tk
from tkinter import scrolledtext
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

class TelaEventoClick:
    def __init__(self, master=None):
        self.janela = tk.Toplevel(master) if master else tk.Tk()
        self.janela.title("Evento de Clique")
        self.janela.geometry("600x450")
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            self.janela.iconbitmap(caminho_icone)


        titulo = tk.Label(
            self.janela,
            text="Como funciona o evento de clique",
            font=("Arial", 14, "bold")
        )
        titulo.pack(pady=10)

        texto_explicativo = (
            "O método bind() permite associar eventos a widgets.\n"
            "O evento <Button-1> representa um clique do botão esquerdo do mouse.\n\n"
            "Sintaxe:\n"
            "widget.bind('<Button-1>', funcao)\n\n"
            "A função chamada deve receber um parâmetro (objeto de evento).\n"
            "Você pode usar atributos como:\n"
            "- event.x / event.y: coordenadas do clique dentro do widget\n"
            "- event.widget: widget que recebeu o clique\n\n"
            "Exemplo prático abaixo: clique dentro da área azul para ver onde clicou."
        )

        area_texto = scrolledtext.ScrolledText(
            self.janela,
            wrap=tk.WORD,
            width=70,
            height=8,
            font=("Arial", 10)
        )
        area_texto.insert(tk.INSERT, texto_explicativo)
        area_texto.config(state='disabled')
        area_texto.pack(padx=10, pady=5)

        
        self.area_clique = tk.Frame(self.janela, bg="#d0e7ff", width=500, height=250, relief=tk.RIDGE, bd=2)
        self.area_clique.pack(pady=10)
        self.area_clique.pack_propagate(False)

      
        self.label_resultado = tk.Label(self.area_clique, text="Clique aqui com o mouse", bg="#d0e7ff", font=("Arial", 11))
        self.label_resultado.place(relx=0.5, rely=0.5, anchor="center")

        self.area_clique.bind("<Button-1>", self.exibir_coordenadas)

    def exibir_coordenadas(self, event):
        x, y = event.x, event.y
        self.label_resultado.config(text=f"Você clicou em: x={x}, y={y}")

    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()

if __name__ == "__main__":
    app = TelaEventoClick()
    app.iniciar()