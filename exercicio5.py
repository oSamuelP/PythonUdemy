""" Calculadora com while """
while True:
    n1 = int (input ('Digite a um numero: '))
    n2 = int (input ('Digite outro numero: '))
    operador = input ('Escolha qual tipo de calculo quer fazer, "+","-","*","/" ')
    resultado = 0

    if operador == '+':
        resultado = n1 + n2
        print ('A soma dos numeros é: ', resultado)
    elif operador == '-':
        resultado = n1 - n2
        print ('A subtração dos numeros é', resultado)
    elif operador == '*':
        resultado = n1 * n2
        print ('A multiplicação dos numeros é', resultado)
    elif operador == '/':
        resultado = n1 / n2
        print ('A divisão dos numeros é', resultado)
    
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break