#Aula_22

#Modularização, para programas que são muito grandes e precisam ser divididos em diversos pedaços (módulos)
#Objetivo de aumentar a legibilidade e manutenção.

import uteis_22

num = int(input('Digite um valor: '))
fat = uteis_22.fatorial(num)
print(f'O valor de {num} é {fat}')
print(f'O dobro de {num} é {uteis_22.dobro(num)}')

'''Vantagens:

 - Organização do cód.
 - Facilidade na manutenção
 - Ocultação de código detalhado
 - Reutilização em outros projetos'''

# Pacotes, possui varios módulos e varios assuntos de um pacote.
# Os arquivos de pacotes são divididos em pastas e dentro de cada pasta tem que ter um arquivo chamado --init--.py