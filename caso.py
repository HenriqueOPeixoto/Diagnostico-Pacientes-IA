'''
Classificação dos dados:

Sim = True
Não = False

Doente = True
Saudável = False

Manchas pequenas = False
Manchas grandes = True
'''

class Caso:
    def __init__(self, nome, febre, enjoo, manchas, dores, diagnostico):
        self.nome = nome
        self.febre = febre
        self.enjoo = enjoo
        self.manchas = manchas
        self.dores = dores
        self.diagnostico = diagnostico
    

