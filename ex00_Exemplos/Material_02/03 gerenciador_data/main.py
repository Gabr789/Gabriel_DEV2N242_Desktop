from gerenciadordata import GerenciadorDataHora

def menu():
    gd = GerenciadorDataHora()
    while True:
        print("1. Mostrar data e hora atual")
        print("2. Adicionar dias a uma data")
        print("3. Subtrair dias de uma data")
        print("4. Calcular diferença entre duas datas")
        print("5. Converter string para data")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            agora = gd.data_atual()
            print("Data atual:", gd.formatar_data(agora))
            input("\nPressione Enter para voltar ao menu...")
        
        elif opcao == "2":
            data_str = input("Informe a data (dd/mm/aaaa): ")
            dias = int(input("Quantos dias adicionar? "))
            data = gd.converter_str_para_data(data_str)
            nova_data = gd.adicionar_dias(data, dias)
            print("Nova data:", gd.formatar_data(nova_data))
            input("\nPressione Enter para voltar ao menu...")
        
        elif opcao == "3":
            data_str = input("Informe a data (dd/mm/aaaa): ")
            dias = int(input("Quantos dias subtrair? "))
            data = gd.converter_str_para_data(data_str)
            nova_data = gd.subtrair_dias(data, dias)
            print("Nova data:", gd.formatar_data(nova_data))
            input("\nPressione Enter para voltar ao menu...")
        
        elif opcao == "4":
            data1 = input("Data 1 (dd/mm/aaaa): ")
            data2 = input("Data 2 (dd/mm/aaaa): ")
            d1 = gd.converter_str_para_data(data1)
            d2 = gd.converter_str_para_data(data2)
            diferenca = gd.calcular_diferenca(d1, d2)
            print(f"Diferença: {diferenca.days} dias")
            input("\nPressione Enter para voltar ao menu...")
        
        elif opcao == "5":
            data_str = input("Digite a data (dd/mm/aaaa): ")
            data = gd.converter_str_para_data(data_str)
            print("Objeto datetime:", data)
            input("\nPressione Enter para voltar ao menu...")
        
        elif opcao == "6":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()