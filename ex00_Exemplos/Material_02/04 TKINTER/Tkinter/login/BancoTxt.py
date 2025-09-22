import os

class SimuladorBancoTxt:

    def __init__(self, caminho_arquivo="usuarios.txt"):
        self.caminho = caminho_arquivo
        self._criar_arquivo_se_nao_existir()

    def _criar_arquivo_se_nao_existir(self):
        if not os.path.exists(self.caminho):
            with open(self.caminho, 'w', encoding='utf-8') as f:
                f.write("admin:123\n") 

    def carregar_usuarios(self):
        usuarios = {}
        with open(self.caminho, 'r', encoding='utf-8') as f:
            for linha in f:
                if ':' in linha:
                    usuario, senha = linha.strip().split(':', 1)
                    usuarios[usuario] = senha
        return usuarios

    def salvar_usuario(self, usuario, senha):
        usuarios = self.carregar_usuarios()
        if usuario in usuarios:
            raise ValueError("Usuário já existe!")
        with open(self.caminho, 'a', encoding='utf-8') as f:
            f.write(f"{usuario}:{senha}\n")

    def validar_credenciais(self, usuario, senha):
        usuarios = self.carregar_usuarios()
        return usuarios.get(usuario) == senha