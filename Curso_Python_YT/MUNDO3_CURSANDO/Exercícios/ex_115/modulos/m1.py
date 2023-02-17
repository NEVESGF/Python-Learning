from time import sleep

def menu():
    try:
        global x
        while True:
            print('-'*40)
            print(f'{"MENU PRINCIPAL":^40}')
            print('-'*40)
            print(f'\033[0;33m1 - \033[0;34mVer pessoas cadastradas\033[m')
            print(f'\033[0;33m2 - \033[0;34mCadastrar nova pessoa\033[m')
            print(f'\033[0;33m3 - \033[0;34mSair do Sistema')
            print('-'*40)
        
            x = str(input('\033[01;33mSua Opção: \033[m'))
            if x.isnumeric():
                if int(x) == 1:
                    cadastrados()
                elif int(x) == 2:
                    cadastrar()
                elif int(x) == 3:
                    sair()
                else:
                    print('\033[31mERRO! Digite uma opção válida\033[m')
                    sleep(0.5)
            else:
                print('\033[0;31mERRO! Digite um número inteiro válido\033[m')
                sleep(0.5)

    except KeyboardInterrupt:
        print('\033[0;31m O usuário forçou o encerramento do sistema! \033[m')


def cadastrar():
    nome = str(input('Nome: '))
    while True:
        idade = str(input('Idade: '))
        if idade.isnumeric():
            idade = int(idade)
            print(f'\033[42mNovo registro de {nome} , {idade} anos adicionado.\033[m',flush=True)
            break
        else:
            print('\033[0;31mDigite um número inteiro válido\033[m')
    
    with open('lista.txt','w',encoding="utf-8") as lista:
        lista.write(f'{nome} {idade} \n')
        lista.close()
    sleep(0.7)


def cadastrados():
    with open('lista.txt','r') as lista:
        print(lista.read())
        lista.close()
    sleep(0.5)

def sair():
    print('-'*40)
    print('''Obrigado por utilizar nosso sistema! 
Volte Sempre''')
    print('-'*40)
    exit()