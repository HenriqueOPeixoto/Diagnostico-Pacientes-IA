from arvoreDecisao.libEntropia import melhor_decisao
from casoClass import Caso
from enums import enums as dic_enums

from arvoreDecisao.noClass import No 

def separaElementos (conjunto_elementos: list[Caso], chave):
    dic = {}
    valoresPossiveis = list(dic_enums[chave].values())
    for valor in valoresPossiveis:
        dic[valor] = []
    for valor in valoresPossiveis:
        for elemento in conjunto_elementos:
            if ( elemento.find_value_from_string(chave) == valor):
                dic[valor].append(elemento) 
    return dic

def listaHomogenica(conjunto_elementos: list[Caso]):
    resp = conjunto_elementos[0].diagnostico
    for elemento in conjunto_elementos:
        if(resp != elemento.diagnostico):
            return False
    return True
            
def implementa_arvore_decisao(no: No):
    if(listaHomogenica(no.conjunto_elementos)):
        return True

    elementos_separados = separaElementos (no.conjunto_elementos, melhor_decisao(no.conjunto_elementos)[0])
    for chave in elementos_separados:
        no_filho = no.adicionar_filho(elementos_separados[chave])
        implementa_arvore_decisao(no_filho)

def print_niveis_abaixo(no,nivel):
    print("Nível nó: ",nivel)
    print('\n\n\n')
    for elemento in no.conjunto_elementos:
        elemento.print_caso()
    print('\n\n\n')
    for filho in no.filhos:
        print_niveis_abaixo(filho,nivel+1)
