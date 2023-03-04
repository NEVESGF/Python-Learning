import sqlite3
from faker import Faker

'''
GERADOR DE BANCO DE DADOS PARA TESTE DO PROGRAMA DE CADASTRO
'''
fake = Faker('pt_BR')

# Gerar email aleatório com base no nome
def generate_email(name):
    return f"{name.lower().replace(' ', '_')}@{fake.free_email_domain()}"

# Criar tabela e inserir dados
def create_table():
    conn = sqlite3.connect('clientes.bd')
    c = conn.cursor()

    c.execute('''CREATE TABLE clientes
                 (cod INTEGER PRIMARY KEY,
                 nome_cliente TEXT,
                 telefone TEXT,
                 cidade TEXT,
                 estado TEXT,
                 email TEXT)''')

    for i in range(1, 1001):
        nome_cliente = fake.name_nonbinary()
        telefone = fake.cellphone_number() 
        cidade = fake.city()
        estado = fake.state_abbr()
        email = generate_email(nome_cliente)
        c.execute(f"INSERT INTO clientes (cod, nome_cliente, telefone, cidade, estado, email) VALUES ({i}, '{nome_cliente}', '{telefone}', '{cidade}', '{estado}', '{email}')")

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_table()