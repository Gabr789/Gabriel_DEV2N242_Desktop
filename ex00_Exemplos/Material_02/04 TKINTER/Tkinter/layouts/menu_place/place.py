import tkinter as tk
from tkinter import scrolledtext
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

class TelaPlace:
    def __init__(self, master=None):
        self.janela = tk.Toplevel(master) if master else tk.Tk()
        self.janela.title("Exemplo de Layout Place")
        self.janela.geometry("600x450")
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../logo.ico")
        if os.path.exists(caminho_icone):
            self.janela.iconbitmap(caminho_icone)

        
        titulo = tk.Label(
            self.janela,
            text="Como funciona o layout place",
            font=("Arial", 14, "bold")
        )
        titulo.pack(pady=10)

       
        texto_explicativo = (
                "O layout place posiciona widgets utilizando coordenadas absolutas ou relativas, "
                "permitindo um controle preciso e minucioso sobre a localização dos elementos na interface gráfica.\n\n"

                "Funcionamento básico:\n"
                "Com o place, você especifica exatamente onde um widget deve aparecer dentro de seu contêiner, "
                "usando valores em pixels ou valores relativos à largura e altura do contêiner pai.\n"
                "Isso é feito por meio dos parâmetros x, y para posicionamento absoluto, e relx, rely para posicionamento relativo.\n\n"

                "Principais parâmetros e suas funções:\n"
                "- x / y: definem a posição absoluta do widget em pixels, tomando como referência o canto superior esquerdo do contêiner.\n"
                "- relx / rely: definem a posição relativa do widget, com valores variando de 0.0 a 1.0, onde 0.0 é o início do eixo e 1.0 é 100% do tamanho do contêiner.\n"
                "- anchor: especifica o ponto de ancoragem do widget em relação à posição definida, permitindo alinhar o widget pelo seu centro ('center'), topo ('n'), esquerda ('w'), direita ('e'), entre outras opções.\n"
                "  Isso facilita posicionamentos mais intuitivos, especialmente quando se trabalha com widgets de tamanhos variados.\n\n"

                "Vantagens do gerenciador place:\n"
                "- Proporciona controle total sobre o posicionamento exato dos widgets, ideal para layouts onde o design precisa ser rigorosamente seguido.\n"
                "- Permite a sobreposição de widgets, algo não diretamente suportado pelos layouts pack e grid.\n"
                "- Útil em interfaces com elementos gráficos que exigem posicionamentos fixos, como jogos, dashboards personalizados e painéis de controle.\n\n"

                "Desvantagens e cuidados:\n"
                "- Não é responsivo por padrão: widgets posicionados com place não se ajustam automaticamente ao redimensionamento da janela, podendo causar sobreposições ou espaços vazios.\n"
                "- Exige mais cuidado e manutenção manual do layout, especialmente em interfaces que precisam se adaptar a diferentes resoluções ou tamanhos de tela.\n\n"

                "Exemplo prático:\n"
                "- place(x=50, y=100, anchor='nw') posiciona o widget 50 pixels à direita e 100 pixels abaixo do canto superior esquerdo do contêiner, ancorado no canto superior esquerdo do próprio widget.\n"
                "- place(relx=0.5, rely=0.5, anchor='center') posiciona o widget exatamente no centro do contêiner pai.\n\n"

                "Para layouts simples e controle absoluto de posição, place é uma ferramenta poderosa, porém para interfaces dinâmicas e responsivas, outras opções como grid ou pack são geralmente mais indicadas.\n\n"

                "Para mais detalhes, consulte a documentação oficial do Tkinter Place Geometry Manager:\n"
                "https://docs.python.org/3/library/tkinter.html#the-place-geometry-manager\n"
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

       
        frame_exemplo = tk.Frame(self.janela, width=500, height=250, bg="#f9f9f9", relief=tk.GROOVE, bd=1)
        frame_exemplo.pack(pady=10)
        frame_exemplo.pack_propagate(False) 

        
        tk.Label(frame_exemplo, text="Nome:", font=("Arial", 11), bg="#f9f9f9")\
            .place(x=20, y=20)
        self.entry_nome = tk.Entry(frame_exemplo, font=("Arial", 11), width=30)
        self.entry_nome.place(x=120, y=20)

        tk.Label(frame_exemplo, text="Sobrenome:", font=("Arial", 11), bg="#f9f9f9")\
            .place(x=20, y=60)
        self.entry_sobrenome = tk.Entry(frame_exemplo, font=("Arial", 11), width=30)
        self.entry_sobrenome.place(x=120, y=60)

       
        btn_ok = tk.Button(frame_exemplo, text="OK", command=self.mostrar_nome_completo)
        btn_ok.place(x=120, y=110, width=100)

        btn_limpar = tk.Button(frame_exemplo, text="Limpar", command=self.limpar_campos)
        btn_limpar.place(x=230, y=110, width=100)

      
        self.label_resultado = tk.Label(frame_exemplo, text="", font=("Arial", 11), fg="green", bg="#f9f9f9")
        self.label_resultado.place(x=20, y=160)

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
    app = TelaPlace()
    app.iniciar()