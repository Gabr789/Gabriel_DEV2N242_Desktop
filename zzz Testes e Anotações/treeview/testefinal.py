import tkinter as tk
from tkinter import ttk, messagebox

# Funções principais
def adicionar():
    if not nome.get() or not idade.get().isdigit() or not curso.get():
        messagebox.showwarning("Aviso", "Preencha os campos corretamente!")
        return
    
    tree.insert("", "end", values=(nome.get(), idade.get(), curso.get()))
    limpar_campos()

def editar():
    item = tree.selection()
    if not item:
        messagebox.showwarning("Aviso", "Selecione um item para editar")
        return
    
    valores = tree.item(item, "values")
    nome.set(valores[0])
    idade.set(valores[1])
    curso.set(valores[2])

def salvar():
    item = tree.selection()
    if not item:
        messagebox.showwarning("Aviso", "Nenhum item selecionado para salvar")
        return
    
    tree.item(item, values=(nome.get(), idade.get(), curso.get()))
    limpar_campos()

def excluir():
    item = tree.selection()
    if not item:
        messagebox.showwarning("Aviso", "Selecione um item para excluir")
        return
    tree.delete(item)

def limpar_campos():
    nome.set("")
    idade.set("")
    curso.set("")

def filtrar():
    filtro = busca.get().lower()
    for item in tree.get_children():
        valores = tree.item(item, "values")
        if filtro in valores[0].lower() or filtro in valores[2].lower():
            tree.item(item, tags=("visivel",))
        else:
            tree.item(item, tags=("oculto",))
    tree.tag_configure("oculto", foreground="gray70")
    tree.tag_configure("visivel", foreground="black")

# Criando a janela principal
janela = tk.Tk()
janela.title("Sistema de Cadastro - Treeview")
janela.geometry("650x500")

# Variáveis
nome = tk.StringVar()
idade = tk.StringVar()
curso = tk.StringVar()
busca = tk.StringVar()

# Frame do formulário
frame_form = tk.Frame(janela, padx=10, pady=10)
frame_form.pack(fill="x")

tk.Label(frame_form, text="Nome:").grid(row=0, column=0, sticky="w")
tk.Entry(frame_form, textvariable=nome, width=20).grid(row=0, column=1, padx=5)

tk.Label(frame_form, text="Idade:").grid(row=0, column=2, sticky="w")
tk.Entry(frame_form, textvariable=idade, width=5).grid(row=0, column=3, padx=5)

tk.Label(frame_form, text="Curso:").grid(row=0, column=4, sticky="w")
tk.Entry(frame_form, textvariable=curso, width=15).grid(row=0, column=5, padx=5)

tk.Button(frame_form, text="Adicionar", command=adicionar).grid(row=1, column=0, pady=5)
tk.Button(frame_form, text="Editar", command=editar).grid(row=1, column=1, pady=5)
tk.Button(frame_form, text="Salvar", command=salvar).grid(row=1, column=2, pady=5)
tk.Button(frame_form, text="Excluir", command=excluir).grid(row=1, column=3, pady=5)
tk.Button(frame_form, text="Limpar", command=limpar_campos).grid(row=1, column=4, pady=5)

# Campo de busca
frame_busca = tk.Frame(janela, pady=10)
frame_busca.pack(fill="x")

tk.Label(frame_busca, text="Buscar:").pack(side="left", padx=5)
tk.Entry(frame_busca, textvariable=busca, width=20).pack(side="left", padx=5)
tk.Button(frame_busca, text="Filtrar", command=filtrar).pack(side="left", padx=5)

# Treeview
colunas = ("Nome", "Idade", "Curso")
tree = ttk.Treeview(janela, columns=colunas, show="headings", height=15)

for coluna in colunas:
    tree.heading(coluna, text=coluna)
    tree.column(coluna, width=150)

# Inserindo alguns dados iniciais
dados_iniciais = [
    ("Gabriel", 18, "Informática"),
    ("Ana", 20, "Direito"),
    ("Pedro", 22, "Engenharia"),
    ("Mariana", 19, "História"),
    ("Lucas", 21, "Medicina")
]

for d in dados_iniciais:
    tree.insert("", "end", values=d)

tree.pack(fill="both", expand=True, padx=10, pady=10)

# Scrollbar
scroll = ttk.Scrollbar(janela, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scroll.set)
scroll.pack(side="right", fill="y")

janela.mainloop()