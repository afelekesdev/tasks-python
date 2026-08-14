from math import factorial

n = int(input('Digite um numero para calcular seu fatorial: '))
f = factorial(n)
c = n
print("calculando {}! = ".format(n), end='')
while c > 0:
  print('{}'.format(c), end='')
  print(' x ' if c > 1 else ' = ', end='')
  f *= c
  c -= 1
print('{}'.format(n, f))

