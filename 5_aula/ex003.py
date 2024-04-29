# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: Para homens: (72.7h) - 58 Para mulheres: (62.1h) - 44.7
def isNum(num):
  return num.isnumeric() | num.replace('.','').isdigit()
sexo = input('Digite seu sexo \nM-masculino ou F-feminino \n').upper()
while(sexo != 'F' and sexo != 'M'):
  sexo = input('Digite seu sexo \nM-masculino ou F-feminino \n').upper()

altura = input('Digite sua altura \n')
while(isNum(altura) == False):
  altura = input('Digite sua altura \n')
if(sexo == 'F'):
  print("Seu peso ideal seria de: ", round((62.1*float(altura)) - 44.7,2))
else:
  print("Seu peso ideal seria de: ", round((72.7*float(altura)) - 58,2))