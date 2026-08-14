kg = float(input("qual seu peso? "))
altura = float(input("qual sua altura? "))
imc = kg / (altura**2)

print("O IMC dessa pessoa é {:.1f}.".format(imc))

if imc < 18.5:
    print("Você está abaixo do peso")

elif imc > 18.5 and imc < 25:
    print("PARÁBENS!!!! Você está no peso Ideal")

elif imc > 25 and imc < 30:
    print("Sobrepeso")

else:
    print("Obesidade Mórbida")