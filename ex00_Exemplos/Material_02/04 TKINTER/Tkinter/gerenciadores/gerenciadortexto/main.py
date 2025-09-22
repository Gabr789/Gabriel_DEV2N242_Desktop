import os
import tkinter as tk
from tkinter import scrolledtext, messagebox
from gerenciadores.gerenciadortexto.gerenciador_texto import GerenciadorTexto
from tkinter import filedialog
class TelaArquivos:
    def __init__(self, master=None):
       
        self.janela = tk.Toplevel(master) if master else tk.Tk()
        self.janela.title("Manipulação de Arquivos")
        self.janela.geometry("700x600")

      
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../logo.ico")
        if os.path.exists(caminho_icone):
            self.janela.iconbitmap(caminho_icone)

       
        tk.Label(self.janela, text="Manipulação de Arquivos", font=("Arial", 16), bg="white").pack(pady=10)
        tk.Label(self.janela, text="Exemplo de uso da classe GerenciadorTexto").pack(pady=5)

       
        texto_explicativo = (
            "O GerenciadorTexto é uma classe utilitária para manipulação de arquivos '.txt'.\n"
            "Permite criar, ler, editar, renomear, copiar e analisar arquivos de texto de forma simples.\n\n"

            "Abertura de arquivos com 'with open(...) as arquivo_destino':\n"
            "- Utiliza o gerenciador de contexto 'with' para abrir arquivos com segurança.\n"
            "- Garante que o arquivo será fechado automaticamente após o uso, mesmo se ocorrerem erros.\n"
            "- Exemplo:\n"
            "    with open('arquivo.txt', 'r', encoding='utf-8') as arquivo_destino:\n"
            "        conteudo = arquivo_destino.read()\n"
            "- Nesse exemplo:\n"
            "    'arquivo.txt' é o nome do arquivo.\n"
            "    'r' é o modo de leitura.\n"
            "    'encoding=\"utf-8\"' define a codificação de caracteres.\n"
            "    'arquivo_destino' é o nome da variável que representa o arquivo aberto dentro do bloco.\n\n"

            "Modos de abertura de arquivos:\n"
            "- 'r': modo de leitura (read) — abre o arquivo para leitura.\n"
            "- 'w': modo de escrita (write) — cria ou sobrescreve o arquivo.\n"
            "- 'a': modo de anexação (append) — adiciona conteúdo ao final do arquivo existente.\n"
            "- 'x': modo de criação (exclusive) — cria novo arquivo e gera erro se já existir.\n\n"

            "Codificação:\n"
            "- 'utf-8': padrão de codificação que suporta acentuação e caracteres especiais.\n\n"

            "Funções e métodos importantes usados:\n"
            "- os.getcwd(): Retorna o diretório atual de trabalho, ou seja, o caminho onde o programa está executando.\n"
            "- arquivo_destino.read(): Lê e retorna o conteúdo completo do arquivo aberto.\n"
            "- arquivo_destino.write(texto): Escreve o texto passado dentro do arquivo aberto, adicionando ou sobrescrevendo o conteúdo dependendo do modo.\n\n"

            "Métodos disponíveis:\n"
            "- ler_arquivo(nome): Lê e retorna o conteúdo de um arquivo.\n"
            "- escrever_arquivo(nome, texto, modo='w'): Escreve texto em um arquivo usando o modo especificado.\n"
            "- existe(nome): Verifica se o arquivo existe no diretório base.\n"
            "- remover_arquivo(nome): Exclui o arquivo especificado.\n"
            "- renomear(antigo, novo): Renomeia um arquivo.\n"
            "- contar_linhas(nome): Conta o número de linhas em um arquivo.\n"
            "- contar_palavras(nome): Conta o número de palavras em um arquivo.\n"
            "- substituir_texto(nome, texto_antigo, texto_novo): Substitui um texto por outro dentro do arquivo.\n"
            "- copiar_arquivo(origem, destino): Copia o conteúdo de um arquivo para outro.\n"
        )

        self.area_texto = scrolledtext.ScrolledText(
            self.janela,
            wrap=tk.WORD,
            width=80,
            height=15,
            font=("Arial", 10)
        )
        self.area_texto.insert(tk.INSERT, texto_explicativo)
        self.area_texto.config(state='disabled')
        self.area_texto.pack(padx=10, pady=10)


        self.gerenciador_arquivos = GerenciadorTexto()

        tk.Button(self.janela, text="Abrir Tela de Edição", command=self.abrir_tela_edicao).pack(pady=10)

    def criar_arquivo_teste(self):
        self.gerenciador_arquivos.criar_arquivo_teste()
        messagebox.showinfo("Sucesso", "Arquivo de teste criado com sucesso!")

    def ler_arquivo_teste(self):
        if not self.gerenciador_arquivos.existe("arquivo_teste.txt"):
            messagebox.showwarning("Aviso", "Arquivo não encontrado!")
            return
        conteudo = self.gerenciador_arquivos.ler_arquivo("arquivo_teste.txt")

     
        janela_conteudo = tk.Toplevel(self.janela)
        janela_conteudo.title("Conteúdo do Arquivo")
        scrolled_area = scrolledtext.ScrolledText(janela_conteudo, wrap=tk.WORD, width=60, height=20)
        scrolled_area.insert(tk.INSERT, conteudo)
        scrolled_area.config(state='disabled')
        scrolled_area.pack(padx=10, pady=10)

    def contar_arquivo_teste(self):
        if not self.gerenciador_arquivos.existe("arquivo_teste.txt"):
            messagebox.showwarning("Aviso", "Arquivo não encontrado!")
            return
        linhas = self.gerenciador_arquivos.contar_linhas("arquivo_teste.txt")
        palavras = self.gerenciador_arquivos.contar_palavras("arquivo_teste.txt")
        messagebox.showinfo("Contagem", f"Linhas: {linhas}\nPalavras: {palavras}")

    def excluir_arquivo_teste(self):
        if not self.gerenciador_arquivos.existe("arquivo_teste.txt"):
            messagebox.showwarning("Aviso", "Arquivo não encontrado!")
            return
        self.gerenciador_arquivos.remover_arquivo("arquivo_teste.txt")
        messagebox.showinfo("Sucesso", "Arquivo de teste excluído com sucesso!")

    def abrir_tela_edicao(self):
      
        tela_edicao = tk.Toplevel(self.janela)
        tela_edicao.title("Tela de Edição de Arquivos")
        tela_edicao.geometry("600x500")
        caminho_icone = os.path.join(os.path.dirname(__file__), "../../logo.ico")
        if os.path.exists(caminho_icone):
            tela_edicao.iconbitmap(caminho_icone)

        
        tk.Label(tela_edicao, text="Nome do arquivo:").pack(pady=(10, 0))
        entry_nome = tk.Entry(tela_edicao, width=40)
        entry_nome.pack(pady=5)
        entry_nome.insert(0, "arquivo.txt")  # valor padrão

       
        tk.Label(tela_edicao, text="Conteúdo do arquivo:").pack(pady=(10, 0))
        area_texto = scrolledtext.ScrolledText(tela_edicao, wrap=tk.WORD, width=70, height=15)
        area_texto.pack(padx=10, pady=5)

        def selecionar_arquivo_edicao():
         caminho_arquivo = filedialog.askopenfilename(
            title="Selecionar arquivo para edição",
            filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")]
         )
       
         if caminho_arquivo:
                nome_arquivo = os.path.basename(caminho_arquivo)
                entry_nome.delete(0, tk.END)
                entry_nome.insert(0, nome_arquivo)
                try:
                    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                        conteudo = arquivo.read()
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
        tk.Button(tela_edicao, text="Selecionar Arquivo", command=selecionar_arquivo_edicao).pack(pady=5)

    def iniciar(self):
        self.janela.mainloop()


if __name__ == "__main__":
    tela = TelaArquivos()
    tela.iniciar()