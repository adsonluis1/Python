# Faça um Programa que peça às 02 notas da unit, mostre a média e indique a sua situação: Aprovado, Reprovado ou em Recuperação. Caso tenha recuperação, indique a nota mínima que o aluno precisa tirar para ser aprovado.
def isNum (num):
  return num.isnumeric() | num.replace('.','').isdigit()
nota1= input('digite sua primeira nota \n')
while(isNum(nota1) == False):
  print('Digite um valor correto...')
  nota1= input('digite sua primeira nota \n')
nota2= input('digite sua segunda nota nota \n')
while(isNum(nota2) == False):
  print('Digite um valor correto...')
  nota2= input('digite sua segunda nota nota \n')
media = (float(nota1) + float(nota2)) / 2
if media >= 6:
  print('aprovado')
elif media >= 4 and media < 6:
  print('recuperação')
  print('voce precisa tirar:', (media*2 - 18) * -1)
else:
  print('reprovado')