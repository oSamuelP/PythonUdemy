# ""
# Formatação basica de strings
# s - string
# d - int 
# f - float
# .<numero de digitos>f
# x ou X - Hexadecimal
# (Caractere) (><^) (quantidade)
# > - Esquerda 
# < - Direita
# ^ - Centro 
# = - força o numero aparecer antes dos zeros
# Sinal - + ou -
# Ex. : 0 > -100, .1f
# Conversion flags - !r !s !a
#"""

variavel = 'ABC'        
print (f'{variavel}')
print (f'{variavel: >10}')
print (f'{variavel: <10}.')
print (f'{variavel: ^10}.')
print (f'{1000.321321321321321:.1f}')
print (f'o Hexadecial de 1500 é {1500:08X}')


