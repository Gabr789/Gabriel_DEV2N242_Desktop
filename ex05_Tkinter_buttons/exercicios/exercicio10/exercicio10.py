import tkinter as tk
from tkinter import ttk


# Exercício 10 
# Crie um pequeno formulário com: Combobox para curso, Radiobuttons para turno 
# Checkbuttons para Participa do Discord e Gosta de programação 
# Ao clicar no botão Enviar, exiba todas as escolhas em uma nova janela.



class Ex10:
    def __init__(self, janelaPrincipal=None):
        self.janela = tk.Toplevel(janelaPrincipal) if janelaPrincipal else tk.Tk()
        self.janela.title("Exercício 10")
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
                preferencias.config(text=f"Perfil criado com sucesso.\nVocê estudará o curso {curso} no turno da {turno}.\nVocê " + " e ".join(escolhas))
            elif curso and turno != "__nada__":
                preferencias.config(text=f"Perfil criado com sucesso.\nVocê estudará o curso {curso} no turno da {turno}.")
            else:
                preferencias.config(text="Escolha o curso e o turno")




        local_escolhas = tk.Frame(self.janela)
        local_escolhas.pack(pady=20)


        tk.Label(local_escolhas, text="Escolha o curso:").pack(anchor="w")

        cursos = ["Java", "JavaScript", "Python"]

        self.combo = ttk.Combobox(local_escolhas, values=cursos, state="readonly")
        self.combo.pack(pady=10, anchor="w")



        tk.Label(local_escolhas, text="Escolha o turno:").pack(pady=10, anchor="w")

        turnos = tk.StringVar(value="__nada__")

        tk.Radiobutton(local_escolhas, text="Manhã", variable=turnos, value="Manhã").pack(anchor="w")
        tk.Radiobutton(local_escolhas, text="Tarde", variable=turnos, value="Tarde").pack(anchor="w")
        tk.Radiobutton(local_escolhas, text="Noite", variable=turnos, value="Noite").pack(anchor="w")



        tk.Label(local_escolhas, text="Marque as caixas que se aplicam:").pack(pady=10, anchor="w")

        self.participa = tk.BooleanVar()
        self.gosta = tk.BooleanVar()

        tk.Checkbutton(local_escolhas, text="Participa do Discord", variable=self.participa).pack(anchor="w")
        tk.Checkbutton(local_escolhas, text="Gosta de programação", variable=self.gosta).pack(anchor="w")



        botao = tk.Button(self.janela, text="Enviar", command=confirmar)
        botao.pack(pady=10)

        preferencias = tk.Label(self.janela, text="")
        preferencias.pack(pady=10)

    
    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()

exe = Ex10()
exe.iniciar()