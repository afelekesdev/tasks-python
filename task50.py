soma = 0
cont = 0
for i in range (1, 7):
    vl = int(input("digite o {} valor: ".format(i)))
    if vl % 2 == 0:
        soma += vl
        cont += 1
print("Você informou {} numeros pares e a soma foi {}.".format(cont, soma))