a = 'A'
b = 'B'
c = 1.1
formato = 'a={} b={} c={:.2f}'.format(a, b, c) #primeira forma de formatar pegando os dados em sequencia

string = 'a={0} b={1} c={2:.2f}'  # segunda forma escolhendo os dados de 0 em diante
formato = string.format (a, b, c)

string = 'a={} b={} c={:.2f}'  # terceira forma por parametros
formato = string.format(
nome1=a ,nome2=b , nome3=c
)

print (formato)