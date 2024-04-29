# Faça um Programa que leia três números e mostre-os em ordem decrescente.
def isNum(num):
  return num.isnumeric() | num.replace('.','').isdigit()
num1= input('Digite o primeiro número \n')
while(isNum(num1) == False):
  num1= input('Digite o primeiro número \n')

num2= input('Digite o primeiro número \n')
while(isNum(num2) == False):
  num2= input('Digite o primeiro número \n')
num3= input('Digite o primeiro número \n')
while(isNum(num3) == False):
  num3= input('Digite o primeiro número \n')
arr = [float(num1), float(num2), float(num3)]
arr.sort()
print(arr)
