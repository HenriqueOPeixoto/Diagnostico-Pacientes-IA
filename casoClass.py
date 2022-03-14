import enums

class Caso:
    def __init__(self, nome, febre, enjoo, manchas, dores):
        self.nome = nome
        self.febre = enums.febre[febre]
        self.enjoo = enums.enjoo[enjoo]
        self.manchas = enums.manchas[manchas]
        self.dores = enums.dores[dores]
        self.diagnostico = None
    
    def set_diagnostico(self,diagnostico=''):
        self.diagnostico = enums.diagnostico[diagnostico]

    def get_diagnostico_string(self):
        if (self.diagnostico == enums.diagnostico['Doente']):
            return 'Doente'
        else:
            return 'Saudável'

    def find_value_from_string(self,String: str):
        return {
            'nome': self.nome,
            'febre': self.febre,
            'enjoo': self.enjoo,
            'manchas': self.manchas,
            'dores': self.dores,
            'diagnostico': self.diagnostico
        }.get(String, None)
    
    def print_caso(self):
        print({
            'nome': self.nome,
            'febre': self.febre,
            'enjoo': self.enjoo,
            'manchas': self.manchas,
            'dores': self.dores,
            'diagnostico': self.diagnostico
        })
    def get_caso(self):
        return ({
            'nome': self.nome,
            'febre': self.febre,
            'enjoo': self.enjoo,
            'manchas': self.manchas,
            'dores': self.dores,
            'diagnostico': self.diagnostico
        })