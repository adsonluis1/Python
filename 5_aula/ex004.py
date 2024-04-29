# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
def isNum(num):
  return num.isnumeric() | num.replace('.','').isdigit()
kgPeixe = input('Digite o peso do peixe \n')
while(isNum(kgPeixe) == False):
  kgPeixe = input('Digite o peso do peixe \n')
execesso = float(kgPeixe) - 50
if(execesso <= 0):
  print('Parabens, voce não paga multa')
else:
  multa = execesso * 4
  print('O execesso foi de: ', execesso, 'KG')
  print('A multa foi no valor de: R$', multa)