import random
import time
print(f'-=-'*20)
print(f'Tente adivinhar o número de 0 a 5')
print(f'-=-'*20)
num = int(input('Escolha um número: '))
num2 = random.randint(0,5)
print('PENSaNDO...')
time.sleep(2)
if num == num2:
    print('Você ganhou')
else:
    print('Você perdeu')
print(f'o número do computador foi {num2} e o escolhido foi {num}')