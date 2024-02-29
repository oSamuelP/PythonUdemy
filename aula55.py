"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


def soma(x, y, z):
    # Definição parametro é a variavel
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)


soma(1, 2, 3) #argumento nao nomeado
soma(1, y=2, z=5) #argumento nomeado se normear um os proximos precisam ser nomeados tambem

print(1, 2, 3, sep='-')