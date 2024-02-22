"""
Lista de listas e seus índices
"""
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda']  # 2
]

# print(salas[1][0]) resultado Elaine
# print(salas[0][1]) resultado Helena
# print(salas[2][2]) resultado Eduarda
# print(salas[2][3][3]) resultado 30 caso coloque tupla na lista (0, 10, 20, 30)

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)