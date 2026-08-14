p1 = int(input('qual o primeiro termo: '))
rz = int(input('razao da PA: '))
termo = p1
cont = 1
while cont <= 10:
    print('{} ->'.format(termo), end='')
    teermo += rz
    cont += 1
print('FIM')
pergunta = int(input("Quantos termos vc quer mostrar? "))