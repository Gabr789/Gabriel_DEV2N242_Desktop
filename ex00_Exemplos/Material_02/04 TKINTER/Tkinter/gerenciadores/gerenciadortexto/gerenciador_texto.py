import os

class GerenciadorTexto:

    def __init__(self, base_dir=None):
        self.base_dir = base_dir or os.getcwd()

    def definir_diretorio_base(self, caminho):
        if os.path.isdir(caminho):
            self.base_dir = caminho
        else:
            raise ValueError(f"Diretório inválido: {caminho}")

    def _caminho(self, nome):
        return os.path.join(self.base_dir, nome)

    def _abrir_arquivo(self, nome, modo='r', encoding='utf-8'):
        caminho = self._caminho(nome)
        return open(caminho, modo, encoding=encoding)

    def ler_arquivo(self, nome):
        with self._abrir_arquivo(nome) as arquivo:
            return arquivo.read()

    def escrever_arquivo(self, nome, texto, modo='w'):
        with self._abrir_arquivo(nome, modo) as arquivo:
            arquivo.write(texto)

    def existe(self, nome):
        return os.path.isfile(self._caminho(nome))

    def remover_arquivo(self, nome):
        caminho = self._caminho(nome)
        if os.path.isfile(caminho):
            os.remove(caminho)

    def renomear(self, antigo, novo):
        os.rename(self._caminho(antigo), self._caminho(novo))

    def contar_linhas(self, nome):
        with self._abrir_arquivo(nome) as arquivo:
            return sum(1 for _ in arquivo)

    def contar_palavras(self, nome):
        with self._abrir_arquivo(nome) as arquivo:
            return sum(len(linha.split()) for linha in arquivo)

    def substituir_texto(self, nome, texto_antigo, texto_novo):
        with self._abrir_arquivo(nome) as arquivo:
            conteudo = arquivo.read()
        conteudo = conteudo.replace(texto_antigo, texto_novo)
        self.escrever_arquivo(nome, conteudo, modo='w')

    def copiar_arquivo(self, origem, destino):
        with self._abrir_arquivo(origem) as arquivo_origem, self._abrir_arquivo(destino, 'w') as arquivo_destino:
            arquivo_destino.writelines(arquivo_origem)

    def criar_arquivo_teste(self, nome="arquivo_teste.txt"):
        conteudo = ""  
        self.escrever_arquivo(nome, conteudo, modo='w')