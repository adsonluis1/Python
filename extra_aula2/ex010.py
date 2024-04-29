# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar os 60 km/h permitidos da via, mostre a mensagem dizendo que foi multado e o valor da multa aplicada. Considere que a multa vai custar R 129,90maisR 7,00 por cada quilômetro acima do limite (para velocidades até 80 km/h), mais R 14,00porcadaquilômetroacimadolimite(paravelocidadesentre80km/he100km/h)oumaisR  39,00 por cada quilômetro acima do limite (para velocidades até acima 100 km/h).
# v = velocidade
valorFixo = 129.90
vMax = input('Qual era a velocidade maxima da via \n')
def isNum (num):
   return num.isnumeric() | num.replace('.','').isdigit()
while(isNum(vMax) == False):
  vMax = input('Qual era a velocidade maxima da via \n')
vDoVeiculo = input('Qual era a velocidade do veiculo \n')
while(isNum(vDoVeiculo) == False):
  vDoVeiculo = input('Qual era a velocidade do veiculo \n')
if(int(vMax) >= float(vDoVeiculo)):
  print('Parabens, voce não foi multado')
elif(int(vMax) >= 60 and int(vMax) <80):
  print('Valor da multa: ', (float(vDoVeiculo) - 60) * 7 + valorFixo)
elif(int(vMax) >= 80 and int(vMax) <100):
  print('Valor da multa: ', (float(vDoVeiculo) - 80) * 14 + valorFixo)
elif(int(vMax) >= 100):
  print('Valor da multa: ', (float(vDoVeiculo) - 100) * 39 + valorFixo)
else:
  print('Parabens, voce não foi multado')