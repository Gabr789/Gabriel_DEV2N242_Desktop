import tkinter as tk
from tkinter import ttk, messagebox

# =====================================================
# Sistema de Gerenciamento de Alunos
# =====================================================
# Esse sistema usa o Treeview do Tkinter como uma
# "tabela" para exibir dados. Ele permite:
# - Adicionar alunos
# - Editar informações
# - Excluir registros
# - Pesquisar por nome ou curso
# =====================================================

# ---------- FUNÇÕES PRINCIPAIS ----------

def adicionar_aluno():
    """Adiciona um novo aluno na tabela"""
    if not nome.get() or not idade.get().isdigit() or not curso.get():
        messagebox.showwarning("Aviso", "Preencha os campos corretamente!")
        return

    tree.insert("", "end", values=(nome.get(), idade.get(), curso.get()))
    limpar_campos()

def editar_aluno():
    """Carrega os dados do aluno selecionado para os campos de edição"""
    item = tree.selection()
    if not item:
        messagebox.showwarning("Aviso", "Selecione um aluno para editar")
        return
    
    valores = tree.item(item, "values")
    nome.set(valores[0])
    idade.set(valores[1])
    curso.set(valores[2])

def salvar_edicao():
    """Salva as alterações feitas nos campos para o aluno selecionado"""
    item = tree.selection()
    if not item:
        messagebox.showwarning("Aviso", "Nenhum aluno selecionado para salvar")
        return
    
    tree.item(item, values=(nome.get(), idade.get(), curso.get()))
    limpar_campos()

def excluir_aluno():
    """Remove o aluno selecionado da tabela"""
    item = tree.selection()
    if not item:
        messagebox.showwarning("Aviso", "Selecione um aluno para excluir")
        return
    
    confirm = messagebox.askyesno("Confirmação", "Deseja realmente excluir este aluno?")
    if confirm:
        tree.delete(item)

def limpar_campos():
    """Limpa os campos de entrada"""
    nome.set("")
    idade.set("")
    curso.set("")

def buscar_aluno():
    """Aplica um filtro de busca pelo nome ou curso"""
    filtro = busca.get().lower()
    for item in tree.get_children():
        valores = tree.item(item, "values")
        if filtro in valores[0].lower() or filtro in valores[2].lower():
            tree.item(item, tags=("visivel",))
        else:
            tree.item(item, tags=("oculto",))
    tree.tag_configure("oculto", foreground="gray70")
    tree.tag_configure("visivel", foreground="black")

# ---------- JANELA PRINCIPAL ----------

janela = tk.Tk()
janela.title("📘 Gerenciador de Alunos")
janela.geometry("700x500")
janela.configure(bg="#f4f4f4")

# ---------- VARIÁVEIS ----------
nome = tk.StringVar()
idade = tk.StringVar()
curso = tk.StringVar()
busca = tk.StringVar()

# ---------- FRAME DO FORMULÁRIO ----------
frame_form = tk.LabelFrame(janela, text="Cadastro de Alunos", bg="#f4f4f4", padx=10, pady=10)
frame_form.pack(fill="x", padx=10, pady=10)

tk.Label(frame_form, text="Nome:", bg="#f4f4f4").grid(row=0, column=0, sticky="w")
tk.Entry(frame_form, textvariable=nome, width=20).grid(row=0, column=1, padx=5)

tk.Label(frame_form, text="Idade:", bg="#f4f4f4").grid(row=0, column=2, sticky="w")
tk.Entry(frame_form, textvariable=idade, width=5).grid(row=0, column=3, padx=5)

tk.Label(frame_form, text="Curso:", bg="#f4f4f4").grid(row=0, column=4, sticky="w")
tk.Entry(frame_form, textvariable=curso, width=15).grid(row=0, column=5, padx=5)

# Botões de ação
tk.Button(frame_form, text="Adicionar", bg="#4CAF50", fg="white", command=adicionar_aluno).grid(row=1, column=0, pady=5)
tk.Button(frame_form, text="Editar", bg="#2196F3", fg="white", command=editar_aluno).grid(row=1, column=1, pady=5)
tk.Button(frame_form, text="Salvar", bg="#FF9800", fg="white", command=salvar_edicao).grid(row=1, column=2, pady=5)
tk.Button(frame_form, text="Excluir", bg="#F44336", fg="white", command=excluir_aluno).grid(row=1, column=3, pady=5)
tk.Button(frame_form, text="Limpar", bg="#9E9E9E", fg="white", command=limpar_campos).grid(row=1, column=4, pady=5)

# ---------- FRAME DE BUSCA ----------
frame_busca = tk.Frame(janela, bg="#f4f4f4", pady=10)
frame_busca.pack(fill="x", padx=10)

tk.Label(frame_busca, text="Buscar:", bg="#f4f4f4").pack(side="left", padx=5)
tk.Entry(frame_busca, textvariable=busca, width=25).pack(side="left", padx=5)
tk.Button(frame_busca, text="🔍 Filtrar", command=buscar_aluno).pack(side="left", padx=5)

# ---------- TREEVIEW ----------
frame_tabela = tk.Frame(janela, padx=10, pady=10)
frame_tabela.pack(fill="both", expand=True)

colunas = ("Nome", "Idade", "Curso")
tree = ttk.Treeview(frame_tabela, columns=colunas, show="headings", height=15)

# Configurar cabeçalhos
for coluna in colunas:
    tree.heading(coluna, text=coluna)
    tree.column(coluna, width=200 if coluna == "Nome" else 100, anchor="center")

# Inserindo alguns dados iniciais
alunos_iniciais = [
    ("Gabriel", 18, "Informática"),
    ("Ana", 20, "Direito"),
    ("Pedro", 22, "Engenharia"),
    ("Mariana", 19, "História"),
    ("Lucas", 21, "Medicina")
]
for aluno in alunos_iniciais:
    tree.insert("", "end", values=aluno)

# Scrollbar
scroll = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scroll.set)
scroll.pack(side="right", fill="y")
tree.pack(fill="both", expand=True)

# ---------- EXECUTAR PROGRAMA ----------
janela.mainloop()