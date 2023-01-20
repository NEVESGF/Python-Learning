#Tratamento de caracteres

'''Fatiamento
Fatiamento é cortar uma string em um pedaço.

frase = 'Curso em vídeo Python'

frase(9) == 'v'
frase(9:13) == 'vide' #ele exclui o ultimo caractere
frase(9:21) == 'vídeo Python'
frase(9:21:2) == mostra de 9 a 21 mas vai pulando de 2 em 2
frase(:5) == começa antes do zero e vai até o caractére 4
frase(15:) == começa do 15 mas não tem fim
frase(9::3) == começa do 9 e vai até o fim pulando de 3 em 3

   Análise de uma string

len(frase) == mostra o comprimento da frase em caractéres
frase.count('o') == conta quantas vezes aparece a letra o minuscula
frase.count('o',0,3) == conta do 0 até o 12 quantos o minusculos tem
frase.find('deo') == fala quantas vezes encontrou o 'deo' mostrando quando começa
frase.find('Android') == quando não possui a informação ele retorna -1 
'Curso' in frase == True or False

    Transformação

frase.replace('Python','Android') == substitui Python por Android
frase.upper() == faz com que todas as letras fiquem maiusculas
frase.lower() == faz com que todas as letras fiquem minusculas
frase.capitalize() == Faz com que apenas o primeiro caractere da string fique maiuscula
frase.title() == ele analisa quantas palavras existem na frase e torna todas as primeiras letras maiusculas
frase.strip() == remove todos os espaços inuteis no começo e no final da frase
frase.rstrip() == remove todos os espaços no lado direito da string
frase.lstrip() == remove todos os espaços da esquerda da string

    Divisão

frase.split() == divisão dentro da string onde houver espaços recriando indexações da sua frase. Divide cada elemento em uma lista

    Junção

'-'.join(frase) == vai juntar todos os elementos com o separador "-"

'''

frase = 'Curso em Video Python'
print(frase[3]) #usar colchetes
print(frase[3:13])
print(frase[:13])
print(frase[1:15:2])

print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))
print(frase.replace('Python','Android'))

print('Curso' in frase)

print(frase.split())

dividido = frase.split()
print(dividido[0])
print(dividido[2][3])
print(len(frase.split()))
