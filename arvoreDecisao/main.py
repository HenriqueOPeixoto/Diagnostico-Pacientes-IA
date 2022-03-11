from arvoreDecisao.noHandler import passaParaProximoNivelComDiaginosticoFilhosIguais
from arvoreDecisao.treeClass import Tree
from casoClass import Caso

def arvore_decisao():
    file = open("treinamento.txt","r",encoding='utf-8')


    lista_casos: Caso = []

    for line in file:
        valores = line.replace('\n','').split(" ")
        teste = Caso(valores[0],valores[1],valores[2],valores[3],valores[4])
        teste.set_diagnostico(valores[5])
        lista_casos.append(teste)

    arvore = Tree(lista_casos)
    no_atual = arvore.raiz
    continua_separacao = True
    while(continua_separacao):
        continua_separacao = passaParaProximoNivelComDiaginosticoFilhosIguais(no_atual)
        if(continua_separacao):
            no_atual = no_atual.conjunto_elementos
    print('fin')