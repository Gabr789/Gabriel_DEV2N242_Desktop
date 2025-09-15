import tkinter as tk
from tkinter import scrolledtext, messagebox
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

class TelaAtalhosTeclado:
    def __init__(self, master=None):
        self.janela = tk.Toplevel(master) if master else tk.Tk()
        self.janela.title("Atalhos de Teclado")
        self.janela.geometry("600x500")
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            self.janela.iconbitmap(caminho_icone)

       
        titulo = tk.Label(
            self.janela,
            text="Como funcionam os atalhos de teclado",
            font=("Arial", 14, "bold")
        )
        titulo.pack(pady=10)

        texto_explicativo = (
            "Você pode usar o método bind() para capturar atalhos de teclado e associá-los\n"
            "a ações específicas da sua aplicação. Isso torna a interface mais fluida e\n"
            "profissional, permitindo que o usuário execute comandos com rapidez.\n\n"

            "Alguns atalhos comuns incluem:\n"
            "- <Control-s>: Ctrl + S = Salvar dados\n"
            "- <Control-c>: Ctrl + C = Cancelar, limpar campos ou copiar texto\n"
            "- <Control-v>: Ctrl + V = Colar conteúdo\n"
            "- <Control-x>: Ctrl + X = Recortar conteúdo\n"
            "- <Control-z>: Ctrl + Z = Desfazer a última ação\n"
            "- <Control-y>: Ctrl + Y = Refazer a ação desfeita\n"
            "- <Control-a>: Ctrl + A = Selecionar todo o conteúdo\n"
            "- <Control-n>: Ctrl + N = Novo formulário ou novo documento\n"
            "- <Control-o>: Ctrl + O = Abrir um arquivo ou conteúdo\n"
            "- <Control-p>: Ctrl + P = Imprimir\n"
            "- <Return>: Enter = Confirmar ação ou enviar formulário\n"
            "- <Escape>: Esc = Fechar janela, cancelar ou sair\n"
            "- <Tab>: Tab = Navegar entre campos de formulário\n"
            "- <F1>: Ajuda ou suporte\n"
            "- <F5>: Atualizar a janela ou reiniciar a visualização\n\n"

            "Sintaxe:\n"
            "widget.bind('<Control-s>', funcao_salvar)\n"
            

            "Vantagens do uso de atalhos:\n"
            "- Agiliza o uso para usuários frequentes\n"
            "- Reduz a dependência do mouse\n"
            "- Torna a aplicação mais acessível e profissional\n\n"
            "Sintaxe:\n"
            "widget.bind('<Control-s>', funcao_salvar)\n\n"
            "Você pode associar funções úteis a esses atalhos.\n"
            "Exemplo prático abaixo: preencha e use os atalhos:\n"
            "- Ctrl+S → salvar\n"
            "- Ctrl+C → limpar\n"
            "- Esc → sair"
        )

        area_texto = scrolledtext.ScrolledText(
            self.janela, wrap=tk.WORD, width=70, height=8, font=("Arial", 10)
        )
        area_texto.insert(tk.INSERT, texto_explicativo)
        area_texto.config(state='disabled')
        area_texto.pack(padx=10, pady=5)

   
        frame_form = tk.Frame(self.janela)
        frame_form.pack(pady=15)

        tk.Label(frame_form, text="Nome:", font=("Arial", 11)).grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.entry_nome = tk.Entry(frame_form, font=("Arial", 11), width=40)
        self.entry_nome.grid(row=0, column=1, pady=5)

        tk.Label(frame_form, text="Email:", font=("Arial", 11)).grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.entry_email = tk.Entry(frame_form, font=("Arial", 11), width=40)
        self.entry_email.grid(row=1, column=1, pady=5)

      
        self.label_status = tk.Label(self.janela, text="", font=("Arial", 11), fg="green")
        self.label_status.pack(pady=5)

        
        self.janela.bind("<Control-s>", self.salvar)
        self.janela.bind("<Control-c>", self.limpar)
        self.janela.bind("<Escape>", self.sair)

        
        self.entry_nome.focus_set()

    def salvar(self, event=None):
        nome = self.entry_nome.get().strip()
        email = self.entry_email.get().strip()

        if nome and email:
            self.label_status.config(text=f"Salvo: {nome} - {email}", fg="green")
        else:
            self.label_status.config(text="Preencha todos os campos.", fg="red")

    def limpar(self, event=None):
        self.entry_nome.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.label_status.config(text="Campos limpos.", fg="gray")
        self.entry_nome.focus_set()

    def sair(self, event=None):
        if messagebox.askyesno("Sair", "Deseja fechar esta janela?"):
            self.janela.destroy()

    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()


if __name__ == "__main__":
    app = TelaAtalhosTeclado()
    app.iniciar()