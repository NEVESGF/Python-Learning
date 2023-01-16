sal = float(input('Qual é o salário do Funcionário? R$'))
print('Um funcionário que ganhava R${:.2f}, com aumento de 15%, passa a receber R${:.2f}'.format(sal,(sal*1.15)))
print(f'Um funcionário que ganhaava R${sal:.2f}, com aumento de 15%, passa a receber R${sal*1.15:.2f}')

# pode-se utilizar f' antes da sentença assim como .format no final