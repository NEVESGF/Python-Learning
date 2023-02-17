import urllib.request

def connect(host='http://pudim.com.br'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

# test
print( '\033[0;33mConsegui acessar o site Pudim com sucesso! \033[m' if connect() else '\033[0;31mNão foi possivel acessar o site do Pudim!\033[m' )