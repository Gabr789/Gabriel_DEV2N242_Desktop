import sys
import os

class GerenciadorSys:
    """
    Classe para explorar funcionalidades do módulo sys do Python.

    Métodos:
        mostrar_argv(): Retorna a lista de argumentos passados na linha de comando.
        versao_python(): Retorna a versão completa do interpretador Python.
        caminho_interpretador(): Retorna o caminho absoluto do executável Python.
        plataforma(): Retorna o nome da plataforma/sistema operacional.
        modulos_carregados(n=10): Retorna os primeiros N módulos carregados no momento.
        sair(codigo=0): Encerra o programa com um código de saída específico.
        explicar_sys_path_modificacao(): Explica como funciona a modificação do sys.path para importar módulos externos.
    """

    def mostrar_argv(self):
        """
        Retorna os argumentos passados para o script na linha de comando.

        Returns:
            list: Lista de strings representando os argumentos.
            sys.argv é uma lista onde o primeiro elemento é o nome do script,
            e os seguintes são os argumentos que foram passados para o programa.
            Útil para receber parâmetros na execução via terminal.
        """
        return sys.argv

    def versao_python(self):
        """
        Retorna a versão completa do interpretador Python em execução.

        Returns:
            str: String contendo a versão do Python, data e build.
        """
        return sys.version

    def caminho_interpretador(self):
        """
        Retorna o caminho absoluto do executável Python que está rodando o script.

        Returns:
            str: Caminho completo do interpretador Python.
        """
        return sys.executable

    def plataforma(self):
        """
        Retorna o nome da plataforma/sistema operacional onde o Python está rodando.

        Returns:
            str: Identificador da plataforma  win32.
        """
        return sys.platform

    def modulos_carregados(self, n=10):
        """
        Retorna uma lista com os nomes dos primeiros N módulos carregados.

        Args:
            n (int): Quantidade de módulos a listar (padrão 10).

        Returns:
            list: Lista com nomes dos módulos carregados.
        """
        return list(sys.modules.keys())[:n]

    def sair(self, codigo=0):
        """
        Encerra o programa imediatamente com o código de saída fornecido.

        Args:
            codigo (int): Código de saída (0 indica sucesso, outros valores indicam erro).
        """
        sys.exit(codigo)

   