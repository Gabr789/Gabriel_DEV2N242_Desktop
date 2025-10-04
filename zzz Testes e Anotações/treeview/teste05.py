import tkinter as tk
from tkinter import ttk, messagebox

def editar_item():
    item = tree.selection()
    if not item:
        messagebox.showwarning("Aviso", "Selecione um item para editar")
        return
    
    valores = tree.item(item, "values")
    nome.set(valores[0])
    idade.set(valores[1])
    curso.set(valores[2])

def salvar_edicao():
    item = tree.selection()
    if item:
        tree.item(item, values=(nome.get(), idade.get(), curso.get()))
        limpar_campos()

def excluir_item():
    item = tree.selection()
    if item:
        tree.delete(item)
    else:
        messagebox.showwarning("Aviso", "Selecione um item para excluir")

def limpar_campos():
    nome.set("")
    idade.set("")
    curso.set("")

janela = tk.Tk()
janela.title("Treeview - Editar e Excluir")
janela.geometry("600x400")

colunas = ("Nome", "Idade", "Curso")
tree = ttk.Treeview(janela, columns=colunas, show="headings")

for coluna in colunas:
    tree.heading(coluna, text=coluna)

dados = [
    ("Gabriel", 18, "Informática"),
    ("Ana", 20, "Direito"),
    ("Pedro", 22, "Engenharia")
]

for d in dados:
    tree.insert("", tk.END, values=d)

tree.pack(fill="both", expand=True)

# Campos de edição
frame = tk.Frame(janela)
frame.pack(pady=10)

nome = tk.StringVar()
idade = tk.StringVar()
curso = tk.StringVar()

tk.Entry(frame, textvariable=nome, width=15).grid(row=0, column=0, padx=5)
tk.Entry(frame, textvariable=idade, width=5).grid(row=0, column=1, padx=5)
tk.Entry(frame, textvariable=curso, width=15).grid(row=0, column=2, padx=5)

tk.Button(frame, text="Editar", command=editar_item).grid(row=1, column=0, pady=5)
tk.Button(frame, text="Salvar", command=salvar_edicao).grid(row=1, column=1, pady=5)
tk.Button(frame, text="Excluir", command=excluir_item).grid(row=1, column=2, pady=5)

janela.mainloop()
