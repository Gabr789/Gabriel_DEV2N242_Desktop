import os
import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
from gerenciadores.gerenciadorword.gerenciador_word import GerenciadorWord
from Tkinter.imports import *  

class TelaFileDialog:
    def __init__(self, master=None):
        self.master = master
        self.janela = tk.Toplevel(master) if master else tk.Tk()
        self.janela.title("Filedialog")
        self.janela.geometry("800x600")
        self.gerenciador_arquivos = GerenciadorWord()
        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_janela)


        caminho_icone = os.path.join(os.path.dirname(__file__), "../../logo.ico")
        if os.path.exists(caminho_icone):
            self.janela.iconbitmap(caminho_icone)


        tk.Label(self.janela, text="Filedialog", font=("Arial", 16)).pack(pady=10)

        texto_explicativo = (
            "filedialog?\n"
            "O módulo filedialog do Tkinter fornece janelas prontas do sistema operacional para selecionar arquivos.\n"

            "Sintaxe básica:\n"
            "from tkinter import filedialog\n"
            "caminho_arquivo = filedialog.askopenfilename(\n"
            "    title='Selecionar arquivo',\n"
            "    filetypes=[('Arquivos Word', '*.docx'), ('Todos os arquivos', '*.*')]\n"
            ")\n\n"

            "Parâmetros:\n"
            "- title: Título da janela de seleção de arquivos.\n"
            "- filetypes: Filtros para exibir apenas determinados tipos de arquivos (ex: .docx).\n\n"

            "Retorno?\n"
            "- Retorna o caminho completo do arquivo selecionado (ex: C:/usuarios/nome/arquivo.docx).\n"
            "- Se o usuário cancelar, retorna uma string vazia.\n\n"

            "Vantagens:\n"
            "- Evita erros de digitação no nome do arquivo.\n"
            "- Permite ao usuário escolher qualquer arquivo de forma visual.\n"
            "- Funciona em Windows, Linux e macOS.\n\n"

            "Exemplo prático em uma interface:\n"
            "def selecionar_arquivo():\n"
            "    caminho = filedialog.askopenfilename(\n"
            "        title='Abrir Arquivo Word',\n"
            "        filetypes=[('Documentos Word', '*.docx')]\n"
            "    )\n"
            "    if caminho:\n"
            "        nome = os.path.basename(caminho)\n"
            "        print('Arquivo selecionado:', nome)\n\n"

        )

        self.area_texto = scrolledtext.ScrolledText(self.janela, wrap=tk.WORD, width=90, height=30)
        self.area_texto.insert(tk.INSERT, texto_explicativo)
        self.area_texto.config(state='disabled')
        self.area_texto.pack(padx=10, pady=10)
        tk.Button(self.janela, text="Abrir Tela de Edição", command=self.abrir_tela_edicao).pack(pady=10)
     
    def fechar_janela(self):
        if self.master:
            self.master.deiconify()  
        self.janela.destroy()
    def abrir_tela_edicao(self):
            tela_edicao = tk.Toplevel(self.janela)
            tela_edicao.title("Tela de Edição de Arquivos Word")
            tela_edicao.geometry("600x500")
            caminho_icone = os.path.join(os.path.dirname(__file__), "../../logo.ico")
            if os.path.exists(caminho_icone):
                tela_edicao.iconbitmap(caminho_icone)

            tk.Label(tela_edicao, text="Nome do arquivo:").pack(pady=(10, 0))
            entry_nome = tk.Entry(tela_edicao, width=40)
            entry_nome.pack(pady=5)
            entry_nome.insert(0, "arquivo.docx")

            tk.Label(tela_edicao, text="Conteúdo do arquivo:").pack(pady=(10, 0))
            area_texto = scrolledtext.ScrolledText(tela_edicao, wrap=tk.WORD, width=70, height=15)
            area_texto.pack(padx=10, pady=5)
            
            def selecionar_arquivo_word():
                    caminho_arquivo = filedialog.askopenfilename(
                        title="Selecionar arquivo Word",
                        filetypes=[("Documentos Word", "*.docx"), ("Todos os arquivos", "*.*")]
                    )
                    if caminho_arquivo:
                        nome_arquivo = os.path.basename(caminho_arquivo)
                        entry_nome.delete(0, tk.END)
                        entry_nome.insert(0, nome_arquivo)
                        try:
                            conteudo = self.gerenciador_arquivos.ler_arquivo(nome_arquivo)
                            area_texto.delete("1.0", tk.END)
                            area_texto.insert(tk.INSERT, conteudo)
                        except Exception as e:
                            messagebox.showerror("Erro", f"Erro ao abrir o arquivo:\n{str(e)}")





            tk.Button(tela_edicao, text="Selecionar Arquivo", command=selecionar_arquivo_word).pack(pady=5)
    
    def iniciar(self):
        self.janela.mainloop()