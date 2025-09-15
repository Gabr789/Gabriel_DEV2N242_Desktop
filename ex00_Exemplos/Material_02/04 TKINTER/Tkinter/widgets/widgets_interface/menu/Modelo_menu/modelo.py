import tkinter as tk
import os
from .Lista1Frame import TelaLista1Frame
from .Lista1 import Lista1
from tkinter import messagebox
class ModeloMenu():
    def __init__(self,master=None):
        self.janela = tk.Toplevel(master)
        self.janela.title("Modelo menu")
        self.janela.geometry("600x600")
        self.janela.configure(bg="green")
        
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../../logo.ico")
        if os.path.exists(caminho_icone):
            self.janela.iconbitmap(caminho_icone)

        self.frame_modelo = tk.Frame(self.janela, bg="green")
        self.frame_modelo.pack(pady=10)

       
        menu_modelo = tk.Menu(self.janela)
        menu_exercicios = tk.Menu(menu_modelo, tearoff=0)
        menu_nova_janela = tk.Menu(menu_modelo, tearoff=0)

       
        submenulista1 = tk.Menu(menu_exercicios, tearoff=0)
        for i in range(1, 11):
            submenulista1.add_command(label=f"Exercício {i}",command=lambda n=i: self.abrir_exercicio(1, n))
        menu_exercicios.add_cascade(label="Lista 1", menu=submenulista1)
        menu_modelo.add_cascade(label="Exercícios", menu=menu_exercicios)

       
        submenu_lista1_nova_janela = tk.Menu(menu_nova_janela, tearoff=0)
        for i in range(1, 10): 
            submenu_lista1_nova_janela.add_command(label=f"Exercício {i}",command=lambda n=i: self.abrir_exercicio_nova_janela(1, n))
        menu_nova_janela.add_cascade(label="Lista 1", menu=submenu_lista1_nova_janela)
        menu_modelo.add_cascade(label="Nova Janela", menu=menu_nova_janela)

      
        self.janela.config(menu=menu_modelo)

      
        self.exercicios = {
            1: {
                1: TelaLista1Frame,
               
            }
        }

      
        self.exercicios_nova_janela = {
            1: {
                1: Lista1,
                
            }
        }

    def limpar(self):
        for widget in self.frame_modelo.winfo_children():
            widget.destroy()

    def abrir_exercicio(self, lista, numero):
        self.limpar()
        try:
            classe_ex = self.exercicios[lista][numero]
            exercicio_frame = classe_ex(self.frame_modelo)
            exercicio_frame.pack(expand=True, fill="both")
        except KeyError:
          messagebox.showerror("Erro",f"Exercício {numero} da Lista {lista} não encontrado.",)

           

    def abrir_exercicio_nova_janela(self, lista, numero):
        self.limpar()
        try:
            classe_ex = self.exercicios_nova_janela[lista][numero]
            exercicio = classe_ex(self.janela)  
            exercicio.iniciar()  
        except KeyError:
            messagebox.showerror("Erro",f"Exercício {numero} da Lista {lista} não encontrado.",)

             
    def iniciar(self):
        self.janela.mainloop()

