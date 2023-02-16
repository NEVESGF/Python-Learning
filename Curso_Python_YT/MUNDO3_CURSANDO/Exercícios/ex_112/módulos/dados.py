def leiaDinheiro(dinheiro):
    while True:
        q = input(str(dinheiro)).replace(' ','').replace(',','.')
        if q.isalpha():
            print(f'\033[0;31mERRO: "{q}" é um preço inválido!\033[m')
        else:
            dinheiro = float(q)
            break

    return dinheiro