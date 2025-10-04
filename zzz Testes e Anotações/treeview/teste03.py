import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("Treeview com Scrollbar")
janela.geometry("400x250")

frame = tk.Frame(janela)
frame.pack(fill="both", expand=True)

colunas = ("ID", "Nome", "Idade")
tree = ttk.Treeview(frame, columns=colunas, show="headings")

# Definir títulos
for coluna in colunas:
    tree.heading(coluna, text=coluna)

# Inserir muitos dados
for i in range(1, 31):
    tree.insert("", "end", values=(i, f"Pessoa {i}", 18+i))

# Scrollbar vertical
scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scroll.set)

scroll.pack(side="right", fill="y")
tree.pack(side="left", fill="both", expand=True)

janela.mainloop()
