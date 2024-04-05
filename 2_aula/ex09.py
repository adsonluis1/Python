# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
tempFahrenheit = float(input('digite a temperatura em Fahrenheit \n'))
tempCelcios = (tempFahrenheit - 32) / 1.8
print(round(tempCelcios,1), '°F' )