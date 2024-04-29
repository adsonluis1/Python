# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
def verificacao (maior,num,menor = 0):
  if(num.isnumeric() == False):
    return True
  elif(int(num) < menor or int(num) > maior):
    return True

def nuns (num, tipo):
  if(len(num) < 2 and tipo != 'ano'):
    return '0'+num
  elif(len(num) == 1 and tipo == 'ano'):
    return '000'+num
  elif(len(num) == 2 and tipo == 'ano'):
    return '00'+num
  elif(len(num) == 3 and tipo == 'ano'):
    return '0'+num
  return num

dia = input('Digite o dia \n')
while(verificacao(31, dia)):
  print('O dia não pode ser menor que 0 e nem maior que 31')
  dia = input('Digite o dia \n')
dia = nuns(dia, 'dia')
print(dia)

mes = input('Digite o mes \n')
while(verificacao(12, mes)):
  print('O mes não pode ser menor que 0 e nem maior que 12')
  mes = input('Digite o mes \n')
mes = nuns(mes, 'mes')
print(mes)

ano = input('Digite o ano \nexemplo: 2005 \n')

while(verificacao(9999999999,ano)):
  print('O ano não pode ser menor que 0')
  ano = input('Digite o ano \nexemplo: 2005 \n')
ano = nuns(ano, 'ano')
print(dia,'/',mes,'/',ano)