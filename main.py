import caso

title = '| Sistema Automatizado de Diagnóstico de Pacientes |'

print('=' * title.__len__())
print(title)
print('=' * title.__len__())


# caso teste -> paciente Teste, sem febre, sem enjoo, sem manchas, com dores e doente
teste = caso.Caso('Teste', False, False, False, True, True)
