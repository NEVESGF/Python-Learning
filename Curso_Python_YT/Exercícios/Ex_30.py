from colorama import Fore
n1 = float(input('Digite um número qualquer: '))
if (n1 % 2) == 0:
    print(f'O número {n1} é' , Fore.BLUE + 'PAR')
else:
    print(f'O número {n1} é' , Fore.GREEN + 'IMPAR')
