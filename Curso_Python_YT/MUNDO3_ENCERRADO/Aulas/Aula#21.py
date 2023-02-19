''' Interactive Help
    Docstring
    Argumentos opcionais
    Escopo de variaveis
    Retorno de resultados'''

#interactive help basta digitar help()
#help(len)

#Docstrings (manual da função que você mesmo criou)
def contador(i, f, p):
    """
    --> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c< f:
        print(f'{c} ',end=' ')
        c += p
    print('FIM')

#help(contador)
contador(0,100,10)

#Argumentos opicionais
def somar(a,b,c=0):
    s = a + b + c
    print(f'A soma vale {s}')

somar(3,2) #Como colocou o =0 na frente do C o C vira um argumento opcional assim como poderia colocar para todos os argumentos

#Escopo de variaveis
def teste():
    global x
    x=8
    print(f'Na função teste n vale {n}')
    print(f'Na função teste x vale {x}')

n = 2
#X não funciona aqui pois foi definida apenas para def
#se criar outro n no def ele cria uma nova variavel local apenas para o def
#para funcionar global dentro da def digitar global "variavel" antes da variavel
print(n)
teste()
print(x)


#Retorno de valores
def somart(a=0,b=0,c=0):
    s = a + b + c
    #print(f'A soma vale {s}')
    return s #Utilizando o return ele não imprime o valor quando chamar a def ele define s como o valor solicitado

r1 = somart(3,2,5)
r2 = somart(1,7)
r3 = somart(4)

print(f'Meus cálculos deram {r1}, {r2} e {r3}')
