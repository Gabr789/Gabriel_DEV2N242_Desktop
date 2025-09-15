import tkinter as tk
from tkinter import scrolledtext
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
class TelaCheckbutton:
    def __init__(self, master=None):
        self.janela = tk.Toplevel()  
        self.janela.title("Checkbutton")
        self.janela.geometry("600x500")
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            self.janela.iconbitmap(caminho_icone)
        titulo = tk.Label(
            self.janela,
            text="Como funcionam os Checkbuttons",
            font=("Arial", 12, "bold")
        )
        titulo.pack(pady=10)

        texto_explicativo = (
            "O que é um Checkbutton?\n"
            "Um Checkbutton (ou caixa de seleção) é um componente gráfico utilizado em interfaces Tkinter\n"
            "para permitir que o usuário marque ou desmarque uma ou mais opções de forma independente.\n"
            "Diferente do Radiobutton (que permite apenas uma escolha), o Checkbutton é ideal quando\n"
            "o usuário pode selecionar múltiplas preferências ou configurações.\n\n"

            "Para mais detalhes, consulte a documentação oficial do Checkbutton no Tkinter:\n"
            "https://docs.python.org/3/library/tkinter.html#tkinter.Checkbutton\n\n"

            "Situações comuns de uso incluem:\n"
            "- Seleção de interesses (ex: Gosta de Python, Java, C++)\n"
            "- Preferências de notificações\n"
            "- Termos de aceite ou concordância\n\n"

            "Como criar um Checkbutton:\n"
            "Crie uma variável de controle (IntVar, BooleanVar, etc.), que armazenará o estado do botão.\n"
            "Crie o botão, passando a variável no parâmetro variable.\n\n"

            "Exemplo básico:\n"
            "import tkinter as tk\n\n"
            "janela = tk.Tk()\n"
            "janela.title(\"Exemplo de Checkbutton\")\n\n"
            "interesse = tk.IntVar()\n"
            "chk = tk.Checkbutton(janela, text=\"Gosta de Python\", variable=interesse)\n"
            "chk.pack()\n\n"
            "janela.mainloop()\n\n"

            "Principais atributos do Checkbutton:\n"
            "- text: texto exibido ao lado da caixa de seleção\n"
            "- variable: variável associada ao estado (marcado/desmarcado)\n"
            "- onvalue: valor atribuído à variável quando o botão está marcado (padrão: 1)\n"
            "- offvalue: valor atribuído quando está desmarcado (padrão: 0)\n"
            "- command: função chamada sempre que o estado do botão mudar\n\n"

            "Exemplo com função associada:\n"
            "def mostrar():\n"
            "    if interesse.get():\n"
            "        print(\"Gosta de Python\")\n"
            "    else:\n"
            "        print(\"Não selecionado\")\n\n"
            "interesse = tk.IntVar()\n"
            "chk = tk.Checkbutton(janela, text=\"Gosta de Python\", variable=interesse, command=mostrar)\n"
            "chk.pack()\n"
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

        frame_botoes = tk.Frame(self.janela)
        frame_botoes.pack(pady=10)

        botao_intvar = tk.Button(
            frame_botoes,
            text="Executar Exemplo IntVar",
            command=self.executar_exemplo_intvar,
            width=20
        )
        botao_intvar.grid(row=0, column=0, padx=10)

        botao_booleanvar = tk.Button(
            frame_botoes,
            text="Executar Exemplo BooleanVar",
            command=self.executar_exemplo_booleanvar,
            width=30
        )
        botao_booleanvar.grid(row=0, column=1, padx=10)
        
        botao_anchors = tk.Button(
            frame_botoes,
            text="Exemplo Anchors",
            command=self.exemplo_anchors,
            width=20
        )
        botao_anchors.grid(row=0, column=2, padx=10)
    def executar_exemplo_intvar(self):
        nova_janela = tk.Toplevel(self.janela)
        nova_janela.title("Exemplo Checkbutton - IntVar")
        nova_janela.geometry("300x250")
        nova_janela.configure(bg="#f0f0f0")
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            nova_janela.iconbitmap(caminho_icone)

        self.gosta_python = tk.IntVar()
        self.gosta_java = tk.IntVar()

        tk.Label(nova_janela, text="Quais tecnologias você gosta?", bg="#f0f0f0", font=("Arial", 11)).pack(pady=10)

        tk.Checkbutton(nova_janela, text="Python", variable=self.gosta_python, bg="#f0f0f0").pack(anchor="w")
        tk.Checkbutton(nova_janela, text="Java", variable=self.gosta_java, bg="#f0f0f0").pack(anchor="w")

        resultado = tk.Label(nova_janela, text="", bg="#f0f0f0", font=("Arial", 11), fg="blue")
        resultado.pack(pady=10)

        def verificar():
            escolhas = []
            if self.gosta_python.get() == 1:
                escolhas.append("Python")
            if self.gosta_java.get() == 1:
                escolhas.append("Java")

            if escolhas:
                resultado.config(text="Você gosta de: " + ", ".join(escolhas))
            else:
                resultado.config(text="Nenhuma opção marcada.")

        tk.Button(nova_janela, text="Confirmar", command=verificar).pack(pady=5)

    def executar_exemplo_booleanvar(self):
        nova_janela = tk.Toplevel(self.janela)
        nova_janela.title("Exemplo Checkbutton - BooleanVar")
        nova_janela.geometry("300x250")
        nova_janela.configure(bg="#f0f0f0")
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            nova_janela.iconbitmap(caminho_icone)

        self.gosta_js = tk.BooleanVar()
        self.gosta_csharp = tk.BooleanVar()

        tk.Label(nova_janela, text="Quais tecnologias você gosta?", bg="#f0f0f0", font=("Arial", 11)).pack(pady=10)

        tk.Checkbutton(nova_janela, text="JavaScript", variable=self.gosta_js, bg="#f0f0f0").pack(anchor="w")
        tk.Checkbutton(nova_janela, text="C#", variable=self.gosta_csharp, bg="#f0f0f0").pack(anchor="w")

        resultado = tk.Label(nova_janela, text="", bg="#f0f0f0", font=("Arial", 11), fg="green")
        resultado.pack(pady=10)

        def verificar():
            escolhas = []
            if self.gosta_js.get():
                escolhas.append("JavaScript")
            if self.gosta_csharp.get():
                escolhas.append("C#")

            if escolhas:
                resultado.config(text="Você gosta de: " + ", ".join(escolhas))
            else:
                resultado.config(text="Nenhuma opção marcada.")

        tk.Button(nova_janela, text="Confirmar", command=verificar).pack(pady=5)

    def exemplo_anchors(self):
        nova_janela = tk.Toplevel(self.janela)
        nova_janela.title("Visualizando Anchors com place()")
        nova_janela.geometry("400x400")
        nova_janela.configure(bg="#f9f9f9")
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            nova_janela.iconbitmap(caminho_icone)

        tk.Label(nova_janela, text="Checkbuttons posicionados com place() e diferentes anchors:", 
                font=("Arial", 12, "bold"), bg="#f9f9f9").pack(pady=10)

        anchors = [
            "n", "ne", "e", "se", "s", "sw", "w", "nw", "center"
        ]

        vars_anchors = {}
        positions = {
            "n":     (0.5, 0.05),
            "ne":    (0.95, 0.05),
            "e":     (0.95, 0.5),
            "se":    (0.95, 0.95),
            "s":     (0.5, 0.95),
            "sw":    (0.05, 0.95),
            "w":     (0.05, 0.5),
            "nw":    (0.05, 0.05),
            "center":(0.5, 0.5)
        }

       
        frame_chk = tk.Frame(nova_janela, bg="#f9f9f9", width=380, height=300)
        frame_chk.pack(pady=10, fill='both', expand=True)

        for anchor in anchors:
            var = tk.IntVar()
            vars_anchors[anchor] = var
            chk = tk.Checkbutton(
                frame_chk, text=anchor.upper(),
                variable=var,
                bg="#f9f9f9"
            )
           
            chk.place(relx=positions[anchor][0], rely=positions[anchor][1], anchor=anchor)

       
        frame_baixo = tk.Frame(nova_janela, bg="#f9f9f9")
        frame_baixo.pack(pady=5)

        resultado = tk.Label(frame_baixo, text="", font=("Arial", 11), bg="#f9f9f9", fg="blue")
        resultado.pack(pady=5)

        def verificar():
            selecionados = [anc.upper() for anc, var in vars_anchors.items() if var.get() == 1]
            if selecionados:
                texto = "Anchors selecionados: " + ", ".join(selecionados)
            else:
                texto = "Nenhum anchor selecionado."
            resultado.config(text=texto)

        tk.Button(frame_baixo, text="Verificar", command=verificar).pack(pady=5)

    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()