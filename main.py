from casoClass import Caso

title = '| Sistema Automatizado de Diagnóstico de Pacientes |'

print('=' * title.__len__())
print(title)
print('=' * title.__len__())


# caso teste -> paciente Teste, sem febre, sem enjoo, manchas pequenas, com dores e doente
teste = Caso('Teste', 'Não', 'Não', 'Pequenas', 'Sim')
