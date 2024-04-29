# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
def isNum (num):
  return num.isnumeric() | num.replace('.','').isdigit()
num = input('digite um numero \n')
while(isNum(num) == False):
  print('digite um número invalido')
  num = input('digite um numero \n')
print(str(round(float(num),0)).split('.')[0])