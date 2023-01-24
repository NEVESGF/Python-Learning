# Laços de repetição (normalmente 3 existem em todas as linguas)

# while
# for
# repeat (Não existe em python)

print('-='*20)
print(f"{'AULA QUINZE':^40}")

n=s=0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s +=n
print(f'soma vale {s}')

