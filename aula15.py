# operadores logicos 
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras
# se qualquer valor for considerado falso,
# a expressão inteira sera avaliada naquele valor
# São considerados falsy (que voce ja viu)
# 0 0.0 '' False 
# Tambem existe o tipo None que é usado para representar um não valor

### AND

entrada = input('[E]ntrar ou [S]air')
senha_digitada = input ('Digite a senha: ')

senha_permitida = '1234'

if entrada == 'E' and senha_digitada == senha_permitida:
     print ('Entrar')
else:
     print ('Sair')

## Avaliação de curto circuito 
#print (True and False and True)
#print(bool (''))
#print (True and 0 and True)