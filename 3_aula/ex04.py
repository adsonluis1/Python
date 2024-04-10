# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = input('digite uma letra \n').lower()
vogais = ['a','e','i','o']
for item in vogais:
    if letra == item:
      print('vogal')
      break
    else:
        print('consoante')
        break   