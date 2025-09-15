import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

class TelaRadiobutton:
    def __init__(self, master=None):
        self.janela = tk.Toplevel()
        self.janela.title("Radiobutton")
        self.janela.geometry("600x500")
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            self.janela.iconbitmap(caminho_icone)
        titulo = tk.Label(
            self.janela,
            text="Como funcionam os Radiobuttons",
            font=("Arial", 12, "bold"),
        )
        titulo.pack(pady=10)

        texto_explicativo = (
            "O que é um Radiobutton?\n"
            "Um Radiobutton (ou botão de opção) é um componente gráfico utilizado em interfaces de usuário\n"
            "para permitir que o usuário selecione apenas uma entre várias opções disponíveis.\n"
            "Quando uma opção é selecionada, as demais são automaticamente desmarcadas.\n"
            "Esse comportamento é ideal para situações em que é necessário escolher apenas uma alternativa,\n"
            "como por exemplo: sexo, forma de pagamento, ou nível de dificuldade de um jogo.\n\n"
            
            "Para mais detalhes, consulte a documentação oficial do Radiobutton no Tkinter:\n"
            "https://docs.python.org/3/library/tkinter.html#tkinter.Radiobutton\n\n"
            
            "Como criar Radiobuttons no Tkinter (Python):\n"
            "Primeiro, crie uma instância de StringVar() ou IntVar() que servirá como variável de controle.\n"
            "Essa variável armazenará o valor da opção selecionada.\n"
            "Em seguida, crie os botões do tipo Radiobutton, associando todos à mesma variável de controle,\n"
            "mas com valores diferentes. Assim, ao selecionar um botão, o valor da variável será atualizado automaticamente.\n\n"
            
            "Exemplo de código:\n"
            "import tkinter as tk\n\n"
            "janela = tk.Tk()\n"
            "janela.title(\"Exemplo de Radiobutton\")\n\n"
            "var = tk.StringVar(value=\"1\")  # Valor inicial pode ser definido aqui\n\n"
            "rb1 = tk.Radiobutton(janela, text=\"Opção 1\", variable=var, value=\"1\")\n"
            "rb2 = tk.Radiobutton(janela, text=\"Opção 2\", variable=var, value=\"2\")\n"
            "rb3 = tk.Radiobutton(janela, text=\"Opção 3\", variable=var, value=\"3\")\n\n"
            "rb1.pack()\n"
            "rb2.pack()\n"
            "rb3.pack()\n\n"
            "janela.mainloop()\n\n"
            
        )

        area_texto = scrolledtext.ScrolledText(
            self.janela,
            wrap=tk.WORD,
            width=70,
            height=20,
            font=("Arial", 10)
        )
        area_texto.insert(tk.INSERT, texto_explicativo)
        area_texto.config(state='disabled')
        area_texto.pack(padx=10, pady=10)

        botao_executar = tk.Button(
            self.janela,
            text="Executar Exemplo StringVar",
            command=self.executar_exemplo
        )
        botao_executar.pack(pady=5)

        botao_intvar = tk.Button(
            self.janela,
            text="Abrir exemplo IntVar",
            command=self.exemplo_intvar
        )
        botao_intvar.pack(pady=5)

    def executar_exemplo(self):
        nova_janela = tk.Toplevel(self.janela)
        nova_janela.title("Exemplo de Radiobutton")
        nova_janela.geometry("300x230")
        nova_janela.configure(bg="#f0f0f0")
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            nova_janela.iconbitmap(caminho_icone)

        genero = tk.StringVar(value="__nada__")

        tk.Label(
            nova_janela,
            text="Selecione seu gênero:",
            font=("Arial", 11),
            bg="#f0f0f0"
        ).pack(pady=10)

        tk.Radiobutton(nova_janela, text="Masculino", variable=genero, value="Masculino", bg="#f0f0f0").pack(anchor="w")
        tk.Radiobutton(nova_janela, text="Feminino", variable=genero, value="Feminino", bg="#f0f0f0").pack(anchor="w")
        tk.Radiobutton(nova_janela, text="Outro", variable=genero, value="Outro", bg="#f0f0f0").pack(anchor="w")

        resultado = tk.Label(nova_janela, text="", bg="#f0f0f0", font=("Arial", 11), fg="blue")
        resultado.pack(pady=10)

        def mostrar_genero():
            valor = genero.get()
            if valor == "__nada__":
                messagebox.showerror("Erro", "Você deve selecionar uma opção!", parent=nova_janela)
            else:
                resultado.config(text=f"Gênero selecionado: {valor}")

        tk.Button(nova_janela, text="Confirmar", command=mostrar_genero).pack(pady=5)

    def exemplo_intvar(self):
        nova_janela = tk.Toplevel(self.janela)
        nova_janela.title("Exemplo de Radiobutton com IntVar")
        nova_janela.geometry("300x230")
        nova_janela.configure(bg="#f0f0f0")
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            nova_janela.iconbitmap(caminho_icone)
        escolha = tk.IntVar(value=0)

        tk.Label(
            nova_janela,
            text="Escolha um número:",
            font=("Arial", 11),
            bg="#f0f0f0"
        ).pack(pady=10)

        tk.Radiobutton(nova_janela, text="Um", variable=escolha, value=1, bg="#f0f0f0").pack(anchor="w")
        tk.Radiobutton(nova_janela, text="Dois", variable=escolha, value=2, bg="#f0f0f0").pack(anchor="w")
        tk.Radiobutton(nova_janela, text="Três", variable=escolha, value=3, bg="#f0f0f0").pack(anchor="w")

        resultado = tk.Label(nova_janela, text="", bg="#f0f0f0", font=("Arial", 11), fg="green")
        resultado.pack(pady=10)

        def mostrar_escolha():
            valor = escolha.get()
            if valor == 0:
                messagebox.showerror("Erro", "Você deve selecionar uma opção!", parent=nova_janela)
            else:
                resultado.config(text=f"Número selecionado: {valor}")

        tk.Button(nova_janela, text="Confirmar", command=mostrar_escolha).pack(pady=5)

    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()

if __name__ == "__main__":
    app = TelaRadiobutton()
    app.iniciar()