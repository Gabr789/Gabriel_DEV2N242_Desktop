import tkinter as tk
from tkinter import scrolledtext
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

class TelaGrid:
    def __init__(self, master=None):
        self.janela = tk.Toplevel(master) if master else tk.Tk()
        self.janela.title("Exemplo de Grid Layout")
        self.janela.geometry("600x450")
       
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../logo.ico")
        if os.path.exists(caminho_icone):
            self.janela.iconbitmap(caminho_icone)

       
        titulo = tk.Label(
            self.janela,
            text="Como funciona o layout Grid",
            font=("Arial", 14, "bold")
        )
        titulo.pack(pady=10)

        
        texto_explicativo = (
            "O layout grid organiza os widgets em uma grade formada por linhas (rows) e colunas (columns).\n"
            "Cada widget é posicionado em uma célula específica da grade, mas pode também ocupar\n"
            "mais de uma célula horizontalmente ou verticalmente, usando os parâmetros columnspan e rowspan.\n\n"

            "Cada linha e coluna na grade é numerada a partir de zero (0). O parâmetro 'row' define a linha, e 'column' define a coluna onde o widget será colocado.\n"
            "Por exemplo, grid(row=0, column=0) posiciona o widget na primeira linha e primeira coluna.\n"
            "Um widget fica dentro da célula formada pelo cruzamento dessas linhas e colunas.\n"
            "Com 'columnspan' e 'rowspan', o widget pode ocupar múltiplas colunas ou linhas, útil para widgets maiores.\n"
            "O parâmetro 'sticky' define o alinhamento do widget dentro da célula: 'N' (topo), 'S' (base), 'E' (direita), 'W' (esquerda), ou combinações como 'NSEW' para preencher toda a célula.\n\n"

            "Principais vantagens do grid:\n"
            "- Alinhamento preciso e consistente em linhas e colunas, facilitando a organização visual.\n"
            "- Permite construir layouts complexos, com widgets de diferentes tamanhos e formatos.\n"
            "- Excelente controle do redimensionamento da janela através do ajuste de pesos das linhas e colunas.\n\n"

            "Métodos e parâmetros importantes:\n"
            "- grid(row=x, column=y): define a célula exata onde o widget será colocado.\n"
            "- columnspan=N / rowspan=N: fazem o widget ocupar N colunas ou linhas, respectivamente,\n"
            "  ideal para botões ou áreas maiores.\n"
            "- sticky: alinha o widget dentro da célula (N=topo, S=baixo, E=direita, W=esquerda).\n"
            "  Você pode combinar valores, ex: sticky='NSEW' faz o widget expandir e preencher a célula.\n"
            "- rowconfigure / columnconfigure: permite definir o peso das linhas e colunas,\n"
            "  controlando como elas crescem ou encolhem quando a janela é redimensionada.\n"
            "  Pesos maiores indicam que aquela linha/coluna deve expandir mais.\n\n"

            "Exemplo prático (abaixo):\n"
            "- Labels 'Nome' e 'Sobrenome' estão na coluna 0, alinhadas à direita (sticky='e').\n"
            "- Campos Entry para entrada de dados estão na coluna 1, com expansão horizontal (sticky='we').\n"
            "- Botões 'OK' e 'Limpar' ocupam a linha 2, colunas 0 e 1, com sticky='we' para expandir horizontalmente.\n"
            "- O label de resultado ocupa a linha 3, colunas 0 e 1, usando columnspan=2 para expandir pelas duas colunas.\n"
            "- Configuramos pesos das colunas para que a segunda coluna (com os Entries) cresça mais quando a janela for redimensionada.\n\n"

            "Para mais detalhes, consulte a documentação oficial do Tkinter Grid Geometry Manager:\n"
            "https://docs.python.org/3/library/tkinter.html#the-grid-geometry-manager\n"
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

      
        tk.Label(frame_exemplo, text="Nome:", font=("Arial", 11)).grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.entry_nome = tk.Entry(frame_exemplo, font=("Arial", 11))
        self.entry_nome.grid(row=0, column=1, sticky="we", padx=5, pady=5)

        tk.Label(frame_exemplo, text="Sobrenome:", font=("Arial", 11)).grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.entry_sobrenome = tk.Entry(frame_exemplo, font=("Arial", 11))
        self.entry_sobrenome.grid(row=1, column=1, sticky="we", padx=5, pady=5)

      
        btn_ok = tk.Button(frame_exemplo, text="OK", command=self.mostrar_nome_completo)
        btn_ok.grid(row=2, column=0, padx=5, pady=15, sticky="we")

        btn_limpar = tk.Button(frame_exemplo, text="Limpar", command=self.limpar_campos)
        btn_limpar.grid(row=2, column=1, padx=5, pady=15, sticky="we")

    
        self.label_resultado = tk.Label(frame_exemplo, text="", font=("Arial", 11), fg="green")
        self.label_resultado.grid(row=3, column=0, columnspan=2, pady=10)

       
        frame_exemplo.columnconfigure(0, weight=1)
        frame_exemplo.columnconfigure(1, weight=2)

    def mostrar_nome_completo(self):
        nome = self.entry_nome.get().strip()
        sobrenome = self.entry_sobrenome.get().strip()
        if nome and sobrenome:
            self.label_resultado.config(text=f"Nome completo: {nome} {sobrenome}")
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
    app = TelaGrid()
    app.iniciar()





