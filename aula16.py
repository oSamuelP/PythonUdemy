# operadores logicos 
# and (e) or (ou) not (não)
# or - uma das condições precisam ser verdadeiras
# tendo uma condição validada como verdadeira sera executado o bloco do codigo
# Será impresso o primeiro valor verdadeiro da condição
# Tambem existe o tipo None que é usado para representar um não valor

### OR

entrada = input('[E]ntrar ou [S]air ')
senha_digitada = input ('Digite a senha: ')

senha_permitida = '1234'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
     print ('Entrar')
else:
     print ('Sair')

# Avaliação curto circuito
senha = input('Senha: ') or 'Sem senha aluno'
print (senha)