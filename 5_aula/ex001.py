# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
horario = input("M-matutino \nV-Vespertino \nN- Noturno \nDigite o horario que voce estuda \n").upper()
while(horario != "M" and horario != "V" and horario != "N"):
  print('Valor inválido, digite de forma correta...')
  horario = input("Digite o horario que voce estuda \n").upper()
if(horario == 'M'):
  print('Bom Dia!')
elif(horario == 'V'):
  print('Boa Tarde!')
else:
  print('Boa Noite!')