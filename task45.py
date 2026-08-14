from random import randint 
from time import sleep            #LIB USADAS

itens = ('pedra', 'papel', 'tesoura') #Lista de opções

jogada_pc = randint(0, 2) #Gerador da opcao do PC

jogada_pessoal = int(input('''Suas opções:
         [0] PEDRA
         [1] PAPEL
         [2] TESOURA
 Qual sua opção? '''))        #opcao do JOGADOR

print('PEDRA')
sleep(1)
print('PAPEL')        #ESTETICA
sleep(1)
print('E TESOURAAA')
sleep(1)


print("="*30)
print("O computador escolheu {}.".format(itens[jogada_pc]))   #Busca em itens o numero que foi gerado pelo PC
print("Você jogou {}".format(itens[jogada_pessoal])) # Busca em intens o numero escolhido pelo JOGADOR
print("="*30)

#CONSEQUENCIAS DE ESCOLHAS
if jogada_pc == 0:
    if jogada_pessoal == 0:
        print("O dois escolheram pedra, EMPATE!!!")

    elif jogada_pessoal == 1:
        print("Você escolheu PAPEL e o computador PEDRA VOCÊ GANHOU PARABÉNS!!")

    elif jogada_pessoal == 2:
        print("Você escolheu TESOURA e o pc PEDRA, VOCÊ PERDEU TENTE NOVAMENTE!")

    else:
        print("jogada invalida")

if jogada_pc == 1:
    if jogada_pessoal == 0:
        print("Você escolheu PEDRA e o pc PAPEL, VOCÊ PERDEU TENTE NOVAMENTE!")

    elif jogada_pessoal == 1:
        print("Os dois escolheram PAPEL, EMPATE!!")

    elif jogada_pessoal == 2:
        print("Você escolheu TESOURA e o computador PAPEL, VOCÊ GANHOU, PARABÉNS!!")

    else:
        print("Jogada inválida!!")



if jogada_pc == 2:
    if jogada_pessoal == 0:
        print("Você escolheu PEDRA e o computador TESOURA, VOCÊ GANHOU PARABÉNS!!")

    elif jogada_pessoal == 1:
        print("Você escolheu PAPEL e o pc TESOURA, VOCÊ PERDEU TENTE NOVAMENTE!")

    elif jogada_pessoal == 2:
        print("Os dois escolheram PAPEL, EMPATE!!")

    else:
        print("Jogada inválida!!")



