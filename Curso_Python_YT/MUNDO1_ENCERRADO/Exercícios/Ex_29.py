import colorama
velocidade = float(input('Insira a velocidade do veículo: '))
if velocidade > 80.0:
    multa = (velocidade-80)*7
    print(colorama.Fore.RED + 'MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print(colorama.Fore.RED + 'Você deve pagar uma multa de', colorama.Fore.YELLOW + f'R${multa:.2f}')
print(colorama.Fore.GREEN + 'Tenha um bom dia! Dirija com segurança!')