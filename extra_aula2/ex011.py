# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
hTrabalhada = input('Digite quantas horas foram trabalhadas nesse mes \n')
def isNum (num):
   return num.isnumeric() | num.replace('.','').isdigit()
while(isNum(hTrabalhada) ==False):
  hTrabalhada = input('Digite quantas horas foram trabalhadas nesse mes \n')
salarioH = input('Digite quanto voce recebe por hora trabalhada \n')
while(isNum(salarioH)== False):
  salarioH = input('Digite quanto voce recebe por hora trabalhada \n')
salarioBruto = int(hTrabalhada) * float(salarioH)
salarioIr = salarioBruto - salarioBruto * 0.11
salarioInss = salarioIr - salarioIr * 0.08
salarioSindicato = salarioInss - salarioInss * 0.05
print("Salário Bruto", salarioBruto)
print("Pago para o inss: ", round(salarioIr - salarioInss,2))
print("Pago para o sindicato:", round(salarioInss - salarioSindicato,2))
print("Salário líquido :", round(salarioSindicato,2))