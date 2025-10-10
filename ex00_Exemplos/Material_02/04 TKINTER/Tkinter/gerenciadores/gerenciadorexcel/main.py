import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk, simpledialog
from tkinter.scrolledtext import ScrolledText
import pandas as pd
from gerenciadores.gerenciadorexcel.gerenciador_excel import GerenciadorExcel  
from datetime import datetime

class TelaExcel:
    def __init__(self, mestre=None):
        self.gerenciador = GerenciadorExcel()
        self.janela = tk.Tk() if mestre is None else tk.Toplevel(mestre)
        self.janela.title("Manipulação de Arquivos Excel")
        self.janela.geometry("700x600")

        texto_explicativo = (
            "O GerenciadorExcel é uma classe utilitária para manipulação de arquivos .xlsx (Excel).\n"
            "Permite criar, ler, editar, renomear, copiar e analisar planilhas Excel de forma simples.\n\n"
            "Leitura e escrita de arquivos Excel com pandas:\n"
            "- Usa a biblioteca pandas para manipular planilhas com facilidade.\n"
            "- A função pd.read_excel() lê o arquivo Excel e retorna um DataFrame.\n"
            "- A função to_excel() escreve um DataFrame em um arquivo Excel.\n\n"
            "Parâmetros importantes:\n"
            "- nome: nome do arquivo Excel (com extensão .xlsx).\n"
            "- sheet_name: nome ou índice da planilha a ser lida ou escrita.\n"
            "- modo: modo de abertura para escrita w para sobrescrever, a para anexar/atualizar.\n\n"
            "Métodos disponíveis:\n"
            "- ler_arquivo(nome, sheet_name=0): Lê a planilha especificada e retorna um DataFrame.\n"
            "- escrever_arquivo(nome, dataframe, sheet_name='Sheet1', modo='w'): Salva o DataFrame em uma planilha.\n"
            "- existe(nome): Verifica se o arquivo existe no diretório base.\n"
            "- remover_arquivo(nome): Exclui o arquivo especificado.\n"
            "- renomear(antigo, novo): Renomeia um arquivo Excel.\n"
            "- contar_linhas(nome, sheet_name=0): Retorna a quantidade de linhas da planilha.\n"
            "- contar_colunas(nome, sheet_name=0): Retorna a quantidade de colunas da planilha.\n"
            "- substituir_valores(nome, coluna, valor_antigo, valor_novo, sheet_name=0): Substitui valores na coluna.\n"
            "- copiar_arquivo(origem, destino): Copia o arquivo Excel de origem para destino.\n\n"
            "Exemplo de uso básico:\n"
            "    gerenciador = GerenciadorExcel()\n"
            "    df = gerenciador.ler_arquivo(dados.xlsx)\n"
            "    df[Coluna] = df[Coluna].replace(Antigo, Novo)\n"
            "    gerenciador.escrever_arquivo(dados_atualizados.xlsx, df)\n\n"
            "Requisitos:\n"
            "- pandas\n"
            "- openpyxl (para ler e salvar arquivos Excel)\n"
            "- Ambos podem ser instalados via pip: pip install pandas openpyxl\n"
        )

        self.area_texto = ScrolledText(self.janela, wrap=tk.WORD, height=8, font=("Arial", 10))
        self.area_texto.insert(tk.END, texto_explicativo)
        self.area_texto.config(state=tk.DISABLED)
        self.area_texto.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        btn_interacoes = tk.Button(self.janela, text="Interações com Excel", command=self.abrir_janela_interacoes)
        btn_interacoes.pack(pady=10)

        self.tabela = None
        self.dados = pd.DataFrame()
        self.nome_arquivo = None
        self.janela_interacoes = None

    def abrir_janela_interacoes(self):
        if self.janela_interacoes and tk.Toplevel.winfo_exists(self.janela_interacoes):
            self.janela_interacoes.focus()
            return
        
        self.janela_interacoes = tk.Toplevel(self.janela)
        self.janela_interacoes.title("Interações com Excel")
        self.janela_interacoes.geometry("800x800")

        frame_botoes = tk.Frame(self.janela_interacoes)
        frame_botoes.pack(fill=tk.X, padx=10, pady=10)

        tk.Button(frame_botoes, text="Criar Arquivo de Teste", command=self.criar_arquivo).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="Abrir Arquivo Excel", command=self.abrir_arquivo_excel).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="Deletar Arquivo", command=self.deletar_arquivo).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="Renomear Arquivo", command=self.renomear_arquivo).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="Adicionar Cálculos", command=self.adicionar_colunas_calculadas).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="Modificar Linha Selecionada", command=self.modificar_linha).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="Excluir Linha Selecionada", command=self.excluir_linha).pack(side=tk.LEFT, padx=5)

        self.tabela = ttk.Treeview(self.janela_interacoes)
        self.tabela.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    def criar_arquivo(self):
        agora = datetime.now()
        nome_arquivo = "relatorio_alunos_" + agora.strftime("%d_%m_%Y_%H_%M_%S.xlsx")
        self.gerenciador.criar_arquivo(nome_arquivo)
        messagebox.showinfo("Sucesso", f"Arquivo {nome_arquivo} criado com sucesso!")

    def abrir_arquivo_excel(self):
        caminho_arquivo = filedialog.askopenfilename(
            title="Abrir Arquivo Excel",
            filetypes=[("Arquivos Excel", "*.xlsx")]
        )

        if not caminho_arquivo:
            return

        try:
            self.nome_arquivo = os.path.basename(caminho_arquivo)
            pasta = os.path.dirname(caminho_arquivo)
            self.gerenciador.definir_pasta_base(pasta)

            self.dados = self.gerenciador.ler_arquivo(self.nome_arquivo)
            self.mostrar_tabela(self.dados)

        except Exception as erro:
            messagebox.showerror("Erro", f"Não foi possível abrir o arquivo:\n{str(erro)}")

    def mostrar_tabela(self, dados_df):
        if not self.tabela:
            return

        self.tabela.delete(*self.tabela.get_children())

        self.tabela["columns"] = list(dados_df.columns)
        self.tabela["show"] = "headings"

        for nome_coluna in dados_df.columns:
            self.tabela.heading(nome_coluna, text=nome_coluna)
            self.tabela.column(nome_coluna, anchor="center")

        for _, linha in dados_df.iterrows():
            self.tabela.insert("", "end", values=list(linha))

    def deletar_arquivo(self):
        if not self.nome_arquivo:
            messagebox.showwarning("Aviso", "Nenhum arquivo foi carregado.")
            return

        confirmacao = messagebox.askyesno("Confirmar", f"Deseja deletar {self.nome_arquivo}?")
        if confirmacao:
            try:
                self.gerenciador.remover_arquivo(self.nome_arquivo)
                self.nome_arquivo = None
                self.dados = pd.DataFrame()
                self.mostrar_tabela(self.dados)
                messagebox.showinfo("Sucesso", "Arquivo deletado com sucesso.")
            except Exception as erro:
                messagebox.showerror("Erro", f"Erro ao deletar o arquivo:\n{str(erro)}")

    def renomear_arquivo(self):
        if not self.nome_arquivo:
            messagebox.showwarning("Aviso", "Nenhum arquivo foi carregado.")
            return

        novo_nome = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Arquivos Excel", "*.xlsx")])
        if not novo_nome:
            return

        try:
            novo_nome = os.path.basename(novo_nome)
            self.gerenciador.renomear(self.nome_arquivo, novo_nome)
            self.nome_arquivo = novo_nome
            messagebox.showinfo("Sucesso", f"Arquivo renomeado para: {novo_nome}")
        except Exception as erro:
            messagebox.showerror("Erro", f"Erro ao renomear arquivo:\n{str(erro)}")

    def adicionar_colunas_calculadas(self):
            if self.dados.empty:
                messagebox.showwarning("Aviso", "Nenhum arquivo foi carregado.")
                return

            if 'Valor1' not in self.dados.columns or 'Valor2' not in self.dados.columns:
                messagebox.showwarning("Erro", "As colunas Valor1 e Valor2 são necessárias.")
                return

            try:
                self.dados['Valor1'] = pd.to_numeric(self.dados['Valor1'], errors='coerce')
                self.dados['Valor2'] = pd.to_numeric(self.dados['Valor2'], errors='coerce')

                self.dados['Soma'] = self.dados['Valor1'] + self.dados['Valor2']
                self.dados['Subtração'] = self.dados['Valor1'] - self.dados['Valor2']
                self.dados['Multiplicação'] = self.dados['Valor1'] * self.dados['Valor2']
                self.dados['Divisão'] = self.dados['Valor1'] / self.dados['Valor2']
                self.dados['Porcentagem'] = (self.dados['Valor1'] / self.dados['Valor2']) * 100

                self.dados.replace([float('inf'), float('-inf')], None, inplace=True)

                self.mostrar_tabela(self.dados)
                self.salvar_dados()  
                messagebox.showinfo("Sucesso", "Operações adicionadas com sucesso e salvas no arquivo!")

            except ZeroDivisionError:
                messagebox.showerror("Erro", "Divisão por zero encontrada em 'Valor2'.")
            except Exception as erro:
                messagebox.showerror("Erro", f"Ocorreu um erro ao adicionar operações:\n{str(erro)}")

    def modificar_linha(self):
        if self.dados.empty:
            messagebox.showwarning("Aviso", "Nenhum arquivo foi carregado.")
            return

        selecionado = self.tabela.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione uma linha para modificar.")
            return

        idx = self.tabela.index(selecionado[0])
        valores = self.dados.iloc[idx].tolist()

        editar_janela = tk.Toplevel(self.janela_interacoes)
        editar_janela.title("Modificar Linha")
        editar_janela.geometry("600x600")
        editar_janela.transient(self.janela_interacoes)
        editar_janela.grab_set()

        entradas = {}

        for i, coluna in enumerate(self.dados.columns):
            tk.Label(editar_janela, text=coluna).grid(row=i, column=0, sticky="w", padx=10, pady=5)
            entry = tk.Entry(editar_janela)
            entry.grid(row=i, column=1, padx=10, pady=5)
            entry.insert(0, valores[i])
            entradas[coluna] = entry

        def salvar():
            try:
                for coluna, entry in entradas.items():
                    valor = entry.get()
                    try:
                        val = float(valor)
                        if val.is_integer():
                            val = int(val)
                        self.dados.at[idx, coluna] = val
                    except ValueError:
                        self.dados.at[idx, coluna] = valor
                self.mostrar_tabela(self.dados)
                self.salvar_dados()
                messagebox.showinfo("Sucesso", "Linha modificada com sucesso e salva no arquivo.")
                editar_janela.destroy()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao salvar os dados:\n{str(e)}")

        
        def cancelar():
            editar_janela.destroy()

        btn_salvar = tk.Button(editar_janela, text="Salvar", command=salvar)
        btn_salvar.grid(row=len(self.dados.columns), column=1, sticky="e", padx=10, pady=10)

        btn_cancelar = tk.Button(editar_janela, text="Cancelar", command=cancelar)
        btn_cancelar.grid(row=len(self.dados.columns), column=0, sticky="w", padx=10, pady=10)

    def excluir_linha(self):
        if self.dados.empty:
            messagebox.showwarning("Aviso", "Nenhum arquivo foi carregado.")
            return

        selecionado = self.tabela.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione uma linha para excluir.")
            return

        confirmacao = messagebox.askyesno("Confirmar", "Deseja realmente excluir a linha selecionada?")
        if not confirmacao:
            return

        idx = self.tabela.index(selecionado[0])

        self.dados = self.dados.drop(self.dados.index[idx]).reset_index(drop=True)

        self.mostrar_tabela(self.dados)
        self.salvar_dados()
        messagebox.showinfo("Sucesso", "Linha excluída com sucesso e arquivo atualizado.")

    def salvar_dados(self):
        if not self.nome_arquivo:
            messagebox.showwarning("Aviso", "Nenhum arquivo para salvar.")
            return
        try:
           
            self.gerenciador.escrever_arquivo(self.nome_arquivo, self.dados, nome_planilha='Planilha1')
        except PermissionError:
            messagebox.showerror("Erro", "O arquivo está aberto em outro programa (como Excel). Feche o arquivo e tente novamente.")
        except Exception as erro:
            messagebox.showerror("Erro", f"Erro ao salvar arquivo:\n{str(erro)}")

    def iniciar(self):
        self.janela.mainloop()

if __name__ == "__main__":
    app = TelaExcel()
    app.iniciar()