# Faça um algoritmo que leia seu nome e duas notas de avaliação. Imprima na tela seu nome e a sua média.
nome = input('qual seu nome ? \n')
n1 = float(input('primera nota \n'))
n2 = float(input('segunda nota \n'))
media = (n1 + n2) / 2
print('Ola, ',nome ,'sua media é de ', round(media,1))