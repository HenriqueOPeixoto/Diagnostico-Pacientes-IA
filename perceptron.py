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

def treinar(casos):
    pass
