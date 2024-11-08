curso = {'matematica':6, 'Fisica':4, 'Quimica':5}
total_creditos = 0
for asignatura, credito in curso.items():
    print(asignatura, 'tiene', credito, 'creditos')
    total_creditos += credito
print('Total de creditos: ',total_creditos)