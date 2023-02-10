def leiaInt(num):
    #global n
    valor = 0
    while True:
        n = str(input(num))
        if n.isnumeric() == True:
            valor = int(n)
            break
        elif n.isnumeric() != True:
            print("\033[0;31mERRO! Digite um número inteiro válido.\033[m")
    return valor
            

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')