soma = 0
for i in range (1, 501, 2):
    if i % 3 == 0:
        print(i)
        soma = soma + i
print("A soma de todos os valores solicitados é {}.".format(soma))
