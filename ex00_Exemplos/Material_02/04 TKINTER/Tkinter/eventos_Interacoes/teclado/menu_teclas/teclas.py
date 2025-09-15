import tkinter as tk
from tkinter import scrolledtext
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from .login_enter import TelaLoginEnter
class TelaEventoTecla:
    def __init__(self, master=None):
        self.janela = tk.Toplevel(master) if master else tk.Tk()
        self.janela.title("Evento de Teclado")
        self.janela.geometry("600x450")
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            self.janela.iconbitmap(caminho_icone)

       
        titulo = tk.Label(
            self.janela,
            text="Como funciona os eventos ",
            font=("Arial", 14, "bold")
        )
        titulo.pack(pady=10)

        texto_explicativo = (
            "O método bind() pode capturar eventos de teclado.\n"
            "O evento <Key> é acionado sempre que uma tecla é pressionada.\n\n"
            "Sintaxe:\n"
            "widget.bind('<Key>', funcao)\n\n"
            "A função associada deve receber um parâmetro (evento).\n"
            "Você pode acessar:\n"
            "- event.char: caractere digitado\n"
            "- event.keysym: nome simbólico da tecla\n"
            "- event.keycode: código numérico da tecla\n\n"
            "Exemplo prático abaixo: digite algo na área azul e veja as teclas registradas."
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

      
        self.area_digito = tk.Text(self.janela, bg="#d0e7ff", width=70, height=8, font=("Arial", 11))
        self.area_digito.pack(pady=10)
        self.area_digito.focus_set()  
        self.area_digito.bind("<Key>", self.exibir_tecla)

        self.label_resultado = tk.Label(self.janela, text="Pressione qualquer tecla...", font=("Arial", 11))
        self.label_resultado.pack(pady=5)
        botao_exemplo = tk.Button(
            self.janela,
            text="Ver exemplo prático Login com Enter",
            font=("Arial", 11),
            command=self.abrir_exemplo_login
        )
        botao_exemplo.pack(pady=15)
    def exibir_tecla(self, event):
        char = event.char if event.char.strip() != "" else "[tecla especial]"
        tecla = event.keysym
        codigo = event.keycode
        self.label_resultado.config(
            text=f"Tecla pressionada: {char}  |  keysym: {tecla}  |  keycode: {codigo}"
        )


    def abrir_exemplo_login(self):
        TelaLoginEnter(self.janela).iniciar()
    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()

if __name__ == "__main__":
    app = TelaEventoTecla()
    app.iniciar()