import noClass
import casoClass

no = noClass.No

class Tree:
    def __init__(self, lista_dados_iniciais: list[casoClass.Caso] ):
        self.raiz = no(lista_dados_iniciais)
        self.entropia_geral = None # a ser implementado


