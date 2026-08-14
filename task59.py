import time
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input("Segundo valor: "))
opcao = 0
while opcao != 5:
    print('''[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa''')
    opcao = int(input('Qual é sua opção? '))
    if opcao == 1:
       soma = n1 + n2
       print("A soma entre {} + {} = {}".format(n1, n2, soma))
    elif opcao == 2:
       soma = n1 * n2
       print("A Multiplicação de {} * {} = {}".format(n1, n2, soma))
    elif opcao == 3:
        if n1 > n2:
            print("O maior numero é: {}".format(n1))
        else:
            print("O maior numero é: {}".format(n2))
    elif opcao == 4:
        print("Informe os numeros novamente:")
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    elif opcao == 5:
        print("Finalizando programa...")

    else:
        print("Opção inválida. Por favor, digite novamente!")

time.sleep(1)
print("===========" *10)
print("fim do programa! volte sempre!")