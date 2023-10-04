nome = 'Samuka'
altura = 1.95
peso = 125
imc = peso / (altura * altura) #IMC Peso / (altura * altura)

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}' ## :.2f limita quantidade de casas decimais

print(linha_1)
print(linha_2)
print(linha_3)

## EXERCICIO 7 COM FORMATAÇÃO f-strings