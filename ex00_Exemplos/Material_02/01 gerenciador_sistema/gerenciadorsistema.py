import os

class GerenciadorSistema:
    """
    Atributos:
        base_dir (str): Diretório base para operações que usam caminhos relativos.
                        Por padrão, é o diretório atual os.getcwd().

    Métodos:
        listar_conteudo(caminho=None): Lista arquivos e pastas em um diretório.
        diretorio_atual(): Retorna o diretório atual de trabalho.
        mudar_diretorio(novo_caminho): Altera o diretório atual de trabalho.
        juntar_caminho(*partes): Junta partes de caminho em um único caminho.
        existe(caminho): Verifica se um arquivo ou diretório existe.
        criar_diretorio(nome, recursivo=False): Cria um diretório (ou estrutura de diretórios).
        remover_arquivo(nome_arquivo): Remove um arquivo.
        remover_diretorio(nome_diretorio): Remove um diretório vazio.
        renomear(antigo, novo): Renomeia arquivo ou diretório.
        pegar_variavel_ambiente(nome): Obtém o valor de uma variável de ambiente.
    """

    def __init__(self, base_dir=None):
        """
        Inicializa a instância do GerenciadorSistema.

        Args:
            base_dir (str, opcional): Diretório base para operações.
                Se None, utiliza o diretório atual do processo os.getcwd().
                Isso é feito com base_dir or os.getcwd() para garantir
                que sempre haja um caminho válido.
        """
        self.base_dir = base_dir or os.getcwd()

    def listar_conteudo(self, caminho=None):
        """
        Lista o conteúdo do diretório especificado.

        Args:
            caminho: Caminho do diretório.
                Se None, usa o base_dir da instância.

        Return:
            list: Lista de nomes de arquivos e pastas.

        Motivo do uso do parâmetro padrão None:
            Permite usar um diretório padrão base_dir quando o usuário não informa o caminho.
        """
        caminho = caminho or self.base_dir
        return os.listdir(caminho)

    def diretorio_atual(self):
        """
        Retorna o diretório atual de trabalho do processo.

        Return:
            str: Caminho absoluto do diretório atual.

        Usa diretamente os.getcwd() para pegar o caminho atual,
        pois é uma operação simples.
        """
        return os.getcwd()

    def mudar_diretorio(self, novo_caminho):
        """
        Muda o diretório atual de trabalho para o especificado.

        Args:
            novo_caminho: Novo diretório.

        Também atualiza o atributo base_dir para manter o estado da instância
        com o diretório atual.
        """
        os.chdir(novo_caminho)
        self.base_dir = novo_caminho

    def juntar_caminho(self, *partes):
        """
        Junta múltiplas partes de caminho em um caminho válido para o sistema.

        Args:
            *partes: Partes do caminho para juntar.

        Return:
           Caminho completo resultante.

        Usa os.path.join para garantir compatibilidade entre sistemas operacionais.
        """
        return os.path.join(*partes)

    def existe(self, caminho):
        """
        Verifica se o caminho arquivo ou diretório existe.

        Args:
            caminho: Caminho a verificar.

        Return:
            bool: True se existir, False caso contrário.

        Usa os.path.exists para verificar a existência do caminho.
        """
        return os.path.exists(caminho)

    def criar_diretorio(self, nome, recursivo=False):
        """
        Cria um diretório relativo ao base_dir.

        Args:
            nome: Nome do diretório a ser criado.
            recursivo (bool): Se True, cria diretórios intermediários.

        Return:
            Caminho absoluto do diretório criado.

        Explicação do parâmetro recursivo:
            Quando True, usa os.makedirs para criar toda a estrutura,
            evitando erro se diretórios intermediários não existirem.
            Caso contrário, usa os.mkdir para criar apenas o último diretório.
        """
        caminho = os.path.join(self.base_dir, nome)
        if recursivo:
            os.makedirs(caminho, exist_ok=True)
        else:
            os.mkdir(caminho)
        return caminho

    def remover_arquivo(self, nome_arquivo):
        """
        Remove um arquivo relativo ao base_dir, se existir.

        Args:
            nome_arquivo: Nome do arquivo.

        Verifica antes se é arquivo com os.path.isfile para evitar erros.
        """
        caminho = os.path.join(self.base_dir, nome_arquivo)
        if os.path.isfile(caminho):
            os.remove(caminho)

    def remover_diretorio(self, nome_diretorio):
        """
        Remove um diretório vazio relativo ao base_dir.

        Args:
            nome_diretorio: Nome do diretório.

        Usa os.rmdir, que só remove diretórios vazios.
        """
        caminho = os.path.join(self.base_dir, nome_diretorio)
        if os.path.isdir(caminho):
            os.rmdir(caminho)

    def renomear(self, antigo, novo):
        """
        Renomeia arquivo ou diretório.

        Args:
            antigo: Caminho antigo.
            novo: Novo caminho ou nome.

        Usa os.rename para realizar a operação.
        """
        os.rename(antigo, novo)

    def pegar_variavel_ambiente(self, nome):
        """
        Obtém o valor de uma variável de ambiente.

        Args:
            nome: Nome da variável.

        Return:
           Valor da variável, ou None se não existir.

        Usa os.getenv que retorna None caso variável não exista.
        """
        return os.getenv(nome)