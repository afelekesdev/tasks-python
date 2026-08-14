maior = 0 # variaveis sem valores
menor = 0
for pessoas in range(1, 6):
    peso = float(input("Qual peso da {} pessoa? ".format(pessoas)))
    if pessoas == 1: #faz a comparação com a primeira pessoa
        maior = peso
        menor = peso  #recebe o valor e armazena na varial que estava sem valor
    else:
        if peso > maior:   #se o peso digitado for maior que o anterior, ele armazena em "maior"
            maior = peso
        if peso < menor: #mesma coisa vale para o menor.
            menor = peso
print("O MAIOR peso é: {}".format(maior))
print("O MENOR peso é: {}".format(menor))