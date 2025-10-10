import os
import tkinter as tk
from tkinter import Toplevel
from .tela_widgets import TelaWidgets
from .tela_interacao import Interacoes
from exercicios.telainicial.tela_inicial import MenuListas
from Tkinter.imports import *

class MenuPrincipal:
    def __init__(self, master=None, usuario=None, banco=None):
        self.usuario = usuario
        self.banco = banco
        self.janela = Toplevel(master)
        self.janela.title("Menu Principal")
        self.janela.geometry("600x400")

        caminho_icone = os.path.join(os.path.dirname(__file__), "../logo.ico")
        if os.path.exists(caminho_icone):
            self.janela.iconbitmap(caminho_icone)

      
        grupos = []
        if self.banco and self.usuario:
            grupos = self.banco.obter_grupos_usuario(self.usuario)

        barra_menu = tk.Menu(self.janela)

        
        menu_widgets = tk.Menu(barra_menu, tearoff=0)

        submenu_widgets_basicos = tk.Menu(menu_widgets, tearoff=0)
        submenu_widgets_basicos.add_command(label="Botão", command=self.abrir_tela_botao)
        submenu_widgets_basicos.add_command(label="Frame", command=self.abrir_tela_frame)
        submenu_widgets_basicos.add_command(label="Label", command=self.abrir_tela_label)

        submenu_widgets_entrada = tk.Menu(menu_widgets, tearoff=0)
        submenu_widgets_entrada.add_command(label="Combo", command=self.abrir_tela_combo)
        submenu_widgets_entrada.add_command(label="Entrada", command=self.abrir_tela_entrada)
        submenu_widgets_entrada.add_command(label="Scale", command=self.abrir_tela_scale)
        submenu_widgets_entrada.add_command(label="Spinbox", command=self.abrir_tela_spin)

        submenu_widgets_interface = tk.Menu(menu_widgets, tearoff=0)
        submenu_widgets_interface.add_command(label="menu", command=self.abrir_tela_menu)

        submenu_widgets_selecao = tk.Menu(menu_widgets, tearoff=0)
        submenu_widgets_selecao.add_command(label="Check", command=self.abrir_tela_check)
        submenu_widgets_selecao.add_command(label="List", command=self.abrir_tela_list)
        submenu_widgets_selecao.add_command(label="Radio", command=self.abrir_tela_radio)

        submenu_widgets_ttk = tk.Menu(menu_widgets, tearoff=0)
        submenu_widgets_ttk.add_command(label="Árvore", command=self.abrir_tela_arvore)

        menu_widgets.add_cascade(label="Widgets Básicos", menu=submenu_widgets_basicos)
        menu_widgets.add_cascade(label="Widgets Entrada", menu=submenu_widgets_entrada)
        menu_widgets.add_cascade(label="Widgets interface", menu=submenu_widgets_interface)
        menu_widgets.add_cascade(label="Widgets selecao", menu=submenu_widgets_selecao)
        menu_widgets.add_cascade(label="Widgets ttk", menu=submenu_widgets_ttk)

        menu_widgets.add_command(label="Abrir Tela Widgets", command=self.abrir_tela_widgets)

        barra_menu.add_cascade(label="Widgets", menu=menu_widgets)

        
        menu_interacoes = tk.Menu(barra_menu, tearoff=0)

        submenu_teclado = tk.Menu(menu_interacoes, tearoff=0)
        submenu_teclado.add_command(label="Atalhos Teclado", command=self.abrir_tela_botao)
        submenu_teclado.add_command(label="Evento Tecla", command=self.abrir_tela_frame)

        submenu_mouse = tk.Menu(menu_interacoes, tearoff=0)
        submenu_mouse.add_command(label="Evento Click", command=self.abrir_tela_click)
        submenu_mouse.add_command(label="Entrada/Saída", command=self.eventos_entrada_saida)
        submenu_mouse.add_command(label="Movimento do Mouse", command=self.evento_movimento)

        menu_interacoes.add_cascade(label="Teclado", menu=submenu_teclado)
        menu_interacoes.add_cascade(label="Mouse", menu=submenu_mouse)

        menu_interacoes.add_command(label="Abrir Tela Interações", command=self.abrir_tela_interacoes)

        barra_menu.add_cascade(label="Interações", menu=menu_interacoes)

      
        menu_layouts = tk.Menu(barra_menu, tearoff=0)

        submenu_layouts = tk.Menu(menu_layouts, tearoff=0)
        submenu_layouts.add_command(label="Grid", command=self.abrir_tela_grid)
        submenu_layouts.add_command(label="Pack", command=self.abrir_tela_pack)
        submenu_layouts.add_command(label="Place", command=self.abrir_tela_place)

        menu_layouts.add_cascade(label="Gerenciadores", menu=submenu_layouts)
        menu_layouts.add_command(label="Abrir Tela Layouts", command=self.abrir_tela_layouts)

        barra_menu.add_cascade(label="Layouts", menu=menu_layouts)

        
        menu_arquivos = tk.Menu(barra_menu, tearoff=0)
        menu_arquivos.add_command(label="TXT", command=self.gerenciador_texto)
        menu_arquivos.add_command(label="Word", command=self.gerenciador_texto_word)
        menu_arquivos.add_command(label="Selecionador de Arquivo", command=self.selecionador_arquivo)
        menu_arquivos.add_command(label="Excel", command=self.gerenciador_arquvivo_excel)
        barra_menu.add_cascade(label="Arquivos", menu=menu_arquivos)

        # Frame para os exercícios
        self.frame_exercicio = tk.Frame(self.janela)
        self.frame_exercicio.pack(expand=True, fill="both", padx=10, pady=10)

        # Menu Exercícios
        menu_exercicios = tk.Menu(barra_menu, tearoff=0)

        submenu_lista4 = tk.Menu(menu_exercicios, tearoff=0)
        for i in range(1, 11):
            submenu_lista4.add_command(label=f"Exercício {i}", command=lambda n=i: self.abrir_exercicio(4, n))

        submenu_lista5 = tk.Menu(menu_exercicios, tearoff=0)
        for i in range(1, 11):
            submenu_lista5.add_command(label=f"Exercício {i}", command=lambda n=i: self.abrir_exercicio(5, n))

        submenu_lista7 = tk.Menu(menu_exercicios, tearoff=0)
        for i in range(1, 11):
            submenu_lista7.add_command(label=f"Exercício {i}", command=lambda n=i: self.abrir_exercicio(7, n))

        menu_exercicios.add_cascade(label="Lista 4", menu=submenu_lista4)
        menu_exercicios.add_cascade(label="Lista 5", menu=submenu_lista5)
        menu_exercicios.add_cascade(label="Lista 7", menu=submenu_lista7)

        barra_menu.add_cascade(label="Exercícios", menu=menu_exercicios)

        # **Menu Usuários: aparece apenas se usuário NÃO for do grupo 'alunos'**
        if "alunos" not in grupos:
            menu_usuarios = tk.Menu(barra_menu, tearoff=0)
            menu_usuarios.add_command(label="Listar Usuários", command=self.abrir_lista_usuarios)
            barra_menu.add_cascade(label="Usuários", menu=menu_usuarios)

        # Configura o menu na janela
        self.janela.config(menu=barra_menu)

        # Dicionário dos exercícios (sem alterar)
        self.exercicios = {
            4: {
                1: Ex1,
                2: Ex2,
                3: Ex3,
                4: Ex4,
                5: Ex5,
                6: Ex6,
                7: Ex7,
                8: Ex8,
                9: Ex9,
                10: Ex10
            },
            5: {
                1: Ex1_5,
                2: Ex2_5,
                3: Ex3_5,
                4: Ex4_5,
                5: Ex5_5,
                6: Ex6_5,
                7: Ex7_5,
                8: Ex8_5,
                9: Ex9_5,
                10: Ex10_5
            },
            7: {
                1: Ex1_7,
                2: Ex2_7,
                3: Ex3_7,
                4: Ex4_7,
                5: Ex5_7,
                6: Ex6_7,
                7: Ex7_7,
                8: Ex8_7,
                9: Ex9_7,
                10: Ex10_7
            }
        }

    def abrir_exercicio(self, lista, numero):
        classe_ex = self.exercicios[lista][numero]

        if lista == 4:
            for widget in self.frame_exercicio.winfo_children():
                widget.destroy()

            exercicio_frame = classe_ex(self.frame_exercicio)
            exercicio_frame.pack(expand=True, fill="both")
        else:
            for widget in self.frame_exercicio.winfo_children():
                widget.destroy()
            nova_janela = tk.Toplevel(self.janela)
            nova_janela.title(f"Lista {lista} - Exercício {numero}")
            nova_janela.geometry("400x300")
            exercicio_frame = classe_ex(nova_janela)
            exercicio_frame.pack(expand=True, fill="both")






    def abrir_lista_usuarios(self):
      
        TelaListaUsuarios(self.janela).iniciar()

        
    
    def abrir_tela_widgets(self):
        self.janela.withdraw()
        tela_widgets = TelaWidgets(master=self.janela)
        tela_widgets.iniciar()

    def abrir_tela_interacoes(self):
        self.janela.withdraw()
        tela_interacoes = Interacoes(master=self.janela)
        tela_interacoes.iniciar()

    def abrir_tela_layouts(self):
        self.janela.withdraw()
        from .tela_layouts import TelaLayouts
        tela_layouts = TelaLayouts(master=self.janela)
        tela_layouts.iniciar()

    def abrir_tela_exercicios(self):
        self.janela.withdraw()
        tela_exercicios = MenuListas(master=self.janela)
        tela_exercicios.iniciar()

    def iniciar(self):
        self.janela.mainloop()



    def abrir_tela_botao(self):
        TelaBotoes(self.janela).iniciar()

    def abrir_tela_frame(self):
        TelaFrame(self.janela).iniciar()

    def abrir_tela_label(self):
        TelaLabel(self.janela).iniciar()

    def abrir_tela_entrada(self):
        TelaEntry(self.janela).iniciar()

    def abrir_tela_combo(self):
        TelaCombobox(self.janela).iniciar()

    def abrir_tela_spin(self):
        TelaSpinbox(self.janela).iniciar()

    def abrir_tela_scale(self):
        TelaScale(self.janela).iniciar()

    def abrir_tela_text(self):
        TelaText(self.janela).iniciar()

    def abrir_tela_check(self):
        TelaCheckbutton(self.janela).iniciar()
    
    def abrir_tela_menu(self):
        TelaMenu(self.janela).iniciar()

    def abrir_tela_radio(self):
        TelaRadiobutton(self.janela).iniciar()

    def abrir_tela_list(self):
        TelaListbox(self.janela).iniciar()

    def abrir_tela_place(self):
        TelaPlace(self.janela).iniciar()

    def abrir_tela_pack(self):
        TelaPack(self.janela).iniciar()

    def abrir_tela_grid(self):
        TelaGrid(self.janela).iniciar()
    
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

    def gerenciador_texto(self):
        TelaArquivos(self.janela).iniciar()
    
    
    def gerenciador_texto_word(self):
       TelaArquivosWord(self.janela).iniciar()
    
    def gerenciador_arquvivo_excel(self):
       TelaExcel(self.janela).iniciar()
    
    def abrir_tela_arvore(self):
        TelaTreeview(self.janela).iniciar()


    def selecionador_arquivo(self):
       self.janela.withdraw()
       tela_selecionador_arquivo = TelaFileDialog(master=self.janela)
       tela_selecionador_arquivo.iniciar()
       






