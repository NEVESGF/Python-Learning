''' É possivel criar uma lista dentro de uma lista
pessoas=[[pedro,25],[marcos,13],[joana,14]]
            0           1           2 '''

'''print(pessoa[0][0]  Pedro
   print(pessoa[1][1]  19
   print(pessoa[2][0]  João
   print(pessoa[1]     [Pedro,25]'''

teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:])
teste.append('Maria')
teste.append(22)
galera.append(teste[:])
print(galera)

print(galera[0])
print(galera[0][0])
print(galera[0][1])

galera = [['João',19],['Ana',33],['Joaquim',13],['Maria',45]]
for p in galera:
    print(p[0])

