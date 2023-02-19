palavra = ('aprender','programar','linguagem','python','curso','gratis','estudar','praticar','trabalhar','mercado','programador','futuro')

for p in palavra:
    print(f'\nNa palavra {p} temos: ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')