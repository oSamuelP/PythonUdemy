# """"
# Interpolação basica de strings 
# s - string
# d e i - int 
# f - float 
# x e X - Hexadecimal (ABCDEF0123456789)
# """"

nome = 'Pedrin'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' %(nome, preco)
print (variavel)
print ('o Hexadecial de %d é %04x' %(1500, 1500)) #Hexa x ou X