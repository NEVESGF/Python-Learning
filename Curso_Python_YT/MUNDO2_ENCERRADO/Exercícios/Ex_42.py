print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
print('')
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos PODEM FORMAR um triângulo ', end='')
    if s1 == s2 == s3:
        print('EQUILÁTERO')
    elif s1 == s2 != s3 or s1 == s3 != s2 or s2 == s3 != s1:
        print('ISÓCELES')
    else:
        print('ESCALENO')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')