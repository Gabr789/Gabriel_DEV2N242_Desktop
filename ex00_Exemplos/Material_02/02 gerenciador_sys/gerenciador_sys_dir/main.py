import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'gerenciador_sys/gerenciador_sys_exe')))
from gerenciadorsys import GerenciadorSys
"""
Esse trecho permite importar o módulo 'gerenciadorsys' localizado em um pacote externo ao pacote atual.

Explicação passo a passo:

os.path.dirname(__file__):
   Retorna o diretório onde o script atual está localizado.

os.path.join(..., '..', 'gerenciador_sys'):
   Cria um caminho relativo que sobe um nível na estrutura de pastas (com '..')
   e entra na pasta gerenciador_sys — onde está o módulo desejado.

os.path.abspath(...):
   Converte o caminho relativo em um caminho absoluto completo.

sys.path.append(...):
   Adiciona esse caminho à lista de diretórios onde o Python busca por módulos para importação.
   Isso permite que o Python encontre o módulo gerenciadorsys mesmo ele estando fora do caminho padrão.

from gerenciadorsys import GerenciadorSys:
   Após o caminho estar disponível no sys.path, o módulo pode ser importado normalmente.

"""

def menu_sys():
    gs = GerenciadorSys()

    while True:
        print("1 - Mostrar argumentos da linha de comando")
        print("2 - Mostrar versão do Python")
        print("3 - Caminho do interpretador Python")
        print("4 - Plataforma do sistema")
        print("5 - Ver módulos carregados")
        print("6 - Sair do programa")
        print("0 - Encerrar menu normalmente")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                print("Argumentos:", gs.mostrar_argv())

            case "2":
                print("Versão do Python:", gs.versao_python())

            case "3":
                print("Interpretador:", gs.caminho_interpretador())

            case "4":
                print("Plataforma:", gs.plataforma())

            case "5":
                try:
                    n = int(input("Quantos módulos mostrar? (ex: 10): "))
                except ValueError:
                    n = 10
                print("Módulos carregados:", gs.modulos_carregados(n))

            case "6":
                print("Saindo com sys.exit(0)...")
                gs.sair()

            case "0":
                print("Encerrando menu normalmente.")
                break

            case _:
                print("Opção inválida.")


if __name__ == "__main__":
    menu_sys()