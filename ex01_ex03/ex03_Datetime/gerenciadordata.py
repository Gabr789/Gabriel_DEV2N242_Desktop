from datetime import datetime, timedelta

class GerenciadorDataHora:
    """
    Classe para gerenciar operações com data e hora.

    Métodos:
        data_atual(): Retorna a data e hora atual.
        formatar_data(data, formato): Formata uma data para o formato desejado.
        adicionar_dias(data, dias): Adiciona dias a uma data.
        subtrair_dias(data, dias): Subtrai dias de uma data.
        calcular_diferenca(data1, data2): Calcula diferença entre duas datas.
        converter_str_para_data(data_str, formato): Converte string para datetime.
    """

    def data_atual(self):
        """
        Retorna o momento atual com data e hora.

        Returns:
            datetime: Data e hora atual.
        """
        return datetime.now()

    def formatar_data(self, data, formato="%d/%m/%Y %H:%M:%S"):
        """
        Formata uma data conforme o formato especificado.

        Args:
            data (datetime): Objeto datetime.
            formato (str): String de formatação.

        Returns:
            str: Data formatada.
        """
         
        return data.strftime(formato)

    def adicionar_dias(self, data, dias):
        """
        Adiciona dias a uma data.

        Args:
            data (datetime): Objeto datetime.
            dias (int): Quantidade de dias a adicionar.

        Returns:
            datetime: Nova data.
        """
        return data + timedelta(days=dias)

    def subtrair_dias(self, data, dias):
        """
        Subtrai dias de uma data.

        Args:
            data (datetime): Objeto datetime.
            dias (int): Dias a subtrair.

        Returns:
            datetime: Nova data.
        """
        return data - timedelta(days=dias)

    def calcular_diferenca(self, data1, data2):
        """
        Calcula a diferença entre duas datas.

        Args:
            data1 (datetime): Primeira data.
            data2 (datetime): Segunda data.

        Returns:
            timedelta: Diferença entre datas.
        """
        return abs(data1 - data2)

    def converter_str_para_data(self, data_str, formato="%d/%m/%Y"):
        try:
            return datetime.strptime(data_str.strip(), formato)
        except ValueError as e:
            raise ValueError(f"Erro ao converter '{data_str}' para data com formato '{formato}': {e}")