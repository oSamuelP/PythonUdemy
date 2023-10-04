# Operadores in e not in
# Strings são iteraveis 
# 0 1 2 3 4 5 
# S a m u e l 
#-6-5-4-3-2-1

nome = 'Samuel'
#print (nome[0])
#print(nome[-6])

print ('a' in nome)
print ('zero' in nome)
print (10 * '-')
print ('muel' not in nome)
print ('zero' in nome)


nome = input('Digite seu nome ')
encontrar = input ('Oque deseja encontrar? ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
