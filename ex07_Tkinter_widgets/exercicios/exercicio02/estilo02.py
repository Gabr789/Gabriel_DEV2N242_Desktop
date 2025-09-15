

# Todos os exercícios devem usar um módulo de estilização separado para aplicar 
# cores,  
# fontes ou tamanhos aos widgets.

class Estilos02:

    FUNDO_JANELA = "white"

    FUNDO_FRAME = "#1050a0"

    FONTE_TITULO = "Arial", 24
    FONTE_LABEL = "Arial", 16

    FONTE_TEXTO = "Arial", 14
    COR_TEXTO = "white"
    
    FUNDO_BOTAO = "#dbdbff"


    @classmethod
    def estiloJanela(cls):
        return {
            "bg": cls.FUNDO_JANELA
        }

    @classmethod
    def estiloFrame(cls):
        return {
            "bg": cls.FUNDO_FRAME,
            # "highlightbackground": "black",
            # "highlightthicknes": 3,
            # "width": 350,
            # "height": 500
        }
    
    @classmethod
    def estiloFrameLogin(cls):
        return {
            "bg": cls.FUNDO_JANELA
        }
    
    @classmethod
    def estiloLabelTitulo(cls):
        return {
            "bg": cls.FUNDO_FRAME,
            "fg": cls.COR_TEXTO,
            "font": cls.FONTE_TITULO
        }

    @classmethod
    def estiloLabelImagem(cls):
        return {
            "width": 105,
            "height": 105,
        }
    
    @classmethod
    def estiloLabelCampos(cls):
        return {
            "bg": cls.FUNDO_FRAME,
            "fg": cls.COR_TEXTO,
            "font": cls.FONTE_LABEL
        }
    
    @classmethod
    def estiloBotao(cls):
        return {
            "bg": cls.FUNDO_BOTAO,
            "width": 30,
            "height": 1
        }

    @classmethod
    def estiloEntry(cls):
        return {
            "font": cls.FONTE_TEXTO,
            "width": 20
        }
