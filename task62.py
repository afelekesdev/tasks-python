p1 = int(input('qual o primeiro termo: '))
rz = int(input('razao da PA: '))
termo = p1
cont = 1
total = 0
pergunta = 10
while pergunta != 0:
    total = total + pergunta
    while cont <= total:
        print('{} ->'.format(termo), end='')
        termo += rz
        cont += 1
    print('pausa')
    pergunta = int(input("Quantos termos vc quer mostrar? "))
print("FIM")
print(f"Foram mostrados o total de {total} termos")