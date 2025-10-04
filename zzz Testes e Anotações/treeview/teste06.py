import tkinter as tk
from tkinter import ttk

def filtrar():
    filtro = entrada.get().lower()
    for item in tree.get_children():
        valores = tree.item(item, "values")
        if filtro in valores[0].lower() or filtro in valores[2].lower():
            tree.item(item, tags=("visivel",))
        else:
            tree.item(item, tags=("oculto",))
    tree.tag_configure("oculto", foreground="gray70")  # deixa apagado
    tree.tag_configure("visivel", foreground="black")

janela = tk.Tk()
janela.title("Treeview - Filtro de Busca")
janela.geometry("500x300")

colunas = ("Nome", "Idade", "Curso")
tree = ttk.Treeview(janela, columns=colunas, show="headings")

for coluna in colunas:
    tree.heading(coluna, text=coluna)

dados = [
    ("Gabriel", 18, "Informática"),
    ("Ana", 20, "Direito"),
    ("Pedro", 22, "Engenharia"),
    ("Mariana", 19, "História"),
    ("Lucas", 21, "Medicina")
]

for d in dados:
    tree.insert("", tk.END, values=d)

tree.pack(fill="both", expand=True)

entrada = tk.Entry(janela)
entrada.pack(pady=5)

botao = tk.Button(janela, text="Filtrar", command=filtrar)
botao.pack(pady=5)

janela.mainloop()
