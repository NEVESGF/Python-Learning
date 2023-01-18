frase = str(input('Digite uma frase: ').strip())
print(f'A letra A aparece {frase.upper().count("A")} vezes na frase.')
print(f'A primeira letra A apareceu na posição {frase.upper().find("A")+1}')
print(f'A última letra A apareceu na posição {frase.upper().rfind("A")+1}')