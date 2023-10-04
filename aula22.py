"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
nome = input('Digite seu nome ')
idade = input('Digite sua idade ')

if nome and idade:
    print (f'Seu nome é{nome}')
    print (f'seu nome invertido é ', nome[-1::-1])

    if ' ' in nome:
        print('Seu nome contem espaços')
    else:
        print('Seu nome não contem espaços')
        
    print (f'seu nome tem essa quantidade de letras',len (nome))
    print (f'a primeira letra do seu nome é ', nome[0:1])
    print (f'a ultima letra do seu nome é ', nome[-1:])
else:
    print ('Deixou campos vazios')

