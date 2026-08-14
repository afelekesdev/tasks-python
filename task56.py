somaidade = 0 
mdidade = 0
maior_idadeh = 0
nomevelho = ''
mulheres_idade = 0
for p in range (1, 5):
    print("----- {} PESSOA -----".format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade  #SOMA DE TODAS AS IDADES DIGITADAS
    if p == 1 and sexo in "Mm":
        maior_idadeh = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maior_idadeh:
        maior_idadeh = idade
        nomevelho = nome 
    if sexo in "Ff" and idade < 20:  #SE MULHERES MENOS DE 20 ANOS, ARMAZENA EM mulheres_idade
        mulheres_idade 

mdidade = somaidade / 4 #CALCULO DA MEDIA DAS IDADES
print("A media de idade do grupo é de: {}".format(mdidade))
print("O homem mais velho tem {} anos e se chama {}".format(maior_idadeh, nomevelho))
print("Ao total {} mulheres tem menos de 20 anos.".format(mulheres_idade))