import perceptron.perceptron as perceptron
from casoClass import Caso

rede_neural = perceptron.Perceptron()

file = open("treinamento.txt","r",encoding='utf-8')
file_entrada = open("entrada.txt","r",encoding='utf-8')

lista_casos: Caso = []
lista_casos_entrada: Caso = []

for line in file:
    valores = line.replace('\n','').split(" ")
    teste = Caso(valores[0],valores[1],valores[2],valores[3],valores[4])
    teste.set_diagnostico(valores[5])
    lista_casos.append(teste)

for line in file_entrada:
    valores = line.replace('\n','').split(" ")
    teste = Caso(valores[0],valores[1],valores[2],valores[3],valores[4])
    lista_casos_entrada.append(teste)

perceptron.treinar(rede_neural, lista_casos, 5000)
perceptron.printPesos(rede_neural)
print(perceptron.verificar(rede_neural, lista_casos) * 100, '% de acerto')
perceptron.classificar(rede_neural, lista_casos_entrada)

print()
print('| DIAGNÓSTICOS |')
print()

print('Nome / Diagnóstico:')
for caso in lista_casos_entrada:
    print('{}: {}'.format(caso.nome, caso.get_diagnostico_string()))
