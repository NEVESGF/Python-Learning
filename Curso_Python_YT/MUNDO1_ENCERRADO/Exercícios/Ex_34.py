sal = float(input('Qual é o seu salário? R$'))
if sal > 1250:
    print(f'Para o salário de R${sal:.2f} com aumento vai para R${sal*1.1:.2f}')
else:
    print(f'Para o salário de R${sal:.2f} com aumento vai para R${sal*1.15:.2f}')