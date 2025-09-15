from gerenciadorsistema import GerenciadorSistema
def menu():
    gs = GerenciadorSistema()

    while True:
        print("1 - Mostrar diretório atual")
        print("2 - Listar conteúdo do diretório")
        print("3 - Criar diretório")
        print("4 - Remover diretório")
        print("5 - Verificar existência de caminho")
        print("6 - Renomear arquivo/diretório")
        print("7 - Mostrar variável de ambiente")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                print("Diretório atual:", gs.diretorio_atual())

            case "2":
                caminho = input("Digite o caminho (ou enter para padrão): ")
                caminho = caminho if caminho else None
                try:
                    conteudo = gs.listar_conteudo(caminho)
                    print("Conteúdo:", conteudo)
                except FileNotFoundError:
                    print("Caminho não encontrado.")

            case "3":
                nome = input("Nome do diretório a criar: ")
                recursivo = input("Criar recursivamente? (s/n): ").lower() == "s"
                try:
                    gs.criar_diretorio(nome, recursivo)
                    print(f"Diretório '{nome}' criado.")
                except FileExistsError:
                    print("Diretório já existe.")
                except Exception as e:
                    print("Erro:", e)

            case "4":
                nome = input("Nome do diretório a remover: ")
                try:
                    gs.remover_diretorio(nome)
                    print(f"Diretório '{nome}' removido.")
                except FileNotFoundError:
                    print("Diretório não encontrado.")
                except OSError:
                    print("Diretório não está vazio ou não pode ser removido.")

            case "5":
                caminho = input("Caminho para verificar: ")
                existe = gs.existe(caminho)
                print(f"O caminho '{caminho}' existe? {existe}")

            case "6":
                antigo = input("Nome antigo: ")
                novo = input("Novo nome: ")
                try:
                    gs.renomear(antigo, novo)
                    print(f"Renomeado '{antigo}' para '{novo}'.")
                except FileNotFoundError:
                    print("Arquivo ou diretório não encontrado.")

            case "7":
                escolha = input("Deseja (1) digitar o nome de uma variável ou (2) ver as principais? [1/2]: ").strip()

                if escolha == "1":
                    nome = input("Nome da variável de ambiente: ").strip()
                    valor = gs.pegar_variavel_ambiente(nome)
                    if valor:
                        usuario = gs.pegar_variavel_ambiente("USERNAME")
                        print("Usuário:", usuario)
                        print(f"Valor de {nome}: {valor}")
                    else:
                        print("Variável não encontrada.")
                elif escolha == "2":
                    variaveis = [
                    "PATH",                
                    "PYTHONPATH",          
                    "VIRTUAL_ENV",          
                    "TEMP",                 
                    "TMP",                  
                    "USERNAME",             
                    "USERPROFILE",         
                    "APPDATA",              
                    "HOMEPATH",            
                    "COMPUTERNAME",        
                    "SystemRoot",           
                    "ProgramFiles",        
                    "OS",                   
                    "NUMBER_OF_PROCESSORS"  
                    ]

                    print("\nPrincipais variáveis de ambiente:\n")
                    for var in variaveis:
                        valor = gs.pegar_variavel_ambiente(var)
                        print(f"{var}: {valor}")
                else:
                    print("Opção inválida.")
                


            case "0":
                print("Saindo...")
                break

            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()