primeiro_valor = input ('Digite um valor: ')
segundo_valor = input ('Digite outro valor: ')

if primeiro_valor > segundo_valor:
   print (f'Primeiro valor {primeiro_valor} É maior que o segundo valor,  {segundo_valor} ')
elif segundo_valor > primeiro_valor:
   print (f'Segundo valor {segundo_valor} É maior que primeiro valor,  {primeiro_valor} ')
elif primeiro_valor == segundo_valor:
   print (f'Voce digitou valores iguais {primeiro_valor} e {segundo_valor} ')