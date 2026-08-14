from datetime import date
atual = date.today().year
nascimento = int(input("qual seu ano de nascimento? "))
idade = atual - nascimento
print("o atleta tem {} anos.".format(idade))

if idade <= 9:
    print("Categoria: MIRIM")

elif idade <= 14:
    print("Categoria: INFANTIL")

elif idade <= 19:
    print("Categoria: JUNIOR")

elif idade <= 25:
    print("Categoria: SÊNIOR")

elif idade > 25:
    print("Categoria: MASTER")    