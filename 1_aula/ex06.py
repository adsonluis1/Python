# sexto codigo
sexo = input('qual o seu sexo ? H=homem ou M=mulher \n')
while sexo.upper() != 'H' and sexo.upper() != 'M':
    sexo = input('qual o seu sexo ? H=homem ou M=mulher \n')
altura = float(input('digite sua altura \n'))
if sexo.upper() == 'H':
    print(round((72.7 * altura) - 58,2))
if sexo.upper() == 'M':
    print(round((62.1 * altura) - 44.7,2))