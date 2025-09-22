import os
import tkinter as tk
from tkinter import scrolledtext, messagebox
from gerenciadores.gerenciadorword.gerenciador_word import GerenciadorWord
from tkinter import filedialog
class TelaArquivosWord:
    def __init__(self, master=None):
        self.janela = tk.Toplevel(master) if master else tk.Tk()
        self.janela.title("Manipulação de Arquivos Word")
        self.janela.geometry("700x600")

    
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../logo.ico")
        if os.path.exists(caminho_icone):
            self.janela.iconbitmap(caminho_icone)

        tk.Label(self.janela, text="Manipulação de Arquivos Word (.docx)", font=("Arial", 16)).pack(pady=10)

        texto_explicativo = (
            "O GerenciadorWord é uma classe utilitária para manipulação de arquivos do Word (.docx)."
            "Permite criar, ler, editar, renomear, copiar e analisar documentos formatados de forma simples e eficiente.\n\n"

            "Manipulação de arquivos Word:"
            "- Utiliza a biblioteca python-docx para abrir, modificar e salvar documentos .docx.\n"
            "- Permite trabalhar com o conteúdo estrutural do documento, como parágrafos, mantendo a formatação básica.\n"
            "- Exemplo básico para abrir um documento:\n"
            " python\n" " from docx import Document\n" " doc = Document('arquivo.docx')\n" " texto = '\\n'.join(paragraph.text for paragraph in doc.paragraphs)\n" " \n"
            "- Nesse exemplo:\n"
            " - 'arquivo.docx' é o nome do arquivo.\n"
            " - Document() abre o documento para manipulação.\n"
            " - doc.paragraphs é uma lista dos parágrafos do documento.\n"
            " - paragraph.text acessa o texto de cada parágrafo.\n\n"

            "Operações na manipulação de arquivos .docx:"
            "- Para criar um documento vazio e adicionar conteúdo, instanciamos Document() sem argumentos.\n"
            "- O método add_paragraph(texto) adiciona um novo parágrafo ao documento.\n"
            "- save(caminho) grava as alterações no arquivo, criando ou sobrescrevendo.\n"
            "- Para modificar texto existente, iteramos sobre doc.paragraphs e substituímos o conteúdo de paragraph.text.\n\n"

            "Manejo de arquivos e caminhos:"
            "- Usa o módulo os para montar caminhos completos de arquivos com os.path.join e garantir portabilidade entre sistemas operacionais.\n"
            "- Verifica a existência de arquivos com os.path.isfile para evitar erros.\n"
            "- Remove arquivos usando os.remove de forma segura após verificação.\n"
            "- Renomeia arquivos com os.rename, garantindo manipulação simples de nomes e organização.\n\n"

            "Métodos usados:"
            "- Document(caminho): abre um documento Word existente para leitura ou edição.\n"
            "- doc.add_paragraph(texto): adiciona texto como novo parágrafo.\n"
            "- doc.save(caminho): salva o documento no caminho especificado.\n"
            "- os.path.isfile(caminho): verifica se o arquivo existe.\n"
            "- os.remove(caminho): exclui um arquivo.\n"
            "- os.rename(caminho_antigo, caminho_novo): renomeia um arquivo.\n"
            "- Para leitura, iteramos doc.paragraphs e extraímos o texto com paragraph.text.\n"
            "- Para substituição de texto, modificamos paragraph.text diretamente e salvamos novamente.\n\n"

            "Métodos disponíveis no GerenciadorWord:"
            "- criar_arquivo_teste(nome): cria um documento Word com texto padrão para testes.\n"
            "- ler_arquivo(nome): lê e retorna todo o conteúdo textual do documento, unindo parágrafos.\n"
            "- escrever_arquivo(nome, texto): cria ou sobrescreve um documento, dividindo o texto em parágrafos.\n"
            "- remover_arquivo(nome): exclui o arquivo do sistema.\n"
            "- renomear(antigo, novo): altera o nome de um arquivo existente.\n"
            "- contar_linhas(nome): conta o número de parágrafos no documento.\n"
            "- contar_palavras(nome): conta todas as palavras do documento.\n"
            "- substituir_texto(nome, texto_antigo, texto_novo): procura e substitui texto dentro dos parágrafos.\n"
            "- copiar_arquivo(origem, destino): copia o arquivo inteiro byte a byte para outro caminho.\n"
        )

        self.area_texto = scrolledtext.ScrolledText(self.janela, wrap=tk.WORD, width=80, height=15)
        self.area_texto.insert(tk.INSERT, texto_explicativo)
        self.area_texto.config(state='disabled')
        self.area_texto.pack(padx=10, pady=10)

        self.gerenciador_arquivos = GerenciadorWord()

 
        tk.Button(self.janela, text="Criar Arquivo de Teste", command=self.criar_arquivo_teste).pack(pady=5)
        tk.Button(self.janela, text="Ler Arquivo de Teste", command=self.ler_arquivo).pack(pady=5)
        tk.Button(self.janela, text="Contar Linhas/Palavras", command=self.contar_arquivo).pack(pady=5)
        tk.Button(self.janela, text="Excluir Arquivo de Teste", command=self.excluir_arquivo).pack(pady=5)
        tk.Button(self.janela, text="Abrir Tela de Edição", command=self.abrir_tela_edicao).pack(pady=10)

    def criar_arquivo_teste(self):
        self.gerenciador_arquivos.criar_arquivo_teste("arquivo_teste.docx")
        messagebox.showinfo("Sucesso", "Arquivo de teste criado com sucesso!")

    def ler_arquivo(self):
        nome = "arquivo_teste.docx"
        if not self.gerenciador_arquivos.existe(nome):
            messagebox.showwarning("Aviso", "Arquivo não encontrado!")
            return
        conteudo = self.gerenciador_arquivos.ler_arquivo(nome)

        janela_conteudo = tk.Toplevel(self.janela)
        janela_conteudo.title("Conteúdo do Arquivo")
        scrolled_area = scrolledtext.ScrolledText(janela_conteudo, wrap=tk.WORD, width=60, height=20)
        scrolled_area.insert(tk.INSERT, conteudo)
        scrolled_area.config(state='disabled')
        scrolled_area.pack(padx=10, pady=10)

    def contar_arquivo(self):
        nome = "arquivo_teste.docx"
        if not self.gerenciador_arquivos.existe(nome):
            messagebox.showwarning("Aviso", "Arquivo não encontrado!")
            return
        linhas = self.gerenciador_arquivos.contar_linhas(nome)
        palavras = self.gerenciador_arquivos.contar_palavras(nome)
        messagebox.showinfo("Contagem", f"Linhas: {linhas}\nPalavras: {palavras}")

    def excluir_arquivo(self):
        nome = "arquivo_teste.docx"
        if not self.gerenciador_arquivos.existe(nome):
            messagebox.showwarning("Aviso", "Arquivo não encontrado!")
            return
        self.gerenciador_arquivos.remover_arquivo(nome)
        messagebox.showinfo("Sucesso", "Arquivo de teste excluído com sucesso!")

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
        def criar():
            nome = entry_nome.get()
            conteudo = area_texto.get("1.0", tk.END)
            self.gerenciador_arquivos.escrever_arquivo(nome, conteudo)
            messagebox.showinfo("Sucesso", f"Arquivo '{nome}' criado/atualizado com sucesso!")

        def ler():
            nome = entry_nome.get()
            if not self.gerenciador_arquivos.existe(nome):
                messagebox.showwarning("Aviso", "Arquivo não encontrado!")
                return
            conteudo = self.gerenciador_arquivos.ler_arquivo(nome)
            area_texto.delete("1.0", tk.END)
            area_texto.insert(tk.INSERT, conteudo)

        def excluir():
            nome = entry_nome.get()
            if not self.gerenciador_arquivos.existe(nome):
                messagebox.showwarning("Aviso", "Arquivo não encontrado!")
                return
            self.gerenciador_arquivos.remover_arquivo(nome)
            area_texto.delete("1.0", tk.END)
            messagebox.showinfo("Sucesso", f"Arquivo '{nome}' excluído com sucesso!")

        tk.Button(tela_edicao, text="Criar/Atualizar", command=criar).pack(pady=5)
        tk.Button(tela_edicao, text="Ler", command=ler).pack(pady=5)
        tk.Button(tela_edicao, text="Excluir", command=excluir).pack(pady=5)
        tk.Button(tela_edicao, text="Selecionar Arquivo", command=selecionar_arquivo_word).pack(pady=5)

    def iniciar(self):
        self.janela.mainloop()

if __name__ == "__main__":
    tela = TelaArquivosWord()
    tela.iniciar()