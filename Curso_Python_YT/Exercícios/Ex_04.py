n2 = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(n2))
print('Só tem espaços?', n2.isspace())
print('É um número?', n2.isnumeric())
print('É alfabético?', n2.isalpha())
print('É alfanumérico?', n2.isalnum())
print('Está em maiúscula?', n2.isupper())
print('Está em minuscula?',n2.islower())
print('Está capitalizada?',n2.isidentifier())