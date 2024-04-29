# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações: Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado; Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário e encerre o programa; Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário; Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
def isNum(num):
  return num.isnumeric() | num.replace('.','').isdigit()
a = input('Digite o valor de a \n')
while(isNum(a)==False):
  a = input('Digite o valor de a \n')

b = input('Digite o valor de b \n')
while(isNum(a)==False):
  b = input('Digite o valor de b \n')

c = input('Digite o valor de c \n')
while(isNum(a)==False):
  c = input('Digite o valor de c \n')

a=float(a)
b=float(b)
c=float(c)
delta = b*b-4*a*c
if(a <= 0):
  print('Equação não é do segundo grau')
elif(delta <0):
  print('A equação não possui raízes reais')
elif(delta == 0):
  print('A equação possui apenas uma raiz real')
elif(delta > 0):
  print('A equação possui duas raiz reais')
x1 = -b + delta ** 0.5 / 2*a
x2 = -b - delta ** 0.5 / 2*a
print('x1 =', x1, '\nx2=', x2)