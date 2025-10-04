import tkinter as tk
from tkinter import ttk, messagebox
import os
from Tkinter.login.BancoMySQL import BancoMySQL


class TelaListaUsuarios:
    def __init__(self, master=None):
        self.master = master
        self.banco = BancoMySQL()
        self.janela = tk.Toplevel(master) if master else tk.Tk()
        self.janela.title("Lista de Usuários")
        self.janela.geometry("600x400")
        self.janela.configure(bg="white")
        self.janela.resizable(False, False)

        caminho_icone = os.path.join(os.path.dirname(__file__), "../logo.ico")
        if os.path.exists(caminho_icone):
            self.janela.iconbitmap(caminho_icone)

        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_janela)

        titulo = tk.Label(self.janela, text="Usuários Cadastrados", font=("Arial", 16), bg="white")
        titulo.pack(pady=10)

        self.frame_conteudo = tk.Frame(self.janela, bg="#f0f0f0", relief="sunken", bd=2)
        self.frame_conteudo.pack(expand=True, fill="both", padx=20, pady=20)

       
        self.treeview = ttk.Treeview(self.frame_conteudo, columns=("Usuário", "Perfil"), show="headings")
        self.treeview.heading("Usuário", text="Usuário")
        self.treeview.heading("Perfil", text="Perfil")
        self.treeview.column("Usuário", width=250)
        self.treeview.column("Perfil", width=150)
        self.treeview.pack(expand=True, fill="both", padx=10, pady=10)

        self.carregar_usuarios()

        btn_cadastrar = tk.Button(self.janela, text="Cadastrar", command=self.abrir_cadastro)
        btn_cadastrar.pack(side="left", padx=10, pady=10)

        btn_excluir = tk.Button(self.janela, text="Excluir", command=self.excluir_usuario)
        btn_excluir.pack(side="left", padx=10, pady=10)

        self.btn_atualizar = tk.Button(self.janela, text="Atualizar", command=self.abrir_edicao, state="disabled")
        self.btn_atualizar.pack(side="left", padx=10, pady=10)

        self.usuario_selecionado = None

        self.treeview.bind("<ButtonRelease-1>", self.on_treeview_select)
        self.treeview.bind("<Double-1>", self.on_double_click)

    def on_treeview_select(self, event):
        selecionado = self.treeview.selection()
        if selecionado:
            item_selecionado = selecionado[0]
            self.usuario_selecionado = self.treeview.item(item_selecionado)["values"]
            self.btn_atualizar.config(state="normal")
        else:
            self.usuario_selecionado = None
            self.btn_atualizar.config(state="disabled")

    def on_double_click(self, event):
        selecionado = self.treeview.selection()
        if selecionado:
            item_selecionado = selecionado[0]
            self.usuario_selecionado = self.treeview.item(item_selecionado)["values"]
            self.abrir_edicao()

    def carregar_usuarios(self):
        try:
            for item in self.treeview.get_children():
                self.treeview.delete(item)

            query = "SELECT usuario, perfil FROM usuarios"
            self.banco.cursor.execute(query)
            usuarios = self.banco.cursor.fetchall()

            for usuario in usuarios:
                self.treeview.insert("", "end", values=(usuario[0], usuario[1]))

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar os usuários: {e}")

    def excluir_usuario(self):
        selecionado = self.treeview.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um usuário para excluir.")
            return

        item_selecionado = selecionado[0]
        usuario = self.treeview.item(item_selecionado)["values"][0]
        query = "SELECT id FROM usuarios WHERE usuario = %s"
        self.banco.cursor.execute(query, (usuario,))
        usuario_id = self.banco.cursor.fetchone()

        if not usuario_id:
            messagebox.showerror("Erro", "Usuário não encontrado no banco de dados.")
            return

        resposta = messagebox.askyesno("Confirmar exclusão", f"Tem certeza que deseja excluir o usuário '{usuario}'?")
        if resposta:
            try:
                query_delete = "DELETE FROM usuarios WHERE id = %s"
                self.banco.cursor.execute(query_delete, (usuario_id[0],))
                self.banco.conexao.commit()

                self.treeview.delete(item_selecionado)
                messagebox.showinfo("Sucesso", f"Usuário '{usuario}' excluído com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao excluir o usuário: {e}")
            finally:
                self.carregar_usuarios()

    def abrir_edicao(self):
        if not self.usuario_selecionado:
            messagebox.showwarning("Aviso", "Selecione um usuário para editar.")
            return

        usuario = self.usuario_selecionado[0]

        edicao = tk.Toplevel(self.janela)
        edicao.title("Editar Usuário")
        edicao.geometry("300x300")
        edicao.configure(bg="white")
        edicao.resizable(False, False)

        caminho_icone = os.path.join(os.path.dirname(__file__), "../logo.ico")
        if os.path.exists(caminho_icone):
            edicao.iconbitmap(caminho_icone)

        tk.Label(edicao, text="Usuário:", bg="white").pack(pady=(15, 5))
        entrada_usuario = tk.Entry(edicao, highlightthickness=1, highlightbackground="green")
        entrada_usuario.pack(padx=20)
        entrada_usuario.insert(0, usuario)

        tk.Label(edicao, text="Nova Senha:", bg="white").pack(pady=(10, 5))
        entrada_senha = tk.Entry(edicao, show="*", highlightthickness=1, highlightbackground="green")
        entrada_senha.pack(padx=20)

      
        query_perfil = "SELECT perfil FROM usuarios WHERE usuario = %s"
        self.banco.cursor.execute(query_perfil, (usuario,))
        perfil_atual = self.banco.cursor.fetchone()
        perfil_atual = perfil_atual[0] if perfil_atual else "usuário"

        perfis = ["usuário", "moderador", "admin"]
        perfil_var = tk.StringVar(edicao)
        perfil_var.set(perfil_atual)

        tk.Label(edicao, text="Perfil:", bg="white").pack(pady=(10, 5))
        tk.OptionMenu(edicao, perfil_var, *perfis).pack(padx=20)

        def salvar_edicao():
            novo_usuario = entrada_usuario.get().strip()
            nova_senha = entrada_senha.get().strip()
            perfil_novo = perfil_var.get()

            if not novo_usuario or not nova_senha:
                messagebox.showerror("Erro", "Preencha usuário e senha!")
                return

            try:
                query_update = "UPDATE usuarios SET usuario = %s, senha = %s, perfil = %s WHERE usuario = %s"
                self.banco.cursor.execute(query_update, (novo_usuario, nova_senha, perfil_novo, usuario))
                self.banco.conexao.commit()

                messagebox.showinfo("Sucesso", f"Usuário '{novo_usuario}' atualizado com sucesso!")
                edicao.destroy()
                self.carregar_usuarios()

            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao atualizar os dados do usuário: {e}")

        tk.Button(edicao, text="Salvar", command=salvar_edicao, bg="green", fg="white").pack(pady=20)

    def abrir_cadastro(self):
        cadastro = tk.Toplevel(self.janela)
        cadastro.title("Cadastrar Usuário")
        cadastro.geometry("300x300")
        cadastro.configure(bg="white")
        cadastro.resizable(False, False)

        caminho_icone = os.path.join(os.path.dirname(__file__), "../logo.ico")
        if os.path.exists(caminho_icone):
            cadastro.iconbitmap(caminho_icone)

        tk.Label(cadastro, text="Novo Usuário:", bg="white").pack(pady=(15, 5))
        entrada_novo_usuario = tk.Entry(cadastro, highlightthickness=1, highlightbackground="green")
        entrada_novo_usuario.pack(padx=20)

        tk.Label(cadastro, text="Nova Senha:", bg="white").pack(pady=(10, 5))
        entrada_nova_senha = tk.Entry(cadastro, show="*", highlightthickness=1, highlightbackground="green")
        entrada_nova_senha.pack(padx=20)

        perfis = ["usuário", "moderador", "admin"]
        perfil_var = tk.StringVar(cadastro)
        perfil_var.set("usuário")

        tk.Label(cadastro, text="Perfil:", bg="white").pack(pady=(10, 5))
        tk.OptionMenu(cadastro, perfil_var, *perfis).pack(padx=20)

        def salvar_usuario():
            novo_usuario = entrada_novo_usuario.get().strip()
            nova_senha = entrada_nova_senha.get().strip()
            perfil = perfil_var.get()

            if not novo_usuario or not nova_senha:
                messagebox.showerror("Erro", "Preencha usuário e senha!")
                return

            try:
                self.banco.salvar_usuario(novo_usuario, nova_senha, perfil)
                messagebox.showinfo("Sucesso", f"Usuário '{novo_usuario}' cadastrado com sucesso!")
                cadastro.destroy()
                self.carregar_usuarios()

            except ValueError as e:
                messagebox.showerror("Erro", str(e))

        tk.Button(cadastro, text="Salvar", command=salvar_usuario, bg="green", fg="white").pack(pady=20)

    def fechar_janela(self):
        self.janela.destroy()

    def iniciar(self):
        self.janela.mainloop()