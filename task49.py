print("="*30 + "TABUADA EM PY" + "="*30)

vr = int(input("digite um numero para ver a tabuada: "))

for i in range (1, 21):
    soma = vr*i
    print("{} x {:2} = {}".format(vr, i, soma))