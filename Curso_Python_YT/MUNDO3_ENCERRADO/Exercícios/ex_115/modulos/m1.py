from time import sleep

def menu():
    try:
        #global x
        while True:
            print('-'*40)
            print(f'{"MENU PRINCIPAL":^40}')
            print('-'*40)
            print('\033[0;33m1 - \033[0;34mVer pessoas cadastradas\033[m')
            print('\033[0;33m2 - \033[0;34mCadastrar nova pessoa\033[m')
            print('\033[0;33m3 - \033[0;34mSair do Sistema')
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
    
    with open('lista.txt','r+',encoding="utf-8") as lista:
    
        my_list = []
        for i in lista.readlines():
            my_list.append(i.split(";"))

        lista.write(f"\n{nome};{idade}")
        
    sleep(0.7)


def cadastrados():
    with open("lista.txt","r",encoding='utf-8') as lista:
        my_list = []
        for i in lista.readlines():
            my_list.append(i.split(";"))
    c = 1
    for n in my_list:
        if c < len(my_list):
            print(f"{n[0]:.<30} {n[1]}",end='')
        elif c == len(my_list):
            print(f"{n[0]:.<30} {n[1]}")
        c += 1
    sleep(0.5)

def sair():
    print('-'*40)
    print('''Obrigado por utilizar nosso sistema! 
Volte Sempre''')
    print('-'*40)
    exit()