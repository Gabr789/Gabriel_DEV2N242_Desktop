import pandas as pd

class AnalisadorDeDados:
    def __init__(self, dados=None):
        self.dados = dados if dados is not None else pd.DataFrame()

    def carregar_dados(self, nomes, idades, notas):
        self.dados = pd.DataFrame({
            'Nome': nomes, 
            'Idade': idades,
            'Nota': notas
        })

    def adicionar_status(self):
        self.dados['Status'] = self.dados['Nota'] >= 7
        self.dados['Status'] = self.dados['Status'].replace({True: 'Aprovado', False: 'Reprovado'})

    def mostrar_dados(self):
        print("Dados Atuais:")
        print(self.dados)

    def filtrar_aprovados(self):
        return self.dados[self.dados['Status'] == 'Aprovado']

    def calcular_estatisticas(self):
        media = self.dados['Nota'].mean()
        maior = self.dados['Nota'].max()
        menor = self.dados['Nota'].min()
        print(f"Média: {media} | Maior: {maior} | Menor: {menor}")

    def salvar_em_excel(self, nome_arquivo):
        self.dados.to_excel(nome_arquivo, index=False)
        print(f"Dados salvos no arquivo: {nome_arquivo}")

    def carregar_de_excel(self, nome_arquivo):
        self.dados = pd.read_excel(nome_arquivo)
        print("Dados carregados com sucesso.")



if __name__ == "__main__":

    nomes = ["Lucas", "Ana", "Paulo"]
    idades = [22, 24, 19]
    notas = [8.5, 6.0, 9.2]

    analisador = AnalisadorDeDados()
    analisador.carregar_dados(nomes, idades, notas)
    analisador.adicionar_status()
    analisador.mostrar_dados()
    analisador.calcular_estatisticas()

    print("Alunos aprovados:")
    print(analisador.filtrar_aprovados())

    analisador.salvar_em_excel("alunos_resultado.xlsx")