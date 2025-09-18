
"""Configurar o frame com tamanho menor que a janela e com cores bonitas (pensando em um amarelo queimado ou claro meio fosco)"""



class Estilos01:
    FUNDO_JANELA = "#addbff"

    FUNDO_FRAME = "#a0aaff"



    @classmethod
    def estiloJanela(cls):
        return {
            "bg": cls.FUNDO_JANELA
        }
    

    @classmethod
    def estiloFrame(cls):
        return {
            "bg": cls.FUNDO_FRAME,
            "height": 450,
            "width": 300
        }


    @classmethod
    def estiloLabel(cls):
        return {
            "bg": cls.FUNDO_FRAME
        }
    

    @classmethod
    def estiloEntry(cls):
        return {
            "bg": cls.FUNDO_FRAME
        }
    

    @classmethod
    def estiloButton(cls):
        return {
            "bg": cls.FUNDO_JANELA
        }
    

    @classmethod
    def estiloRadio(cls):
        return {
            "bg": cls.FUNDO_FRAME
        }
    

    @classmethod
    def estiloCheck(cls):
        return {
            "bg": cls.FUNDO_FRAME
        }
    

    @classmethod
    def estiloLabel(cls):
        return {
            "bg": cls.FUNDO_FRAME
        }
    

    @classmethod
    def estiloLabel(cls):
        return {
            "bg": cls.FUNDO_FRAME
        }

