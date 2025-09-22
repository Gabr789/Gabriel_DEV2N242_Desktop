import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from .estilo02 import Estilos02


# Desafio 2 
# Crie uma interface com uma Combobox para o tamanho da pizza: Pequena, Média, 
# Grande, Radiobuttons para o tipo de massa: Fina, Tradicional, e Checkbuttons para 
# ingredientes: Queijo, Calabresa, Tomate, Cebola. 
# Adicione também Radiobuttons para a forma de pagamento: Dinheiro, Cartão, Pix. 
# Ao clicar no botão Finalizar Pedido, exiba no Label o pedido completo com as 
# escolhas feitas. 



class Ex0601:
    def __init__(self, master=None):
        self.janela = tk.Toplevel(master) if master else tk.Tk()
        self.janela.title("Exercício 1")
        self.janela.geometry("600x700")
        self.janela.config(**Estilos02.estiloJanela())


        def confirmarNome(nome):
            return bool(nome.strip())
        
        def confirmarIdade(idade):
            return idade.isdigit() and int(idade) > 0 and int(idade) < 130
    
        def confirmarCurso(curso):
            return bool(curso)    

        def confirmarTurno(turno):
            return turno != "__nada__"


        def enviar():
            nome = self.nome.get().strip()
            idade = self.idade.get()
            curso = self.combo.get()
            turno = turnos.get()
            escolhas = []
            if self.participa.get():
                escolhas.append("participa do Discord")
            if self.gosta.get():
                escolhas.append("gosta de programação")

            if not confirmarNome(nome):
                messagebox.showerror("Erro", "Digite um nome válido")
            elif not confirmarIdade(idade):
                messagebox.showerror("Erro", "Digite uma idade válida")
            elif not confirmarCurso(curso):
                messagebox.showerror("Erro", "Escolha um curso")
            elif not confirmarTurno(turno):
                messagebox.showerror("Erro", "Escolha um turno")
            else:
                mensagem = (
                    "Perfil criado com sucesso!\n"
                    f"Você se chama {nome} e tem {idade} anos.\n"
                    f"Você estudará o curso de {curso} no turno da {turno}.\n"
                    )
                if escolhas:
                    mensagem += "Você " + " e ".join(escolhas) + "."

                messagebox.showinfo("Perfil Criado", mensagem)



        """Frame"""

        frame_principal = tk.Frame(self.janela, **Estilos02.estiloFrame())
        frame_principal.pack(pady=50)



        # Desafio 2 
        # Crie uma interface com uma Combobox para o tamanho da pizza: Pequena, Média, 
        # Grande, Radiobuttons para o tipo de massa: Fina, Tradicional, e Checkbuttons para 
        # ingredientes: Queijo, Calabresa, Tomate, Cebola. 
        # Adicione também Radiobuttons para a forma de pagamento: Dinheiro, Cartão, Pix. 
        # Ao clicar no botão Finalizar Pedido, exiba no Label o pedido completo com as 
        # escolhas feitas. 

        """Tamanho"""

        tk.Label(
            frame_principal,
            **Estilos02.estiloLabel(),
            text="Escolha o tamanho da pizza:"
            ).pack(pady=(20, 10), padx=40, anchor="w")


        tamanhos = ["pequena", "média", "grande"]

        self.tamanho = ttk.Combobox(
            frame_principal,
            **Estilos02.estiloCombo(),
            values=tamanhos,
            state="readonly"
            )
        self.tamanho.pack(padx=40, anchor="w")



        """Tipo de massa"""

        tk.Label(
            frame_principal,
            **Estilos02.estiloLabel(),
            text="Escolha o tipo de massa da pizza:"
        ).pack(pady=(20, 10), padx=40, anchor="w")


        tipos_massa = tk.StringVar(value="__nada__")

        tk.Radiobutton(
            frame_principal,
            **Estilos02.estiloRadio(),
            text="Fina",
            variable=tipos_massa,
            value="fina"
        ).pack(padx=40, anchor="w")

        tk.Radiobutton(
            frame_principal,
            **Estilos02.estiloRadio(),
            text="Tradicional",
            variable=tipos_massa,
            value="tradicional"
        ).pack(padx=40, anchor="w")



        """Ingredientes"""

















        tk.Radiobutton(
            frame_principal,
            **Estilos02.estiloRadio(),
            text="Grande",
            variable=tamanhos,
            value="grande"
        ).pack(padx=40, anchor="w")




        tk.Radiobutton(
            frame_principal,
            **Estilos01.estiloRadio(),
            text="Manhã",
            variable=turnos,
            value="Manhã"
            ).pack(padx=40, anchor="w")



        "Nome"

        tk.Label(
            frame_principal,
            **Estilos01.estiloLabel(),
            text="Digite seu nome:"
            ).pack(pady=(20, 10), padx=40, anchor="w")
        
        self.nome = tk.Entry(
            frame_principal,
            **Estilos01.estiloEntry(),
        )
        self.nome.pack(padx=40, anchor="w")



        """Idade"""

        tk.Label(
            frame_principal,
            **Estilos01.estiloLabel(),
            text="Digite sua idade:"
            ).pack(pady=(20, 10), padx=40, anchor="w")
        
        self.idade = tk.Entry(
            frame_principal,
            **Estilos01.estiloEntry(),
        )
        self.idade.pack(padx=40, anchor="w")



        """Curso"""

        tk.Label(
            frame_principal,
            **Estilos01.estiloLabel(),
            text="Escolha o curso:"
            ).pack(pady=(20, 10), padx=40, anchor="w")

        cursos = ["ADS", "Jogos", "Redes"]
        self.combo = ttk.Combobox(
            frame_principal,
            **Estilos01.estiloCombo(),
            values=cursos,
            state="readonly"
            )
        self.combo.pack(padx=40, anchor="w")



        """Turno"""

        tk.Label(
            frame_principal,
            **Estilos01.estiloLabel(),
            text="Escolha o turno:"
            ).pack(pady=(30, 10), padx=40, anchor="w")

        turnos = tk.StringVar(value="__nada__")
        tk.Radiobutton(
            frame_principal,
            **Estilos01.estiloRadio(),
            text="Manhã",
            variable=turnos,
            value="Manhã"
            ).pack(padx=40, anchor="w")
        tk.Radiobutton(
            frame_principal,
            **Estilos01.estiloRadio(),
            text="Tarde",
            variable=turnos,
            value="Tarde"
            ).pack(padx=40, anchor="w")
        tk.Radiobutton(
            frame_principal,
            **Estilos01.estiloRadio(),
            text="Noite",
            variable=turnos,
            value="Noite"
            ).pack(padx=40, anchor="w")



        """Escolhas"""
        
        tk.Label(
            frame_principal,
            **Estilos01.estiloLabel(),
            text="Marque as caixas que se aplicam:"
            ).pack(pady=(30, 10), padx=40, anchor="w")

        self.participa = tk.BooleanVar()
        self.gosta = tk.BooleanVar()
        tk.Checkbutton(
            frame_principal,
            **Estilos01.estiloCheck(),
            text="Participa do Discord",
            variable=self.participa
            ).pack(padx=40, anchor="w")
        tk.Checkbutton(
            frame_principal,
            **Estilos01.estiloCheck(),
            text="Gosta de Programação",
            variable=self.gosta
            ).pack(padx=40, anchor="w")



        """Botão Enviar"""

        tk.Button(
            frame_principal,
            **Estilos01.estiloButton(),
            text="Enviar",
            command=enviar
            ).pack(pady=30, padx=40, anchor="e")



    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()