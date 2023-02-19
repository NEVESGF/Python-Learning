def aumentar(n_a,p_a):
    return n_a * ((p_a/100) +1)

def diminuir(n_d,p_d):
    return n_d * (1-(p_d/100))

def dobro(n_do):
    return n_do * 2

def metade(n_me):
    return n_me / 2

def moeda(n_moe = 0.0, moeda ='R$'):
    return f'{moeda}{n_moe:.2f}'.replace(".",",")
    
    