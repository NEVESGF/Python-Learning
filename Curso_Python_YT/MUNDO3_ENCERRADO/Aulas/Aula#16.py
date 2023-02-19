#Tuplas 
#AS TUPLAS SÃO ENTRE PARENTESES

lanche = ('Hamburguer','Suco','Pizza','Pudim')
for c in lanche:
    print(f'Eu vou comer {c}')
print('Comi muito!')

for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')

for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida} na posição {pos}')

# AS TUPLAS SÃO IMUTAVEIS, NÃO É POSSIVEL ALTERA-LAS

print(sorted(lanche)) #coloca em ordem
print(lanche)

a = (2, 4, 5)
b = (3, 8, 12, 18)
c = a + b
print(c)
print(c.count(5)) #Quantas vezes aparece na tupla essa info
print(c.index(5)) #Mostra em qual posição está aquele número

#pode ter dados de varios tipos dentro de uma tuplas
