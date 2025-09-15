from gerenciadorsys import GerenciadorSys
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