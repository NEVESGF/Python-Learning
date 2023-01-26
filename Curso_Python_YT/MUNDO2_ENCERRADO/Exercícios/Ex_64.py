soma = qtd = digite = 0
while digite != 999:
    digite = int(input('Digite o número [999 para parar]: '))
    if digite != 999:
        soma += digite
        qtd += 1
print(f'Você digitou {qtd} números e a soma entre eles foi {soma}.')