from arvoreDecisao.noHandler import implementa_arvore_decisao, print_niveis_abaixo
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
    implementa_arvore_decisao(arvore.get_no())
    print_niveis_abaixo(arvore.get_no(),0)
