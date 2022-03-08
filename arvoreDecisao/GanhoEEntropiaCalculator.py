from casoClass import Caso
import math

from enums import enums as dic_enums

def calculador_entropia(conjunto_elementos: list[Caso], chave: str):
    dic = dic_enums[chave]
    possibilidades = list(dic.keys())
    acumulador = 0
    values_dic = {}

    # instancia o dicionário
    for key in possibilidades:
        values_dic[key] = 0
    
    for caso in conjunto_elementos:
        valor_atual = caso.find_value_from_string(str)
        values_dic[valor_atual] += 1 


    for key in possibilidades:
        probabilidade = values_dic[key]/len(conjunto_elementos)
        acumulador += -(probabilidade)*math.log(probabilidade,2)
    
    return acumulador