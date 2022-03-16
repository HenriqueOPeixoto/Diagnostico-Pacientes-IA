'''
função de ativação:
u = somatorio(xi . wi) - theta

Onde theta é o limiar

correção:
wi = wi + delta(wi)
delta(wi) = eta.xi(d - y), com d != y

pesos iniciais:
wi = 0.5
eta = 0.4
theta = 0.6
'''

import casoClass
import enums

class Perceptron:
    def __init__(self):
        # wi é o weight, ou peso, de determinada entrada
        self.w1 = 0.5
        self.w2 = 0.5
        self.w3 = 0.5
        self.w4 = 0.5

        # taxa de aprendizado
        self.eta = 0.4

        # limiar / threshold
        self.theta = 0.6

def treinar(self, casos: 'list[casoClass.Caso]', maxCiclos):
    atualizouPesos = True
    cicloAtual = 0
    while (atualizouPesos) and (cicloAtual < maxCiclos):
        atualizouPesos = False
        
        for caso in casos:
            func_ativacao = (caso.febre * self.w1 + caso.enjoo * self.w2 + 
                caso.manchas * self.w3 + caso.dores * self.w4 - self.theta)
            
            if func_ativacao >= 0:
                y = 1
            else:
                y = 0
            
            # Se d != y, deve atualizar os pesos
            # wi = wi + ηxi(d-y)
            if caso.diagnostico != y:
                self.w1 = self.w1 + self.eta * caso.febre * (caso.diagnostico - y)
                self.w2 = self.w2 + self.eta * caso.enjoo * (caso.diagnostico - y)
                self.w3 = self.w3 + self.eta * caso.manchas * (caso.diagnostico - y)
                self.w4 = self.w4 + self.eta * caso.dores * (caso.diagnostico - y)
                self.theta = self.theta + self.eta * -1 * (caso.diagnostico - y)
                atualizouPesos = True
            
        cicloAtual += 1

# Avalia a porcentagem de acerto do perceptron.
def verificar(self, casos: 'list[casoClass.Caso]'):
    erros = 0
    for caso in casos:
        func_ativacao = (caso.febre * self.w1 + caso.enjoo * self.w2 + 
                caso.manchas * self.w3 + caso.dores * self.w4 - self.theta)
            
        if func_ativacao >= 0:
            y = 1
        else:
            y = 0
        
        # Se d != y, ocorreu um erro
        if caso.diagnostico != y:
            erros += 1
    
    return 1 - (erros/len(casos)) # 1 - taxa de erro = taxa de acerto

def classificar(self, casos: 'list[casoClass.Caso]'):
    for caso in casos:
        u = (caso.febre * self.w1 + caso.enjoo * self.w2 + 
                caso.manchas * self.w3 + caso.dores * self.w4 - self.theta)
        
        caso.set_diagnostico('Saudável')
        if (u >= 0):
            caso.set_diagnostico('Doente')

def printPesos(self):
    print('w1 ', self.w1)
    print('w2 ', self.w2)
    print('w3 ', self.w3)
    print('w4 ', self.w4)
    print('theta ', self.theta)
