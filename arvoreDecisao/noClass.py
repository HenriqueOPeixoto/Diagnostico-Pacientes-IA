from casoClass import Caso
from noClass import No


class No:
    def __init__(self, conjunto_elementos: list[Caso], pai: No):
        self.conjunto_elementos = conjunto_elementos
        self.filhos:list[No] = []
        self.pai = pai
        self.ganho = None #Retornará um dicionário ou vetor com o valor do ganho e qual atributo apresenta o maior valor

    
    def adicionar_filho(self, filho: No):
        filho.pai= self
        self.filhos = self.filhos.append(filho)


