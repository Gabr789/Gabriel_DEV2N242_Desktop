import tkinter as tk
from tkinter import scrolledtext
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

class TelaEventoMotion:
    def __init__(self, master=None):
        self.janela = tk.Toplevel(master) if master else tk.Tk()
        self.janela.title("Evento de Movimento do Mouse")
        self.janela.geometry("600x600")
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            self.janela.iconbitmap(caminho_icone)

   
        titulo = tk.Label(
            self.janela,
            text="Como funciona o evento de movimento",
            font=("Arial", 14, "bold")
        )
        titulo.pack(pady=10)


        texto_explicativo = (
            "O evento <Motion> é acionado sempre que o mouse se move dentro de um widget.\n\n"
            "Sintaxe:\n"
            "widget.bind('<Motion>', funcao)\n\n"
            "A função associada deve receber um parâmetro (evento), e você pode acessar:\n"
            "- event.x / event.y: coordenadas do mouse dentro do widget\n"
            "- event.x_root / event.y_root: coordenadas absolutas na tela\n\n"
            "Exemplo prático abaixo: mova o mouse na área azul para ver as coordenadas atualizadas em tempo real."
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


        self.area_mouse = tk.Frame(self.janela, bg="#e0f7fa", width=500, height=250, relief=tk.RIDGE, bd=2)
        self.area_mouse.pack(pady=10)
        self.area_mouse.pack_propagate(False)

        self.label_coordenadas = tk.Label(self.area_mouse, text="Mova o mouse aqui", bg="#e0f7fa", font=("Arial", 11))
        self.label_coordenadas.place(relx=0.5, rely=0.5, anchor="center")

        self.area_mouse.bind("<Motion>", self.exibir_coordenadas)

   
        botao_exemplo = tk.Button(self.janela, text="Abrir Exemplo do Dia a Dia", command=self.abrir_exemplo_pratico)
        botao_exemplo.pack(pady=10)

    def exibir_coordenadas(self, event):
        x, y = event.x, event.y
        self.label_coordenadas.config(text=f"Coordenadas do mouse: x={x}, y={y}")

    def abrir_exemplo_pratico(self):
        ExemploMotionForm(self.janela).iniciar()

    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()


class ExemploMotionForm:
    def __init__(self, master=None):
        self.janela = tk.Toplevel(master) if master else tk.Tk()
        self.janela.title("Destaque ao Passar o Mouse")
        self.janela.geometry("400x250")
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            self.janela.iconbitmap(caminho_icone)

        titulo = tk.Label(
            self.janela,
            text="Simulação de Destaque do mouse",
            font=("Arial", 13, "bold")
        )
        titulo.pack(pady=10)

        self.frame_form = tk.Frame(self.janela)
        self.frame_form.pack(pady=20)

  
        tk.Label(self.frame_form, text="Nome:", font=("Arial", 11)).grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.entry_nome = tk.Entry(self.frame_form, font=("Arial", 11), width=25)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5)


        tk.Label(self.frame_form, text="Email:", font=("Arial", 11)).grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.entry_email = tk.Entry(self.frame_form, font=("Arial", 11), width=25)
        self.entry_email.grid(row=1, column=1, padx=5, pady=5)

      
        self.entry_nome.bind("<Enter>", lambda e: self.highlight(e.widget))
        self.entry_nome.bind("<Leave>", lambda e: self.remove_highlight(e.widget))
        self.entry_email.bind("<Enter>", lambda e: self.highlight(e.widget))
        self.entry_email.bind("<Leave>", lambda e: self.remove_highlight(e.widget))

    def highlight(self, widget):
        widget.config(bg="#d0f0c0")  # verde claro

    def remove_highlight(self, widget):
        widget.config(bg="white")

    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()


if __name__ == "__main__":
    app = TelaEventoMotion()
    app.iniciar()