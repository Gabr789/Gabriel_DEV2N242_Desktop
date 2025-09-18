import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from estilo01 import Estilos01


# Desafio 1 
# Crie uma janela com campos Entry para nome e idade, uma Combobox com os 
# cursos: ADS, Jogos, Redes, Radiobuttons para turno: Manhã, Tarde, Noite, e 
# Checkbuttons para Gosta de programação e Participa do Discord. 
# Ao clicar no botão Enviar, exiba todas as informações em uma nova janela. Se algum 
# campo estiver vazio, mostre a mensagem "Preencha todos os campos!".



class Ex0601:
    def __init__(self, master=None):
        self.janela = tk.Toplevel(master) if master else tk.Tk()
        self.janela.title("Exercício 1")
        self.janela.geometry("600x500")
        self.janela.config(**Estilos01.estiloJanela())


        def confirmar():
            curso = self.combo.get()
            turno = turnos.get()
            escolhas = []
            if self.participa.get():
                escolhas.append("Participa do Discord")
            if self.gosta.get():
                escolhas.append("Gosta de programação")


            if curso and turno != "__nada__" and escolhas:
                messagebox.showinfo("Perfil Criado", f"Perfil criado com sucesso.\nVocê estudará o curso {curso} no turno da {turno}.\nVocê " + " e ".join(escolhas))
            elif curso and turno != "__nada__":
                messagebox.showinfo("Perfil Criado", f"Perfil criado com sucesso.\nVocê estudará o curso {curso} no turno da {turno}.")
            else:
                messagebox.showerror("Erro", "Escolha o curso e o turno")



        frame_principal = tk.Frame(self.janela, **Estilos01.estiloFrame())
        frame_principal.pack(pady=50)



        tk.Label(
            frame_principal,
            **Estilos01.estiloLabel(),
            text="Escolha o curso:"
            ).pack(pady=(20, 10), padx=40, anchor="w")

        cursos = ["ADS", "Jogos", "Redes"]
        self.combo = ttk.Combobox(frame_principal, values=cursos, state="readonly")
        self.combo.pack(padx=40, anchor="w")



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



        tk.Button(
            frame_principal,
            **Estilos01.estiloButton(),
            text="Enviar",
            command=confirmar
            ).pack(pady=30, padx=40, anchor="e")

        """Configurar as fontes"""



    
    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()

exemplo = Ex0601()
exemplo.iniciar()