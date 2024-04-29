# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com aumento de 15%
def isNum (num):
  return num.isnumeric() | num.replace('.','').isdigit()
oldSalario = input('Digite seu salário ... \n')
while(isNum(oldSalario) == False):
  print('Digite um valor correto...')
  oldSalario = input('Digite seu salário ... \n')
print('seu novo salário é de: R$', round(float(oldSalario) * 1.15,2))