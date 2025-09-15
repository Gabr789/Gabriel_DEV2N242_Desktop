import tkinter as tk

janela = tk.Tk()
menubar = tk.Menu(janela)

menu_exercicios = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Exercícios", menu=menu_exercicios)

# Submenu da lista 04
submenu_lista04 = tk.Menu(menu_exercicios, tearoff=0)
submenu_lista04.add_command(label="Exercício 04.1")
submenu_lista04.add_command(label="Exercício 04.2")

# Submenu da lista 05
submenu_lista05 = tk.Menu(menu_exercicios, tearoff=0)
submenu_lista05.add_command(label="Exercício 05.1")
submenu_lista05.add_command(label="Exercício 05.2")

# Agora adicionamos os dois submenus dentro de Exercícios
menu_exercicios.add_cascade(label="Lista 04", menu=submenu_lista04)
menu_exercicios.add_cascade(label="Lista 05", menu=submenu_lista05)

janela.config(menu=menubar)
janela.mainloop()
