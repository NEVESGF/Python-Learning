larg = float(input('Largura da parede: '))
altu = float(input('Altura da parede: '))
area = larg*altu
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.3f}m².'.format(larg,altu,area))
print('Para pintar essa parede, você precisará de {:.4f}l de tinta.'.format(area/2))