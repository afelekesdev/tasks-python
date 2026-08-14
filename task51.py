n1 = int(input('primeiro termo: '))
razao = int(input('razao: '))
decimo = n1 + (10 - 1) * razao
for i in range(n1, decimo + razao, razao):
    print('{} '.format(i), end=' -> ')
print('STOP PROGRAM')