class Estilos:
    FUNDO_JANELA = "#282828"
    COR_TEXTO_TITULO = "#FFFFFF"
    FONTE_TITULO = ("Arial", 16, "bold")

    FUNDO_BOTAO = "#4CAF50"
    COR_TEXTO_BOTAO = "#FFFFFF"
    FONTE_BOTAO = ("Arial", 12, "bold")

    @classmethod
    def estilo_botao(cls):
        return {
            "bg": cls.FUNDO_BOTAO,
            "fg": cls.COR_TEXTO_BOTAO,
            "font": cls.FONTE_BOTAO,
            "relief": "raised",
            "bd": 3,
            "padx": 10,
            "pady": 5,
        }