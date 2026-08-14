from datetime import date

atual = date.today().year
nasc = int(input("qual sua data de nascimento? "))
idade = atual - nasc

print("quem nasceu em {} tem {} anos em {}".format(nasc, idade, atual))

if idade == 18:
   print("voce tem que se alistar IMEDIATAMENTE!!")

elif idade > 18:
    saldo = idade - 18
    print("Voce ja deveria ter se alistado há {} anos.".format(saldo))

elif idade < 18:
    saldo = 18 - idade
    print("Ainda falta {} anos para vc se alistar.".format(saldo))
