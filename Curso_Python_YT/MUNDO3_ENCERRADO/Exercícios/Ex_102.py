
def fatorial(n=1,show=False):
    """
    --> Calcula o fatorial de um número.
    :para n: O número a ser calculado.
    :para show: (opcional) mostra ou não a conta
    :return: O valor fatorial de um número"""
    print('-'*30)
    if show == False:
        f = 1
        for i in range(n,0,-1):
            f *= i 
        print(f)
    else:
        f = 1
        for i in range(n,0,-1):
            f *= i
            if i > 1:
                print(i,end=' x ')
            elif i == 1:
                print(f'{i} =',end='')
        print(f' {f}')

fatorial()
#help(fatorial)