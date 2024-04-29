# Escreva um programa para aprovar ou negar um empréstimo bancário para compra de um carro, sabendo que a prestação mensal não pode exceder 30% do salário do solicitante e o tempo máximo de financiamento não ultrapasse 5 anos.
def isNum (num):
  return num.isnumeric() | num.replace('.','').isdigit()
salario = input('Digite seu salario \n')
while(isNum(salario) == False):
  salario = input('Digite seu salario \n')
emprestimo = input('Digite o valor do emprestimo desejado \n')
while(isNum(emprestimo) == False):
  emprestimo = input('Digite o valor do emprestimo desejado \n')
parcelas = 60
while(parcelas > 0):
  if(float(emprestimo) / parcelas <= float(salario) * 0.3):
    print(parcelas,'vezes, valor da prestação =',round(float(emprestimo) / parcelas,2))
  parcelas-= 12