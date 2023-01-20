import time
from random import randint

itens = ('pedra', 'papel', 'tesoura')
computador = randint(0,2)

player1 = int(input('''escolha umas das opções
[0] pedra
[1]papel
[2]tesoura
'''))
print(10 * ('-'),'JO',10 * ('-'))
time.sleep(3)
print(10 * ('-'),'ken',10 * ('-'))
time.sleep(2)
print(10 * ('-'),'PO',10 * ('-'))
print('o player1 escolheu {}'.format(itens[player1]))

print('o computador escolheu {}'.format(itens[computador]))
print(40 * ('-'))
if computador == 0:
    if player1 == 0:
        print('Empate')
    elif player1 == 1:
        print('player1 ganhou')
    elif player1 == 2:
        print('computador ganhou')
if computador == 1:
    if player1 == 0:
        print('computador ganhou')
    elif player1 == 1:
        print('Empate')
    elif player1 == 2:
        print('player1 ganhou')

if computador == 2:
    if player1 == 0:
        print('player1 ganhou')
    elif player1 == 1:
        print('computador ganhou')
    elif player1 == 2:
        print('Empate')
print(40 * ('-'))

