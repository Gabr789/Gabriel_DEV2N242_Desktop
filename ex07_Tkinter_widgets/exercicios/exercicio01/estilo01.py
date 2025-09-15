

# Todos os exercícios devem usar um módulo de estilização separado para aplicar 
# cores,  
# fontes ou tamanhos aos widgets.

class Estilos01:

    FUNDO_FRAME = "#efefff"

    FONTE_TEXTO = "Arial", 14
    
    FUNDO_BOTAO = "#dbdbff"
    FONTE_BOTAO = "Arial", 10


    @classmethod
    def estiloJanela(cls):
        return {
            "bg": cls.FUNDO_JANELA
        }

    @classmethod
    def estiloFrame(cls):
        return {
            "bg": cls.FUNDO_FRAME,
            "highlightbackground": "black",
            "highlightthicknes": 3,
            "width": 500,
            "height": 150
        }

    @classmethod
    def estiloLabel(cls):
        return {
            "bg": cls.FUNDO_FRAME,
            "font": cls.FONTE_TEXTO
        }
    
    @classmethod
    def estiloBotao(cls):
        return {
            "bg": cls.FUNDO_BOTAO,
            "font": cls.FONTE_BOTAO,
            "width": 30,
            "height": 1
        }

    @classmethod
    def estiloEntry(cls):
        return {
            "font": cls.FONTE_TEXTO
        }
