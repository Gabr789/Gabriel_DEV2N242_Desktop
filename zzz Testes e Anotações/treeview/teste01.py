import tkinter as tk
from tkinter import ttk

# Criar janela
janela = tk.Tk()
janela.title("Exemplo Treeview - Tabela simples")
janela.geometry("500x300")

# Criar Treeview com colunas
colunas = ("Nome", "Idade", "Curso")
tree = ttk.Treeview(janela, columns=colunas, show="headings")

# Definir títulos das colunas
for coluna in colunas:
    tree.heading(coluna, text=coluna)

# Inserir dados
tree.insert("", tk.END, values=("Gabriel", 18, "Informática"))
tree.insert("", tk.END, values=("Ana", 20, "Direito"))
tree.insert("", tk.END, values=("Pedro", 22, "Engenharia"))

tree.pack(fill="both", expand=True)

janela.mainloop()
