from arvoreDecisao.libEntropia import melhor_decisao
from casoClass import Caso
from enums import enums as dic_enums
from enums import diagnostico

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

def SeparaElementos_chave_valor(conjunto_elementos: list[Caso], chave,valor):
    lista = []
    for elemento in conjunto_elementos:
        if(elemento.find_value_from_string(chave) == valor):
            lista.append(elemento)
    return lista

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

def classifica_novo_caso(no: No,novo_caso: Caso):
    # print('\n\n\n')
    # for elemento in no.conjunto_elementos:
    #     elemento.print_caso()
    # print('\n\n\n')
    if(listaHomogenica(no.conjunto_elementos)):
        chave_correta = None
        for chave in diagnostico:
            if(no.conjunto_elementos[0].diagnostico == diagnostico[chave]):
                chave_correta = chave
                break
        novo_caso.set_diagnostico(chave_correta)
        return novo_caso.get_diagnostico_string()
    
    [chave,valor_chave] = melhor_decisao(no.conjunto_elementos)
    # print(chave)
    valor_referencia = novo_caso.find_value_from_string(chave)
    novo_no = No(SeparaElementos_chave_valor(no.conjunto_elementos,chave,valor_referencia),no)
    return classifica_novo_caso(novo_no,novo_caso)

def print_niveis_abaixo(no,nivel):
    print("Nível nó: ",nivel)
    print('\n\n\n')
    for elemento in no.conjunto_elementos:
        elemento.print_caso()
    print('\n\n\n')
    for filho in no.filhos:
        print_niveis_abaixo(filho,nivel+1)
