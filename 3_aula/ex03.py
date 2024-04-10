# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
sexo = input('digite M ou F \n')
while sexo.upper()!='M' and sexo.upper()!= 'F':
  sexo = input('digite M ou F \n')
if sexo.upper() == 'M':
  print('Masculino')
else:
  print('Feminino')