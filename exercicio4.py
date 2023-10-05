
##Iterando strings com while


nome = input ('Digite seu nome aluno ')  # Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'{letra}-'
    indice += 1

ch = '-'
novo_nome = novo_nome.rstrip(ch)
    
print(novo_nome)