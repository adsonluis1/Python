# Faça um algoritmo que leia o preço de um produto em dólar e mostre seu preço em real com imposto. Considere uma compra realizada na Flórida (EUA).
def isNum (num):
  return num.isnumeric() | num.replace('.','').isdigit()
valor = input('digite o valor do produto \n')
while(isNum(valor) == False):
  print('digite o valor correto')
  valor = input('digite o valor do produto \n')
print('calculando ...')
print('valor: ',float(valor) * 1.072)