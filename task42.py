a = int(input("digite o lado A do triangulo: "))
b = int(input("digite o lado B do triangulo: "))
c = int(input("digite o lado C do triangulo: "))

if a == b and b == c:
    print("Triangulo Equilatero!")

elif a != b and a != c:
    print("Triangulo Escaleno!")

else:
    print("Triangulo Isosceles!")
    