from arvoreDecisao.noClass import No
from casoClass import Caso


class Tree:
    def __init__(self, lista_dados_iniciais: list[Caso] ):
        self.raiz = No(lista_dados_iniciais,None)


