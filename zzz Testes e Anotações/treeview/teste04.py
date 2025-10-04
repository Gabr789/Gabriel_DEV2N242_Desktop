import tkinter as tk
from tkinter import ttk, messagebox

def mostrar_selecao():
    item = tree.selection()  # pega o item selecionado
    if item:
        valores = tree.item(item, "values")
        messagebox.showinfo("Selecionado", f"Nome: {valores[0]}\nIdade: {valores[1]}\nCurso: {valores[2]}")

janela = tk.Tk()
janela.title("Treeview - Seleção")
janela.geometry("500x300")

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

botao = tk.Button(janela, text="Mostrar Seleção", command=mostrar_selecao)
botao.pack(pady=10)

janela.mainloop()
