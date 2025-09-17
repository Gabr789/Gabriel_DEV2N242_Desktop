
"""Configurar o frame com tamanho menor que a janela e com cores bonitas (pensando em um amarelo queimado ou claro meio fosco)"""



class Estilos01:
    FUNDO_JANELA = "white"

    FUNDO_FRAME = "#101010"



    @classmethod
    def estiloFrame(cls):
        return {
            "bg": cls.FUNDO_FRAME,
            "height": 450,
            "width": 300
        }

