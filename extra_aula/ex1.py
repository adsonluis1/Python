# Vamos criar um algoritmo para ler uma variável e extrair o máximo de informações: É número? É alfabético? É alfanumérico? Está maiúscula? está minúscula ? Quantos caracteres possui?

import re
var = input('digite... \n')
regex = '^(?=.*[a-zA-Z])(?=.*[0-9])[A-Za-z0-9]+$'

def eAlfanumerico (str):
  p = re.compile(regex)

  if(str == None):
    return False


  if(re.search(p, str)):
      return True
  else:
      return False

if(var.isdigit()):
  print('variavel é um número e possui', len(var), 'casas decimais')

elif(eAlfanumerico(var)):
  if(var.lower() == var):
    print('variavel é um alfanumerico, está em minúscula e possui ', len(var), 'caracteres')
  else:
    print('variavel é um alfanumerico, está em maiuscula e possui ', len(var), 'caracteres')

else:
  if(var.lower() == var):
    print('variavel não é um alfanumerico, está em minúscula e possui ', len(var), 'caracteres')
  else:
    print('variavel não é um alfanumerico, está em maiuscula e possui ', len(var), 'caracteres')