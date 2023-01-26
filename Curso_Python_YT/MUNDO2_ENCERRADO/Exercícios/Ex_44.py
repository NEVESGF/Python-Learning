from time import sleep
print('='*11 + 'LOJAS DE PYTHON' + '='*11)
print('Olá caro Cliente')
preco = float(input('Qual total das compras? R$'))
sleep(0.3)
print('FORMAS DE PAGAMENTO')
sleep(0.1)
print('[ 1 ] à vista dinheiro/cheque')
sleep(0.1)
print('[ 2 ] à vista cartão')
sleep(0.1)
print('[ 3 ] 2x no cartão')
sleep(0.1)
print('[ 4 ] 3x ou mais no cartão')
sleep(0.1)
op = int(input('\n Qual a forma de pagamento? ~'))
print(f'Sua compra de R${preco:.2f} vai custar', end=' ')
if op == 1:
    print(f'R${preco*0.9:.2f}')
elif op ==2:
    print(f'R${preco*0.95:.2f}')
elif op ==3:
    print(f'R${preco}')
elif op ==4:
    print(f'R${preco*1.2}')
else:
    print(' ------- \nEssa não é uma opção válida.')
    exit()
sleep(0.1)
escolha = input('Deseja seguir para o pagamento ? (Y/N) ~')
if escolha == 'Y':
    sleep(0.5)
    print('Processando pagamento...')
    sleep(0.3)
    print('Contatando seu banco...')
    sleep(1.0)
    print('Pagamento aprovado...')
    sleep(0.5)
    print('Obrigado pela preferência, volte sempre!')
else:
    print('Operação cancelada!')
