print('-'*40)
print(f"{'Listagem de preços':^40}")
print('-'*40)
lista = ('Lápis',1.75,'Borracha',2,'Caderno',15.9,'Estojo',25,'Transferidor',4.20,'Compasso',9.99,'Mochila',120.32,'Canetas',22.30,'Livro',34.90)

for c in range (0, len(lista)-1,2):
    print(f'{lista[c]:.<30}R${lista[c+1]:>7.2f}')
print('-'*40)