def notas(*notas,sit=False):
    """
    --> Função para analisar situação de aluno
    :para n: uma ou mais notas (aceita várias)
    :para sit: valor opcional, indicando se deve ou não adicionar a situação
    :retun: dicionario com varias informações sobre a situação"""
    
    dict = {}
    tot = men = mai = 0

    dict['total'] = len(notas)
    for n in notas:
        if n >= mai:
            dict['maior'] = n
            mai = n
        if men == 0 or n < men:
            dict['menor'] = n
            men = n
        
        tot += n

    dict['média'] = tot/len(notas)

    if sit == True:
        if tot/len(notas) >= 7:
            dict['situação'] = 'BOA'
        elif tot/len(notas) >= 6:
            dict['situação'] = 'RAZOÁVEL'
        else:
            dict['situação'] = 'RUIM'

    return dict

resp = notas(10, 0.3, 3.5, 8, 7.3, 2, 19, sit=True)
print(resp)
