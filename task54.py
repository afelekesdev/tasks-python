from datetime import date
atual = date.today().year      # dia atual de hj
ttmaior = 0
ttmenor = 0
for qnt in range(1,8):
    nas = int(input("Em que ano a pessoa {} nasceu? ".format(qnt)))
    idade = atual - nas   #o dia de hj - recebe o ano de nascimento da pessoa
    if idade >= 18:
        ttmaior += 1
    else:
        ttmenor += 1
print("Foram inseridas {} pessoas, entre ela {} maiores de idade e {} menores.".format(qnt, ttmaior, ttmenor))

