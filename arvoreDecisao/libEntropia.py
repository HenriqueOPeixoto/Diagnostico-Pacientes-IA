from casoClass import Caso
import math

from enums import enums as dic_enums
from enums import enumsSemDiaginostico as dic_enums_sem_diaginostico

def calculador_entropia(conjunto_elementos: list[Caso], chave: str):
    
    dic = dic_enums_sem_diaginostico[chave]
    possibilidades = list(map(lambda x: dic[x],list(dic.keys())))
    acumulador = 0
    values_dic = {}

    # instancia o dicionário
    for key in possibilidades:
        values_dic[key] = 0
    
    for caso in conjunto_elementos:
        valor_atual = caso.find_value_from_string(chave)
        values_dic[valor_atual] += 1 

    for key in possibilidades:
        probabilidade = values_dic[key]/len(conjunto_elementos)
        # print((probabilidade,values_dic,key,len(conjunto_elementos)))
        if(probabilidade == 0):
            acumulador += 1  
        else:
            acumulador += -(probabilidade)*math.log(probabilidade,2)
    
    return acumulador

def calculador_entropia_geral(conjunto_elementos: list[Caso]):
    chaves = list(dic_enums['diagnostico'].keys())
    dic = {}
    acumulador = 0
    for valor in chaves:
        dic[dic_enums['diagnostico'][valor]] = 0
    for elemento in conjunto_elementos:
        dic[elemento.diagnostico] += 1

    valores = list(dic.values())
    for result in valores:
        probabilidade = result/len(conjunto_elementos)
        # print('probabilidade',probabilidade)    
        acumulador += -(probabilidade)*math.log(probabilidade,2)
    return acumulador


def calculador_ganho(conjunto_elementos: list[Caso]):
    chaves = list(dic_enums_sem_diaginostico.keys())
    resultados = {}
    # print(chaves)
    for chave in chaves:
        valores_possiveis = list(dic_enums_sem_diaginostico[chave].keys())
        resultado_parcial = {}
        acumulador = 0

        for valor in valores_possiveis:
            resultado_parcial[dic_enums_sem_diaginostico[chave][valor]] = 0

        for elemento in conjunto_elementos:
            resultado_parcial[elemento.find_value_from_string(chave)] += 1

        for resultado in resultado_parcial:
            acumulador += (resultado/len(conjunto_elementos))*calculador_entropia(conjunto_elementos,chave)
        resultados[chave] = calculador_entropia_geral(conjunto_elementos) - acumulador 
    return resultados

def melhor_decisao(conjunto_elementos: list[Caso]):
    lib = calculador_ganho(conjunto_elementos)
    chave_maior_valor = max(lib.keys(), key=(lambda key: lib[key]))
    # print([chave_maior_valor,lib[chave_maior_valor]])
    return([chave_maior_valor,lib[chave_maior_valor]])
