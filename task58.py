from random import randint
print('Sou seu computador...')
print('Acabei de escolher um numero de 0 a 10.')
print('Consegue adivinha qual foi? ')
acertou = False
computador = randint(0, 10)
quantidade = 0

while not acertou:
  player = int(input('Qual é o seu palpite? '))
  quantidade += 1
  if player == computador:
    acertou = True
  else:
    if player < computador:
      print('Mais... Tente mais uma vez.')
    elif player > computador:
      print('Menos... Tente mais uma vez.')

print('Eu escolhi o numero {}. Parabéns, você acertou com {} tentativas, parabens. '.format(computador, quantidade))
