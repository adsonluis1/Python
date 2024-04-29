# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R 5,759opreçodolitrodoálcooléR 4,498. álcool até 20 litros, desconto de 3% por litro acima de 20 litros, desconto de 5% por litro gasolina até 20 litros, desconto de 4% por litro acima de 20 litros, desconto de 6% por litro
def isNum (num):
   return num.isnumeric() | num.replace('.','').isdigit()
combustivel = input('Digite A para álcool \nDigite G para gasolina \n').upper()
while(combustivel != "A" and combustivel != "G"):
  print("[ERROR]")
  combustivel = input('Digite A para álcool \nDigite G para gasolina \n').upper()
litros = input("Quantos litros deseja abastecer ? \n")
while(isNum(litros) == False):
  litros = input("Quantos litros deseja abastecer ? \n")
if(combustivel == 'A'):
  preco = round(float(litros) * 4.498 ,2)
  if(float(litros) <= 20):
    print(round(preco - preco * 0.03 ,2))
  else:
    print(round(preco - preco * 0.05 ,2))
else:
  preco = round(float(litros) * 5,759 ,2)
  if(float(litros) <= 20):
    print(round(preco - preco * 0.04 ,2))
  else:
    print(round(preco - preco * 0.06 ,2))