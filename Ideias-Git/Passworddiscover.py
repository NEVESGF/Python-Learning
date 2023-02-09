#Código Funcional para 2 elementos
'''

psw = "10"
b= ""
for l1 in range(0,10):
    a = str(l1)
    print(a)
    if a == psw:
        print(f'ACERTOU a senha é {a}')
        exit()
    else:
        for l2 in range(0,10):
            a2 = str(l2)
            b = (a + a2)
            print(b)
            if b == psw:
                print(f'ACERTOU a senha é {b}')
                exit()

                '''