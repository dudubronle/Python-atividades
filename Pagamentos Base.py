v = float(input('valor da compra R$'))
print('''escolha sua forma de pagamento 
[1] á vista dinheiro/cheque 10% DESCONTO 
[2] á vista no cartao/5% DESCONTO 
[3] 3x no cartao de credito\Sem juros
[4] 3x ou mais no cartao de credito com juros''')



opçao = int(input('qual sua forma de pagamento ? '))

if opçao == 1:
    total = v - (v * 10/100)

elif opçao == 2:
    total = v - (v * 5/100)

elif opçao == 3:
    total = v
    parc = total/3
    print('sua compra sera parcelada em 3x e ficará R${:.2f}'.format(parc))

elif opçao == 4:
    total = v + (v * 20/100)
    totparc = int(input('escolha o total de parcelas'))
    parcela = total / totparc
    print('o total de {:.2f} parcelado ficará {:.2f}'.format(v, parcela))


# deve ficar fora dos if e elif
print('o valor {:.2f} ficará {:.2f}'.format(v, total))