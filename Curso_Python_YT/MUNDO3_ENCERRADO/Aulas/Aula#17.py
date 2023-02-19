#As listas são mutaveis e utilizam colchetes

lanche=['Dogão','suco','pizza','pudim']
print(lanche[3])
lanche[3]='picole'
print(lanche[3])

#Listas permitem modificações

lanche.append('janduia') #adiciona um item no fim da lista
lanche.insert(0,'jandaia') # adiciona em qualquer posição
del lanche[3] #apaga um elemento escolhido
lanche.pop() #apaga normalmente ultimo elemento
lanche.remove('jandaia') #remove por nome na lista

if 'pizza' in lanche:
    lanche.remove('pizza')

valores=[8,2,3,7,5,4,3]
valores.sort() #ordena os valores
valores.sort(reverse=True) #mostra do maior para o menor
len(valores) #mostra quantidade de itens na lista

#Se falar que uma lista é igual a outra ele cria uma ligação
#ao mudar uma muda a outra, se criar uma cópia não muda

a = [0,1,2,3,4,5]
b = a #cria uma ligação
b = a[:] #Cria uma cópia e pode mudar apenas a b
