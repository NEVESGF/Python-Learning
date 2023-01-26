n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
escolha = 0

while escolha != 5:
    if escolha!= 5:
        escolha = int(input('\n[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa \n \n'+'Escolha uma opção \n~'))
        if escolha == 1:
            print(f'A soma dos valores é igual a {n1+n2}')
        elif escolha ==2:
            print(f'A multiplicação dos valores é igaul a {n1*n2}')
        elif escolha ==3:
            print(f'O maior número é {n1}' if n1>n2 else f'O maior número é {n2}')
        elif escolha == 4:
            n1 = float(input('Digite o primeiro valor: '))
            n2 = float(input('Digite o segundo valor: '))
        elif escolha == 5:
            exit()
        else:
            print(f'O número {escolha} é invalido.\nSelecione uma nova opção.')