import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("Exemplo Treeview - Hierarquia")
janela.geometry("400x300")

tree = ttk.Treeview(janela)

# Inserindo itens principais (pais)
pai1 = tree.insert("", "end", text="Documentos")
pai2 = tree.insert("", "end", text="Imagens")

# Inserindo filhos
tree.insert(pai1, "end", text="Trabalho.docx")
tree.insert(pai1, "end", text="Lista.pdf")
tree.insert(pai2, "end", text="foto1.png")
tree.insert(pai2, "end", text="foto2.jpg")

tree.pack(fill="both", expand=True)

janela.mainloop()
