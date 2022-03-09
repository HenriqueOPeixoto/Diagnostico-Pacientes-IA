import perceptron.perceptron as perceptron
from casoClass import Caso

rede_neural = perceptron.Perceptron()

file = open("treinamento.txt","r",encoding='utf-8')

lista_casos: Caso = []

for line in file:
    valores = line.replace('\n','').split(" ")
    teste = Caso(valores[0],valores[1],valores[2],valores[3],valores[4])
    teste.set_diagnostico(valores[5])
    lista_casos.append(teste)

perceptron.treinar(rede_neural, lista_casos)
