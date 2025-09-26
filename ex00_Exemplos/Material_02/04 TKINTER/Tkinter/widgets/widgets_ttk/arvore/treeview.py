import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import os

class TelaTreeview:
    def __init__(self, master=None):
        self.janela = tk.Toplevel(master)
        self.janela.title("Treeview")
        self.janela.geometry("700x500")

        caminho_icone = os.path.join(os.path.dirname(__file__), "../../../logo.ico")
        if os.path.exists(caminho_icone):
            self.janela.iconbitmap(caminho_icone)

        titulo = tk.Label(
            self.janela,
            text="Como funciona o Treeview no Tkinter",
            font=("Arial", 12, "bold")
        )
        titulo.pack(pady=10)

        texto_explicativo = (
            "O que é um Treeview?\n"
            "O Treeview é um widget do módulo ttk (do Tkinter) usado para exibir dados em forma de tabela ou hierarquia.\n\n"
            "Exemplo básico:\n"
            "import tkinter as tk\n"
            "from tkinter import ttk\n\n"
            "root = tk.Tk()\n"
            "tree = ttk.Treeview(root)\n"
            "tree['columns'] = ('Nome', 'Idade')\n"
            "tree.heading('#0', text='ID')\n"
            "tree.heading('Nome', text='Nome')\n"
            "tree.heading('Idade', text='Idade')\n"
            "tree.insert('', 'end', text='1', values=('Ana', 25))\n"
            "tree.pack()\n"
            "root.mainloop()\n\n"
            "Aplicações comuns:\n"
            "- Exibir tabelas\n"
            "- Estruturas hierárquicas como pastas\n"
            "- Interfaces com múltiplas colunas de dados\n"
        )

        area_texto = scrolledtext.ScrolledText(
            self.janela,
            wrap=tk.WORD,
            width=80,
            height=15,
            font=("Arial", 10)
        )
        area_texto.insert(tk.INSERT, texto_explicativo)
        area_texto.config(state='disabled')
        area_texto.pack(padx=10, pady=10)

        frame_botoes = tk.Frame(self.janela)
        frame_botoes.pack(pady=10)

        btn_simples = tk.Button(
            frame_botoes,
            text="Exemplo Simples",
            command=self.exemplo_treeview_simples,
            width=20
        )
        btn_simples.grid(row=0, column=0, padx=10)

        btn_colunas = tk.Button(
            frame_botoes,
            text="Exemplo com Colunas",
            command=self.exemplo_com_colunas,
            width=20
        )
        btn_colunas.grid(row=0, column=1, padx=10)

        btn_hierarquia = tk.Button(
            frame_botoes,
            text="Exemplo Hierárquico",
            command=self.exemplo_hierarquico,
            width=20
        )
        btn_hierarquia.grid(row=0, column=2, padx=10)

    def exemplo_treeview_simples(self):
        nova_janela = tk.Toplevel(self.janela)
        nova_janela.title("Treeview Simples")
        nova_janela.geometry("300x300")

        arvore = ttk.Treeview(nova_janela)
        arvore.insert('', 'end', text='Item 1')
        arvore.insert('', 'end', text='Item 2')
        arvore.insert('', 'end', text='Item 3')
        arvore.pack(fill='both', expand=True, padx=10, pady=10)

        def ao_clicar(event):
            item_id = arvore.focus()
            if item_id:
                texto = arvore.item(item_id, 'text')
                messagebox.showinfo("Item Selecionado", f"Você clicou em: {texto}")

        arvore.bind("<Double-1>", ao_clicar)

        frame = tk.Frame(nova_janela)
        frame.pack(pady=5)

        entry_texto = tk.Entry(frame, width=20)
        entry_texto.grid(row=0, column=0, padx=5)
        entry_texto.insert(0, "Novo Item")

        def inserir():
            texto = entry_texto.get().strip()
            if texto:
                arvore.insert('', 'end', text=texto)
                entry_texto.delete(0, tk.END)

        def excluir():
            item_id = arvore.focus()
            if item_id:
                arvore.delete(item_id)

        tk.Button(frame, text="Inserir", command=inserir).grid(row=0, column=1, padx=5)
        tk.Button(frame, text="Excluir", command=excluir).grid(row=0, column=2, padx=5)

    def exemplo_com_colunas(self):
        nova_janela = tk.Toplevel(self.janela)
        nova_janela.title("Treeview com Colunas")
        nova_janela.geometry("500x400")

        arvore = ttk.Treeview(nova_janela, columns=('Nome', 'Idade'), show='headings')
        arvore.heading('Nome', text='Nome')
        arvore.heading('Idade', text='Idade')
        arvore.column('Nome', width=150)
        arvore.column('Idade', width=80)

        dados = [('João', 30), ('Maria', 25), ('Pedro', 22)]
        for nome, idade in dados:
            arvore.insert('', 'end', values=(nome, idade))

        arvore.pack(fill='both', expand=True, padx=10, pady=10)

        def ao_clicar(event):
            item_id = arvore.focus()
            if item_id:
                valores = arvore.item(item_id, 'values')
                if valores:
                    messagebox.showinfo("Item Selecionado", f"Nome: {valores[0]}\nIdade: {valores[1]}")

        arvore.bind("<Double-1>", ao_clicar)

        frame_botoes = tk.Frame(nova_janela)
        frame_botoes.pack(pady=10)

        entry_nome = tk.Entry(frame_botoes, width=20)
        entry_nome.grid(row=0, column=0, padx=5)
        entry_nome.insert(0, "Nome")

        entry_idade = tk.Entry(frame_botoes, width=10)
        entry_idade.grid(row=0, column=1, padx=5)
        entry_idade.insert(0, "Idade")

        def inserir_item():
            nome = entry_nome.get().strip()
            idade = entry_idade.get().strip()
            if nome and idade.isdigit():
                arvore.insert('', 'end', values=(nome, int(idade)))
                entry_nome.delete(0, tk.END)
                entry_idade.delete(0, tk.END)

        def excluir_item():
            item_id = arvore.focus()
            if item_id:
                arvore.delete(item_id)

        tk.Button(frame_botoes, text="Inserir", command=inserir_item).grid(row=0, column=2, padx=5)
        tk.Button(frame_botoes, text="Excluir", command=excluir_item).grid(row=0, column=3, padx=5)

    def exemplo_hierarquico(self):
        nova_janela = tk.Toplevel(self.janela)
        nova_janela.title("Treeview Hierárquico")
        nova_janela.geometry("400x400")

        arvore = ttk.Treeview(nova_janela)
        arvore.heading('#0', text='Estrutura de Pastas')

        pasta1 = arvore.insert('', 'end', text='Documentos')
        arvore.insert(pasta1, 'end', text='Relatório.docx')
        arvore.insert(pasta1, 'end', text='Apresentação.pptx')

        pasta2 = arvore.insert('', 'end', text='Imagens')
        arvore.insert(pasta2, 'end', text='foto1.jpg')
        arvore.insert(pasta2, 'end', text='foto2.png')

        arvore.pack(fill='both', expand=True, padx=10, pady=10)

        def ao_clicar(event):
            item_id =arvore.focus()
            if item_id:
                texto = arvore.item(item_id, 'text')
                messagebox.showinfo("Item Selecionado", f"Você clicou em: {texto}")

        arvore.bind("<Double-1>", ao_clicar)

        frame = tk.Frame(nova_janela)
        frame.pack(pady=5)

        entry_texto = tk.Entry(frame, width=25)
        entry_texto.grid(row=0, column=0, padx=5)
        entry_texto.insert(0, "Novo item")

        def inserir():
            texto = entry_texto.get().strip()
            if texto:
                item_selecionado = arvore.focus()
                if item_selecionado:
                    arvore.insert(item_selecionado, 'end', text=texto)
                else:
                   arvore.insert('', 'end', text=texto)
                entry_texto.delete(0, tk.END)

        def excluir():
            item_id = arvore.focus()
            if item_id:
                arvore.delete(item_id)

        tk.Button(frame, text="Inserir", command=inserir).grid(row=0, column=1, padx=5)
        tk.Button(frame, text="Excluir", command=excluir).grid(row=0, column=2, padx=5)
    def iniciar(self):
        self.janela.mainloop()


