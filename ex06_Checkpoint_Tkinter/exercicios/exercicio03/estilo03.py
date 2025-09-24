

class Estilos03:
    FUNDO_JANELA = "#addbff"

    FUNDO_FRAME = "#a0aaff"

    FONTE_TEXTO = "Arial", 13



    @classmethod
    def estiloJanela(cls):
        return {
            "bg": cls.FUNDO_JANELA
        }
    

    @classmethod
    def estiloFrame(cls):
        return {
            "bg": cls.FUNDO_FRAME,
            "height": 700,
            "width": 300
        }


    @classmethod
    def estiloLabel(cls):
        return {
            "bg": cls.FUNDO_FRAME,
            "font": cls.FONTE_TEXTO
        }
    

    @classmethod
    def estiloEntry(cls):
        return {
            "font": cls.FONTE_TEXTO
        }
    

    @classmethod
    def estiloButton(cls):
        return {
            "bg": cls.FUNDO_JANELA,
            "font": cls.FONTE_TEXTO
        }
    

    @classmethod
    def estiloRadio(cls):
        return {
            "bg": cls.FUNDO_FRAME,
            "font": cls.FONTE_TEXTO
        }
    

    @classmethod
    def estiloCheck(cls):
        return {
            "bg": cls.FUNDO_FRAME,
            "font": cls.FONTE_TEXTO
        }
    

    @classmethod
    def estiloCombo(cls):
        return {
            "font": cls.FONTE_TEXTO
        }