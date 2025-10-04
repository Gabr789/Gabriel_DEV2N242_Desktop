class Estilos01:
    FUNDO_JANELA = "#addbff"

    FUNDO_FRAME = "#a0aaff"

    FONTE_TEXTO = "Arial", 13



    @classmethod
    def estiloJanela(cls):
        return {
            "bg": cls.FUNDO_JANELA
        }