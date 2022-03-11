from casoClass import Caso


class No:
    def __init__(self, conjunto_elementos: list[Caso], pai):
        self.conjunto_elementos = conjunto_elementos
        self.filhos:list[No] = []
        self.pai = pai
    
    def adicionar_filho(self, filho):
        no_filho = No(None,self)
        self.filhos.append(no_filho)
    


