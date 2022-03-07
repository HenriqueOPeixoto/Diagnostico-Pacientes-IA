import enums

class Caso:
    def __init__(self, nome, febre, enjoo, manchas, dores):
        self.nome = nome
        self.febre = enums.febre[febre]
        self.enjoo = enums.enjoo[enjoo]
        self.manchas = enums.manchas[manchas]
        self.dores = enums.dores[dores]
        self.diagnostico = None
    
    def set_diagnostico(self,diagnostico):
        self.diagnostico = enums.diaginostico[diagnostico]
