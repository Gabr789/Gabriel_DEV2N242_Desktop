from gerenciador_sistema import GerenciadorSistema
import sys

def continuar():
    input("Aperte Enter para continuar...")

def executarOS():
    gs = GerenciadorSistema()

    while True:
        print("\n\nMenu OS")
        print("1 - Executar exercícios de OS")
        print("0 - Sair")

        opcao = input("Escolha: ")

        match opcao:

            case '1':
                print("\n\Executando exercícios de OS:\n")

                # Ex 1:

                
                print("Diretório atual:", gs.diretorioAtual())

                continuar()

                # Ex 2:

                print("Listando o conteúdo do diretório base:", gs.listarConteudo())
                caminho = input("\nDigite o caminho do diretório: ")
                try:
                    print("Listando o conteúdo do diretório selecionado:", gs.listarConteudo(caminho))
                except FileNotFoundError:
                    print("Caminho não encontrado.")
                except OSError:
                    print("Tente digitar sem aspas.")

                continuar()

                # 3 a ser feito

                continuar()

                # Ex 4:

                try:
                    gs.criarDiretorio("teste")
                    print("Diretório teste criado.")
                except FileExistsError:
                    print("Diretório já existe.")
                except Exception as e:
                    print("Erro:", e)

                try:
                    gs.criarDiretorio("diretorio/subdiretorio", True)
                    print("Diretório 'diretorio' e subdiretório 'subdiretorio' criados.")
                except FileExistsError:
                    print("Diretório já existe.")
                except Exception as e:
                    print("Erro:", e)

                continuar()

                # ex 5:

                try:
                    existencia = "Existe" if gs.existe("teste") else "Não existe"
                    print(f"Verificando se o diretório 'teste' existe: {existencia}")
                except Exception as e:
                    print(f"Erro: {e}")

                try:
                    if gs.removerDiretorio("diretorio/subdiretorio"):
                        print("Removendo o subdiretório 'subdiretorio'.")
                except Exception as e:
                    print(f"Erro: {e}")

            case '0':
                print("\nSaindo...")
                sys.exit()

            case _:
                print("\nOpção inválida. Tente novamente.")

executarOS()