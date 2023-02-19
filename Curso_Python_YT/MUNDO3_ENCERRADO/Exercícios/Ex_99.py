from time import sleep
def analise(*num):
    print('-='*20)
    print('Análisando os valores passados...')
    for i in num:
        print(f'{i}',end=' ',flush=True)
        sleep(0.25)
    print(f'Foram informados {len(num)} ao todo.')
    print(f'O maior valor informado foi {sorted(num)[len(num)-1] if len(num)>0 else 0}')
    print('-='*20)

analise(2,9,4,5,7,1)
analise(4,7,0)
analise(1,2)
analise(6)
analise()