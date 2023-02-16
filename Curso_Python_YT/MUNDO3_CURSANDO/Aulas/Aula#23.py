#Tratamento de Erros

try:
    b = int(input('Numerador: '))
    a  = int(input('Denominador: '))
    r = b / a
except (ValueError,TypeError):
    print('Infelizmente tivemos um problema com o tipo de dados digitados')
except ZeroDivisionError:
    print('Não é possivel dividir um número por ZERO')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados')
else:
    print(f'A divisão é igual a {r}')
finally:
    print(f'Volte sempre')