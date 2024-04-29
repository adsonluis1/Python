# Crie um programa que leia quanto dinheiro em real uma pessoa tem na carteira e mostre quantos dólares, euros ou bitcoins ela pode comprar. Faça uma busca da cotação das moedas e indique como comentário no código o dia da cotação.
dolar = 5.117
euro = 5.48
bitcoin = 327418.60
def isNum (num):
  return num.isnumeric() | num.replace('.','').isdigit()
real = input('Digite o quanto voce tem... \n')
while(isNum(real) == False):
    print('Tem que ser um numero')
    real = input('Digite o quanto voce tem... \n')
print('Vc pode comprar', round(float(real) / dolar,2),'Dolares')
print('Vc pode comprar', round(float(real) / euro,2),'Euros')
print('Vc pode comprar', round(float(real) / bitcoin,3),'Bitcoins')