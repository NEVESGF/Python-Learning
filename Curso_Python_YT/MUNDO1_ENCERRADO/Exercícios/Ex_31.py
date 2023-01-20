import emoji
dist = float(input('Qual a distância em KM da sua viagem? '))
print(f'Você esta prestes a iniciar uma viagem de {dist}Km')
if dist > 200:
    print(f'O valor da sua viagem será de R${dist*0.45:.2f}')
else:
    print(f'O valor da sua viagem será de R${dist*0.5:.2f}')
print(emoji.emojize('Tenha uma excelente viagem :bus:'))
