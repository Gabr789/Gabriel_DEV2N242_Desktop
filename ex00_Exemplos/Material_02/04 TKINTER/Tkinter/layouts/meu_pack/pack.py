import tkinter as tk
from tkinter import scrolledtext
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

class TelaPack:
    def __init__(self, master=None):
        self.janela = tk.Toplevel(master) if master else tk.Tk()
        self.janela.title("Exemplo de Layout Pack")
        self.janela.geometry("600x450")
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../logo.ico")
        if os.path.exists(caminho_icone):
            self.janela.iconbitmap(caminho_icone)

        
        titulo = tk.Label(
            self.janela,
            text="Como funciona o layout pack",
            font=("Arial", 14, "bold")
        )
        titulo.pack(pady=10)


        texto_explicativo = (
            "O layout pack organiza os widgets empilhando-os em uma direção específica, "
            "de forma vertical ou horizontal, facilitando a criação de interfaces simples e lineares.\n\n"

            "Funcionamento básico:\n"
            "O gerenciador pack posiciona widgets um após o outro, respeitando a ordem em que são adicionados ao contêiner, "
            "e distribui o espaço disponível conforme parâmetros que definem alinhamento, preenchimento e expansão.\n\n"

            "Principais parâmetros e suas funções:\n"
            "- side: determina o lado do contêiner onde o widget será empilhado. Pode ser 'top' (padrão), 'bottom', 'left' ou 'right'. "
            "Isso controla se a pilha cresce para baixo, cima, direita ou esquerda.\n"
            "- fill: especifica como o widget deve preencher o espaço disponível. Pode ser 'x' (preenche horizontalmente), 'y' (verticalmente), "
            "'both' (em ambas as direções) ou 'none' (não preenche além do tamanho natural do widget).\n"
            "- expand: um valor booleano que indica se o widget deve expandir para ocupar espaço extra no contêiner, "
            "permitindo que a interface se adapte melhor ao redimensionamento.\n\n"

            "Vantagens do gerenciador pack:\n"
            "- Muito simples e rápido de usar, ideal para layouts lineares e hierárquicos.\n"
            "- Automatiza o posicionamento sequencial, poupando o desenvolvedor de cálculos manuais de coordenadas.\n"
            "- Pode ser combinado com múltiplos frames (subcontêineres) para criar layouts mais complexos, segmentando a interface em áreas controláveis.\n\n"

            "Limitações e considerações:\n"
            "- Não é ideal para layouts altamente complexos que exigem posicionamento em grade ou absoluto.\n"
            "- O controle detalhado sobre o alinhamento e sobreposição é limitado comparado aos layouts grid e place.\n"
            "- Pode exigir o uso conjunto com outros gerenciadores para criar interfaces mais flexíveis e responsivas.\n\n"

            "Exemplo prático:\n"
            "- pack(side='top', fill='x', expand=True) posiciona o widget no topo do contêiner, fazendo-o expandir horizontalmente e ocupar o espaço extra disponível.\n"
            "- pack(side='left', fill='y') empilha widgets da esquerda para a direita, preenchendo verticalmente o espaço disponível.\n\n"

            "Para interfaces simples e empilhamento rápido de widgets, pack é uma excelente escolha, "
            "especialmente quando combinado com frames para segmentar e organizar o layout.\n\n"

            "Para mais detalhes, consulte a documentação oficial do Tkinter Pack Geometry Manager:\n"
            "https://docs.python.org/3/library/tkinter.html#the-pack-geometry-manager\n"
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

      
        frame_exemplo = tk.Frame(self.janela)
        frame_exemplo.pack(pady=10, fill=tk.BOTH, expand=True)

      
        tk.Label(frame_exemplo, text="Nome:", font=("Arial", 11)).pack(anchor='w', padx=5, pady=5)
        self.entry_nome = tk.Entry(frame_exemplo, font=("Arial", 11))
        self.entry_nome.pack(fill=tk.X, padx=5, pady=5)

        tk.Label(frame_exemplo, text="Sobrenome:", font=("Arial", 11)).pack(anchor='w', padx=5, pady=5)
        self.entry_sobrenome = tk.Entry(frame_exemplo, font=("Arial", 11))
        self.entry_sobrenome.pack(fill=tk.X, padx=5, pady=5)

       
        frame_botoes = tk.Frame(frame_exemplo)
        frame_botoes.pack(pady=15, fill=tk.X)

        btn_ok = tk.Button(frame_botoes, text="OK", command=self.mostrar_nome_completo)
        btn_ok.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=10)

        btn_limpar = tk.Button(frame_botoes, text="Limpar", command=self.limpar_campos)
        btn_limpar.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=10)

       
        self.label_resultado = tk.Label(frame_exemplo, text="", font=("Arial", 11), fg="green")
        self.label_resultado.pack(pady=10)

    def mostrar_nome_completo(self):
        nome = self.entry_nome.get().strip()
        sobrenome = self.entry_sobrenome.get().strip()
        if nome and sobrenome:
            self.label_resultado.config(text=f"Nome completo: {nome} {sobrenome}", fg="green")
        else:
            self.label_resultado.config(text="Por favor, preencha nome e sobrenome.", fg="red")

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_sobrenome.delete(0, tk.END)
        self.label_resultado.config(text="", fg="green")

    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()


if __name__ == "__main__":
    app = TelaPack()
    app.iniciar()