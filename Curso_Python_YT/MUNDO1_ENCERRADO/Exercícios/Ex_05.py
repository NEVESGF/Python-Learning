n = int(input('Digite um número: '))
ant = n-1
suc = n+1
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n,ant,suc))

#quanto menos variáveis utilizar, mais memória é consumida do dispositivo.
#usando uma variável

print('Analisando o valor {}, seu antecessor é {} e o seu sucessor é {}'.format(n, (n-1),(n+1)))