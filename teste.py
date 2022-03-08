

from arvoreDecisao.GanhoEEntropiaCalculator import calculador_entropia, calculador_entropia_geral, calculador_ganho
from casoClass import Caso


file = open("treinamento.txt","r",encoding='utf-8')

lista_casos: Caso = []

for line in file:
  valores = line.replace('\n','').split(" ")
  teste = Caso(valores[0],valores[1],valores[2],valores[3],valores[4])
  teste.set_diagnostico(valores[5])
  lista_casos.append(teste)

# n = calculador_entropia(lista_casos,'febre')
n = calculador_entropia_geral(lista_casos)
print(n)

# Foi :D