def aumentar(n_a,p_a, formato=False):
    res = n_a * ((p_a/100) +1)
    return res if formato is False else (moeda(res))

def diminuir(n_d,p_d,formato=False):
    res = n_d * (1-(p_d/100))
    return res if formato is False else (moeda(res))

def dobro(n_do,formato=False):
    res = n_do * 2
    return res if formato is False else (moeda(res))

def metade(n_me,formato=False):
    res = n_me / 2
    return res if formato is False else (moeda(res))

def moeda(n_moe = 0.0, moeda ='R$'):
    return f'{moeda}{n_moe:.2f}'.replace(".",",")
    
    