sexo = str(input("Informe seu sexo: [M ou F] ")).strip().upper()[0]

while sexo not in 'MmFf':
  sexo = str(input('Dados inválido, por favor, informe o dado correto: '))

print('Sexo {} registrado com sucesso.'.format(sexo))
