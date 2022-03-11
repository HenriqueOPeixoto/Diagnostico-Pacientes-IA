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

def listaHomogenico(conjunto_elementos: list[Caso]):
    resp = conjunto_elementos[0].diagnostico
    for elemento in conjunto_elementos:
        if(resp != elemento.diagnostico):
            return False
    return True
            
def passaParaProximoNivelComDiaginosticoFilhosIguais(no: No):
    print('\n\n\n')
    print(no)
    print('\n\n\n')
    elementos_separados = separaElementos (no.conjunto_elementos, melhor_decisao(no.conjunto_elementos)[0])
    # print('\n\n\n\n', elementos_separados,'\n\n\n\n')
    for chave in elementos_separados:
        no.adicionar_filho(elementos_separados[chave])
        if(not listaHomogenico(elementos_separados[chave])):
            return True
    return False
