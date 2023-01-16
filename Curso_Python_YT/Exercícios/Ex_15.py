
#R$ 60 por dia
#R$ 0.15 por km

dias = int(input('Quantos dias alugados? '))
kms = float(input('Quantos Kms rodados? '))
total_dias = int(dias*60)
total_kms = float(kms*0.15)
print(f'O total a pagar é de R${total_dias+total_kms:.2f}')