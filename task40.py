n1 = float(input("Digite o valor da sua 1ª nota: "))
n2 = float(input("Digite o valor da sua 2ª nota: "))
media = (n1 + n2) / 2

print("Tirando {} e {}, a media do aluno é {}".format(n1, n2, media))

if media < 5.0:
    print('Você está Reprovado!!')

elif media > 5.0 and media < 6.9:
    print("você está em recuperação!!!!!")

else:
    print("você está aprovado!!!")
