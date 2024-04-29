# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$98,75 por dia e que cada km custa um adicional custa 0,028 centavos.
def isNum (num):
  return num.isnumeric() | num.replace('.','').isdigit()
dias = input('Quantos dias o carro foi alugado... \n')
while(isNum(dias) == False):
  print('Digite um numero valido')
  dias = input('Quantos dias o carro foi alugado... \n')
km = input('Quantos Km o carro rodou... \n')
while(isNum(km) == False):
  print('Digite um numero valido')
  km = input('Quantos Km o carro rodou... \n')
print('valor do aluguel : R$', float(dias)*98.75 + float(km)*0.028)