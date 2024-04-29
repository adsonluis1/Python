# Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e mostre a quantidade de tinta necessária para pintá-á, sabendo que cada litro de tinta, pinta uma área de 2m2.
def isNum (num):
  return num.isnumeric() | num.replace('.','').isdigit()
altura = input('Digite um a altura da parede \n')
while (isNum(altura) == False):
  print('Digite um valor correto ...')
  altura = input('Digite um a altura da parede \n')
largura = input('Digite um a largura da parede \n')
while (isNum(largura) == False):
  print('Digite um valor correto ...')
  largura = input('Digite um a largura da parede \n')
metrosQuadrados = float(altura) * float(largura)
print('Sua parede tem', metrosQuadrados, 'metros quadrados e vão ser usados um total de:', metrosQuadrados / 2, 'Litros')