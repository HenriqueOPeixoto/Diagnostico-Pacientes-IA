import casoClass
import noClass

no = noClass.No
caso = casoClass.Caso


class No:
    def __init__(self, conjunto_elementos: list[caso], pai: no):
        self.conjunto_elementos = conjunto_elementos
        self.filhos:list[no] = []
        self.pai = pai
        self.ganho = None #Retornará um dicionário ou vetor com o valor do ganho e qual atributo apresenta o maior valor

    
    def adicionar_filho(self, filho: no):
        filho.pai= self
        self.filhos = self.filhos.append(filho)


