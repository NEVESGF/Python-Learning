print('-'*20)
print(f"{'Loja Super Baratão':20}")
print('-'*20)
produto = continuar = produto_barato = ' '
preco = preco_total = qtd = barato = contmil = 0
while True:
    produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$'))
    preco_total += preco
    qtd += 1
    if qtd == 1 or barato <= preco:
        barato = preco
        produto_barato = produto
    if preco > 1000:
        contmil+=1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f"{'FIM DO PROGRAMA':-^20}")
print(f'O total da compra foi R${preco_total}')
print(f'Temos {contmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {produto_barato} que custa R${barato:.2f}')

