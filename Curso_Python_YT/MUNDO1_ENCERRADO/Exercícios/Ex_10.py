din = float(input('Quanto dinheiro você tem na carteira? R$'))
print('Com R${} você pode comprar US${:.2f}'.format(din,(din/5.09)))
print('Com R${} você pode comprar EUR{:.2f}'.format(din,(din/5.51)))