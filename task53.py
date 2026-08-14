frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juntar = ''.join(palavras)
print ('voce digitou a frase {}'.format(juntar))
inverter = ''
for letra in range(len(juntar) -1, -1, -1):
    inverter += juntar[letra]
if inverter == juntar:
    print("Temos um palíndromo!!")    
else:
    print("A frase digitada não é um palíndromo!")

