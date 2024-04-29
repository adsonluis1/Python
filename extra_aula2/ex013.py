# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R 80,00ouemgalõesde3,6litros,quecustamR 25,00. Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:comprar apenas latas de 18 litros;comprar apenas galões de 3,6 litros Misture latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
class lata :
    tamanho = 18
    preco = 80

class galao :
    tamanho = 3.6
    preco = 25

class uso :
  lata = 0
  galao = 0

metrosQuadrados = input("Quantos metros quadrados voce deseja pintar \n")
def isNum (num):
   return num.isnumeric() | num.replace('.','').isdigit()
while(isNum(metrosQuadrados) == False):
  metrosQuadrados = input("Quantos metros quadrados voce deseja pintar \n")
litros = float(metrosQuadrados) * 6
print("Uso somente de lata: ", round(litros / lata.tamanho * 1.1, 0), "\npreço: ", round(litros / lata.tamanho * 1.1, 0) * lata.preco)
print("Uso somente de galão: ", round(litros / galao.tamanho * 1.1, 0), "\npreço: ", round(litros / galao.tamanho * 1.1, 0) * galao.preco)
while(round(litros, 1) > 0):
  if(round(litros, 1) >= lata.tamanho):
    uso.lata+= 1.1
    litros-= 18
  elif(round(litros, 1) > 0):
    uso.galao+= 1.1
    litros-= 3.6
print('Economia de tinta')
print("Uso de galões: ", round(uso.galao, 0), "\npreço: ", round(round(uso.galao, 0) * galao.preco, 2))
print("Uso da lata: ", round(uso.lata, 0), "\npreço: ", round(round(uso.lata, 0) * lata.preco, 2))