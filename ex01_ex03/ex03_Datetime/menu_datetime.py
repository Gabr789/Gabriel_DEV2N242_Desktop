from gerenciadordata import GerenciadorDataHora



# Fazer uma função para escrever " (número exercício) - exercício (número exercício)" pela quantidade de exercícios que tiver




def continuar():
    input("\nAperte Enter para continuar...")

def menuRevisao():
    gdt = GerenciadorDataHora()
    while True:
        print("\n", "- "*50, "\n")
        print("-- Menu Datetime -- ")
        print("  1 - Exercício 1")
        print("  2 - Exercício 2")
        print("  3 - Exercício 3")
        print("  4 - Exercício 4")
        print("  5 - Exercício 10 a 11")
        print(" 0 - Sair do programa")

        opcao = input("Escolha uma das opções: ")

        match opcao:

            case '1':
                print("\n\nExercício 1:\n")
                
# Exercício 1 
# Crie uma instância da classe GerenciadorDataHora e 
# Use o método data_atual() para obter a data e hora atual. 
# Formate o resultado com formatar_data() usando o formato "dd/mm/yyyy 
# HH:MM:SS". 
# Imprima a string formatada no terminal. 

                gdt_formatado = gdt.formatar_data(gdt.data_atual())
                print(f"Data atual: {gdt_formatado}")

                continuar()

            
            case '2':
                print("\n\nExercício 2:\n")

# Exercício 2 
# Obtenha a data atual com data_atual() e 
# Use adicionar_dias() para adicionar 10 dias. 
# Use subtrair_dias() para subtrair 7 dias. 
# Imprima ambas as novas datas formatadas. 

                hoje = gdt.data_atual()
                print(f"Data atual: {gdt.formatar_data(hoje)}")

                dez_dias = gdt.adicionar_dias(hoje, 10)
                print(f"Data daqui a 10 dias: {gdt.formatar_data(dez_dias)}")

                sete_dias = gdt.subtrair_dias(hoje, 7)
                print(f"Data uma semana atrás: {gdt.formatar_data(sete_dias)}")

                continuar()


            case '3':
                print("\n\nExercícios 3:\n")

# Exercício 3 
# Solicite ao usuário duas datas no formato dd/mm/yyyy. 
# Converta ambas para objetos datetime usando converter_str_para_data(). 
# Calcule a diferença entre as duas usando calcular_diferenca(). 
# Imprima a diferença em dias.

                data1 = input("Digite uma data no formato dd/mm/yyyy: ")
                data2 = input("Digite outra data no formato dd/mm/yyyy: ")

                data1_convertida = gdt.converter_str_para_data(data1)
                data2_convertida = gdt.converter_str_para_data(data2)

                dif = gdt.calcular_diferenca(data1_convertida, data2_convertida)
                print(f"Diferença de dias entre as datas {data1} e {data2}: {dif.days} dias.")

                continuar()

            case '4':
                print("\n\nExercícios 7, 8 e 9:\n")

# Exercício 4 
# Peça ao usuário uma data no formato dd/mm/yyyy. 
# Converta-a para datetime. 
# Adicione 365 dias a ela (1 ano) e formate a nova data. 
# Imprima a data resultante.

                data1 = input("Digite uma data no formato dd/mm/yyyy: ")
                data1 = gdt.converter_str_para_data(data1)
                data1 = gdt.adicionar_dias(data1, 365)
                data1 = gdt.formatar_data(data1, "%d/%m/%Y")

                print(f"Data daqui 365 dias: {data1}")

            case '5':
                print("\n\nExercícios 10 e 11:\n")

            case '0':
                print("\nSaindo...")
                break

            case _:
                print("\nOpção inválida. Tente novamente...")


if __name__ == "__main__":
    menuRevisao()