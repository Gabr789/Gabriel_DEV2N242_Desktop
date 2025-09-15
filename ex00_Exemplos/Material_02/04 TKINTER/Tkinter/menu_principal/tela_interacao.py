


from Tkinter.imports import *
import tkinter as tk
from tkinter import ttk


class Interacoes:
    def __init__(self, master=None):
        self.master = master
        self.janela = tk.Toplevel(master) if master else tk.Tk()
        self.janela.title("Interações")
        self.janela.geometry("600x600")
        self.janela.configure(bg="white")
        self.janela.resizable(False, False)
        caminho_icone = os.path.join(os.path.dirname(__file__), "../logo.ico")
        if os.path.exists(caminho_icone):
            self.janela.iconbitmap(caminho_icone)
        
        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_janela)

        titulo = tk.Label(self.janela, text="Interações", font=("Arial", 16), bg="white")
        titulo.pack(pady=10)

        frame_menu = tk.Frame(self.janela, bg="white")
        frame_menu.pack(pady=10)

        tk.Button(frame_menu, text="Teclado", command=self.mostrar_teclado).pack(side="left", padx=10)
        tk.Button(frame_menu, text="Mouse", command=self.mostrar_mouse).pack(side="left", padx=10)
       

        self.frame_conteudo = tk.Frame(self.janela, bg="#f0f0f0", relief="sunken", bd=2)
        self.frame_conteudo.pack(expand=True, fill="both", padx=20, pady=20)

        self.mostrar_mensagem_inicial()

    def fechar_janela(self):
        if self.master:
            self.master.deiconify()  
        self.janela.destroy()

    def limpar_conteudo(self):
        for widget in self.frame_conteudo.winfo_children():
            widget.destroy()

    def mostrar_mensagem_inicial(self):
        self.limpar_conteudo()
        label = tk.Label(self.frame_conteudo, text="Escolha uma categoria de Interações acima.",
                         font=("Arial", 12), bg="#f0f0f0")
        label.pack(expand=True)

    def mostrar_teclado(self):
        self.limpar_conteudo()
        frame_botoes = tk.Frame(self.frame_conteudo, bg="#f0f0f0")
        frame_botoes.pack(anchor='n', pady=10)

        tk.Button(frame_botoes, text="Atalhos de Teclado", command=self.abrir_tela_botao).pack(side="left", padx=5)
        tk.Button(frame_botoes, text="Evento de Teclado", command=self.abrir_tela_frame).pack(side="left", padx=5)
        

    def mostrar_mouse(self):
        self.limpar_conteudo()
        frame_botoes = tk.Frame(self.frame_conteudo, bg="#f0f0f0")
        frame_botoes.pack(anchor='n', pady=10)

        tk.Button(frame_botoes, text="Evento de Clique", command=self.abrir_tela_click).pack(side="left", padx=5)
        tk.Button(frame_botoes, text="Eventos de Entrada e Saída", command=self.eventos_entrada_saida).pack(side="left", padx=5)
        tk.Button(frame_botoes, text="Evento de Movimento do Mouse", command=self.evento_movimento).pack(side="left", padx=5)




   
    def abrir_tela_botao(self):
        TelaAtalhosTeclado(self.janela).iniciar()

    def abrir_tela_frame(self):
        TelaEventoTecla(self.janela).iniciar()

    def abrir_tela_click(self):
        TelaEventoClick(self.janela).iniciar()

    def eventos_entrada_saida(self):
       TelaEventoEnterLeave(self.janela).iniciar()

    def evento_movimento(self):
        TelaEventoMotion(self.janela).iniciar()

    
    

 



    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()