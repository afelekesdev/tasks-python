print("="*20 + "Lojas Python" + "="*20)

vl_compra = int(input("qual valor da compra? "))

print('''FORMAS DE PAGAMENTO
[1] a vista dinheiro/cheque 
[2] a vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')

opcao = int(input("qual opção? "))

if opcao == 1:
    vl_compra2 = vl_compra - (vl_compra * 0.10)
    print("vc iria pagar o valor de {}, com desconto o valor fica {}.".format(vl_compra, vl_compra2))

elif opcao == 2:
    vl_avista = vl_compra - (vl_compra * 0.05)
    print("Sua compra era {}, com desconto vai sair por: R${}.".format(vl_compra, vl_avista))

elif opcao == 3:
    vl_cartao = vl_compra / 2
    print("o valor em 2x fica: 2x de {}.".format(vl_cartao))

elif opcao == 4:
    qnt_parcelas = int(input("em quantas parcelas: "))
    if qnt_parcelas >= 3:
        vl_juros = (vl_compra + (vl_compra * 0.20)) / qnt_parcelas
        print("o valor era {}, em {}x o valor da parcela sai a: R${:.2f}.".format(vl_compra, qnt_parcelas, vl_juros))