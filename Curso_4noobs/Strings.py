
'Oque é uma string'

string1 = 'Olá Mundo'
string2 = "H4rtDevs é o maior grupo de devs do Brasil"
string3 = """Nossa, bem grande essa strig"""

print(type(string1))
print(type(string2))
print(type(string3))

'transformar tipos diferentes em strings (str)'

string4 = 223313
print(type(string4))
x=str(string4)
print(type(x))

'concatenar uma string basta umas o +'

string5 = "teste" * 3 + "string 2"
print(string5)

"Desconstruindo uma String"
'   utilizando o [x] com um número após uma string é possivel'
'   trazer o caractere relativo aquela posição na string'
'   começa com 0 na primeira letra a esquerda e 1- no último à direita'

String6 = "python"
print(String6[0])
print(String6[-6])

'   se quiser exibir uma parte do texto basta utilizar os : '

print(String6[1:4])

'   se quiser caractéres alternados'

print(String6[0:5:2])

"Métodos internos"
'   O método len, mostra o número de caracteres de uma string.'

String7 = "Python4Noobs"
print(len(String7))

'   O método count verifica quantas vezes determinado caractere aparece'

print(String7.count("o"))

'   Podemos definir também de onde iniciar e onde parar.'
print(String7.count("o",3,7))


"UPPER e LOWER - maiuscula e minuscula"

print(String7.upper())
print(String7.lower())

'Os métodos: Isalnum, replace e split.'
'Isalnum: Retorna true se todos os caracteres forem alfanúmericos.'
'replace:Retorna uma nova string substituindo na string a todas as ocorrências de uma string b por uma nova string c.'
'split:Separa a string a toda vez que for encontrada uma string b.'

String7 = "melancia321"
String8 = "melancia321*%#"
String9 = "Brasil"

print(String7.isalnum())
print(String8.isalnum())
print(String9.replace("s","z"))
print(String9.split("as"))