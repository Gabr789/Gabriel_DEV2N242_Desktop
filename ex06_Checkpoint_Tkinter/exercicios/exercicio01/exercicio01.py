import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


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





        frame_principal = tk.Frame(self.janela) # **Estilos01.estiloFramePrincipal()
        frame_principal.pack()


        tk.Label(frame_principal, text="Escolha o curso:").pack(pady=(20, 10), anchor="w") # **Estilos01.estiloLabel()

        cursos = ["ADS", "Jogos", "Redes"]
        self.combo = ttk.Combobox(frame_principal, values=cursos, state="readonly")
        self.combo.pack(anchor="w")



        tk.Label(frame_principal, text="Escolha o turno:").pack(pady=(30, 10), anchor="w") # **Estilos01.estiloLabel()

        turnos = tk.StringVar(value="__nada__")
        tk.Radiobutton(frame_principal, text="Manhã", variable=turnos, value="Manhã").pack(anchor="w") # **Estilos01.estiloRadio()
        tk.Radiobutton(frame_principal, text="Tarde", variable=turnos, value="Tarde").pack(anchor="w") # **Estilos01.estiloRadio()
        tk.Radiobutton(frame_principal, text="Noite", variable=turnos, value="Noite").pack(anchor="w") # **Estilos01.estiloRadio()


        
        tk.Label(frame_principal, text="Marque as caixas que se aplicam:").pack(pady=(30, 10), anchor="w") # Estilos01.estiloLabel()

        self.participa = tk.BooleanVar()
        self.gosta = tk.BooleanVar()

        tk.Checkbutton(frame_principal, text="Participa do Discord", variable=self.participa).pack(anchor="w") # **Estilos01.estiloCheck()
        tk.Checkbutton(frame_principal, text="Gosta de Programação", variable=self.gosta).pack(anchor="w") # **Estilos01.estiloCheck()


        tk.Button(frame_principal, text="Enviar", command=confirmar).pack(pady=30, anchor="e") # **Estilos01.estiloButton()

        """Configurar os estilos"""



    
    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()

exemplo = Ex0601()
exemplo.iniciar()