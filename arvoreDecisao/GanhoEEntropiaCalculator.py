from casoClass import Caso
import math

from enums import enums as dic_enums

def calculador_entropia(conjunto_elementos: list[Caso], chave: str):
    
    dic = dic_enums[chave]
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
        acumulador += -(probabilidade)*math.log(probabilidade,2)
    
    return acumulador

def calculador_entropia_geral(conjunto_elementos: list[Caso]):
    chaves = list(dic_enums['dores'].keys())
    dic = {}
    acumulador = 0
    for valor in chaves:
        dic[dic_enums['dores'][valor]] = 0
    for elemento in conjunto_elementos:
        dic[elemento.diagnostico] += 1

    valores = list(dic.values())
    for result in valores:
        probabilidade = result/len(conjunto_elementos)
        # print('probabilidade',probabilidade)    
        acumulador += -(probabilidade)*math.log(probabilidade,2)
    return acumulador


def calculador_ganho(conjunto_elementos: list[Caso],entropia_geral):
    chaves = list(dic_enums.keys())
    resultados = {}

    for chave in chaves:
        valores_possiveis = list(dic_enums[chave].keys())
        resultado_parcial = {}
        acumulador = 0

        for valor in valores_possiveis:
            resultado_parcial[dic_enums[chave][valor]] = 0

        for elemento in conjunto_elementos:
            resultado_parcial[elemento.find_value_from_string(chave)] += 1

        for resultado in resultado_parcial:
            acumulador += (resultado/len(conjunto_elementos))*calculador_entropia(conjunto_elementos,chave)
        resultados[chave] = entropia_geral - acumulador 
    # print(resultados)
    return None