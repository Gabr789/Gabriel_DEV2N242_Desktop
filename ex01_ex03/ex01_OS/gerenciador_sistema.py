import os

class GerenciadorSistema:
    def __init__(self, diretorio_base=None):
        self.diretorio_base = diretorio_base or os.getcwd()

    def listarConteudo(self, caminho = None):
        return os.listdir(caminho) if caminho else os.listdir(self.diretorio_base)
    
    def diretorioAtual(self):
        return os.getcwd()
    
    def mudarDiretorio(self, novo_caminho):
        os.chdir(novo_caminho)
        self.diretorio_base = novo_caminho

    def juntarCaminho(self, *partes):
        return os.path.join(*partes)
    
    def existe(self, caminho):
        return os.path.exists(caminho)
    
    def criarDiretorio(self, nome, recursivo=False):
        caminho = os.path.join(self.diretorio_base, nome)
        if recursivo:
            os.makedirs(caminho, exist_ok=True)
        else:
            os.mkdir(caminho)
        return caminho
    
    def removerArquivo(self, nome_arquivo):
        caminho = os.path.join(self.diretorio_base, nome_arquivo)
        if os.path.isfile(caminho):
            os.remove(caminho)
            return True
        return False

    def removerDiretorio(self, nome_diretorio):
        caminho = os.path.join(self.diretorio_base, nome_diretorio)
        if os.path.isdir(caminho):
            os.rmdir(caminho)
            return True
        return False

    def renomear(self, nome_antigo, nome_novo):
        os.rename(nome_antigo, nome_novo)

    def pegarVariavelAmbiente(self, nome):
        return os.getenv(nome)