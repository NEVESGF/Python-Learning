from módulos import moeda,dados

p = dados.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p,float(input('Qual a porcentagem de aumento? ')),float(input('Qual a porcentagem de redução? ')))