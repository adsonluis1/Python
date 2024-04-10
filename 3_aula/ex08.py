# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
produto1 = float(input('valor do produto \n'))
produto2 = float(input('valor do produto \n'))
produto3 = float(input('valor do produto \n'))

print('o produto comprado deve ser o', min(produto1,produto2,produto3))