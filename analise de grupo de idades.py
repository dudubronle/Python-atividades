somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1,5):
    print('______________________')
    nome = str(input('digite seu nome: '))
    idade = int(input('digite sua idade: '))
    sexo = str(input('seu sexo [M/F]'))
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade > 20:
        totmulher20 += 1
médiaidade = somaidade / 4
print('a media do grupo é {} anos'.format(médiaidade))
print('o homem mais velho é {} e tem {} anos'.format(maioridadehomem, nomevelho))
print('no total sao {} mulheres abaixo de 20 anos '.format(totmulher20))

