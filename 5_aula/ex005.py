# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. Dicas: Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro; Triângulo Equilátero: três lados iguais; Triângulo Isósceles: quaisquer dois lados iguais; Triângulo Escaleno: três lados diferentes;
def isNum(num):
  return num.isnumeric() | num.replace('.','').isdigit()
lado1 = input('Digite o valor do 1° lado \n')
while(isNum(lado1) == False):
  lado1 = input('Digite o valor do 1° lado \n')

lado2 = input('Digite o valor do 2° lado \n')
while(isNum(lado2) == False):
  lado2 = input('Digite o valor do 2° lado \n')

lado3 = input('Digite o valor do 3° lado \n')
while(isNum(lado3) == False):
  lado3 = input('Digite o valor do 3° lado \n')
triangulo = True
lado1 = float(lado1)
lado2 = float(lado2)
lado3 = float(lado3)

if(lado1 + lado2 < lado3):
  triangulo = False
  print('1')
elif(lado2 + lado3 < lado1):
  triangulo = False
  print('2')
elif(lado1 + lado3 < lado2):
  triangulo = False
  print('3')
if(triangulo == False):
  print('Não é um triângulo')
else:
  if(lado1 == lado2 == lado3):
    print('Triângulo Equilátero')
  elif(lado1 == lado2 or lado2 == lado3 or lado1 == lado3):
    print('Triângulo Equilátero')
  else:
    print('Triângulo Escaleno')