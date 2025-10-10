# pip install pandas openpyxl
import os
import pandas as pd

class GerenciadorExcel:

    def __init__(self, pasta_base=None):
       
        self.pasta_base = pasta_base or os.getcwd()

    def definir_pasta_base(self, caminho):
       
        if os.path.isdir(caminho):
            self.pasta_base = caminho
        else:
            raise ValueError(f"Pasta inválida: {caminho}")

    def _caminho_completo(self, nome_arquivo):
      
        return os.path.join(self.pasta_base, nome_arquivo)

    def ler_arquivo(self, nome_arquivo, nome_planilha=0):
     
        caminho = self._caminho_completo(nome_arquivo)
        if not os.path.isfile(caminho):
            raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")
        return pd.read_excel(caminho, sheet_name=nome_planilha)

    def escrever_arquivo(self, nome_arquivo, dataframe, nome_planilha='Planilha1', modo='w'):
  
        caminho = self._caminho_completo(nome_arquivo)
        if modo == 'a' and os.path.exists(caminho):
           
            with pd.ExcelWriter(caminho, engine='openpyxl', mode='a', if_sheet_exists='replace') as escritor:
                dataframe.to_excel(escritor, index=False, sheet_name=nome_planilha)
        else:
            with pd.ExcelWriter(caminho, engine='openpyxl') as escritor:
                dataframe.to_excel(escritor, index=False, sheet_name=nome_planilha)

    def existe(self, nome_arquivo):
       
        return os.path.isfile(self._caminho_completo(nome_arquivo))

    def remover_arquivo(self, nome_arquivo):
      
        caminho = self._caminho_completo(nome_arquivo)
        if os.path.isfile(caminho):
            os.remove(caminho)

    def renomear(self, nome_antigo, nome_novo):
       
        os.rename(self._caminho_completo(nome_antigo), self._caminho_completo(nome_novo))

    def contar_linhas(self, nome_arquivo, nome_planilha=0):
       
        df = self.ler_arquivo(nome_arquivo, nome_planilha)
        return len(df)

    def contar_colunas(self, nome_arquivo, nome_planilha=0):
      
        df = self.ler_arquivo(nome_arquivo, nome_planilha)
        return len(df.columns)

    def substituir_valores(self, nome_arquivo, coluna, valor_antigo, valor_novo, nome_planilha=0):
     
        df = self.ler_arquivo(nome_arquivo, nome_planilha)
        df[coluna] = df[coluna].replace(valor_antigo, valor_novo)
        self.escrever_arquivo(nome_arquivo, df, nome_planilha=nome_planilha)

    def copiar_arquivo(self, origem, destino):
       
        caminho_origem = self._caminho_completo(origem)
        caminho_destino = self._caminho_completo(destino)
        with open(caminho_origem, 'rb') as f_origem:
            with open(caminho_destino, 'wb') as f_destino:
                f_destino.write(f_origem.read())

    def criar_arquivo(self, nome):
       
        df = pd.DataFrame({
            "Nome": ["Pedro", "Enzo", "Miguel"],
            "Idade": [25, 30, 22],
            "Valor1": [10, 20, 30],
            "Valor2": [2, 4, 5]

            
        })
        self.escrever_arquivo(nome, df)