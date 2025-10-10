import tkinter as tk
from tkinter import scrolledtext
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

class TelaEventoEnterLeave:
    def __init__(self, master=None):
        self.janela = tk.Toplevel(master) if master else tk.Tk()
        self.janela.title("Eventos de Entrada e Saída")
        self.janela.geometry("600x500")
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            self.janela.iconbitmap(caminho_icone)

    
        titulo = tk.Label(
            self.janela,
            text="Como funcionam os eventos",
            font=("Arial", 14, "bold")
        )
        titulo.pack(pady=10)

        # Texto explicativo
        texto_explicativo = (
            "Os eventos <Enter> e <Leave> são acionados quando o mouse entra ou sai de um widget.\n\n"
            "Sintaxe:\n"
            "widget.bind('<Enter>', funcao_entrada)\n"
            "widget.bind('<Leave>', funcao_saida)\n\n"
            "Esses eventos são úteis para:\n"
            "- Destacar botões quando o mouse passa por cima\n"
            "- Criar efeitos visuais\n"
            "- Guiar o usuário em campos de formulário\n\n"
            "Área azul abaixo muda de cor ao entrar e sair com o mouse."
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

   
        self.area_mouse = tk.Frame(self.janela, bg="#e0f7fa", width=500, height=200, relief=tk.RIDGE, bd=2)
        self.area_mouse.pack(pady=10)
        self.area_mouse.pack_propagate(False)

        self.label_destaque = tk.Label(self.area_mouse, text="Passe o mouse aqui", bg="#e0f7fa", font=("Arial", 11))
        self.label_destaque.place(relx=0.5, rely=0.5, anchor="center")

        self.area_mouse.bind("<Enter>", self.mouse_entrou)
        self.area_mouse.bind("<Leave>", self.mouse_saiu)

        botao_exemplo = tk.Button(self.janela, text="Abrir Exemplo do Dia a Dia", command=self.abrir_exemplo_pratico)
        botao_exemplo.pack(pady=10)

    def mouse_entrou(self, event):
        self.area_mouse.config(bg="#b2ebf2")
        self.label_destaque.config(text="Mouse entrou na área", bg="#b2ebf2")

    def mouse_saiu(self, event):
        self.area_mouse.config(bg="#e0f7fa")
        self.label_destaque.config(text="Passe o mouse aqui", bg="#e0f7fa")

    def abrir_exemplo_pratico(self):
        ExemploHoverBotao(self.janela).iniciar()

    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()

class ExemploHoverBotao:
    def __init__(self, master=None):
        self.janela = tk.Toplevel(master) if master else tk.Tk()
        self.janela.title("Exemplo de Botões com Destaque ao Passar o Mouse")
        self.janela.geometry("600x200")
        self.janela.resizable(False,False)
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            self.janela.iconbitmap(caminho_icone)

        titulo = tk.Label(
            self.janela,
            text="Passe o mouse sobre os botões abaixo",
            font=("Arial", 12, "bold")
        )
        titulo.pack(pady=10)

        frame_botoes = tk.Frame(self.janela)
        frame_botoes.pack(pady=20)

        for texto in ["Salvar", "Cancelar", "Ajuda"]:
            botao = tk.Button(frame_botoes, text=texto, font=("Arial", 11), width=12)
            botao.pack(side=tk.LEFT, padx=10)

            botao.bind("<Enter>", lambda e, b=botao: b.config(bg="#d0f0c0"))
            botao.bind("<Leave>", lambda e, b=botao: b.config(bg="SystemButtonFace"))

    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()

if __name__ == "__main__":
    app = TelaEventoEnterLeave()
    app.iniciar()