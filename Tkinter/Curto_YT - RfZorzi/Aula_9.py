from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()

#AULA7

# https://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html#conectando-e-desconectando-do-banco

class Funcs():
    def limpa_tela(self):
        self.codigo_entry.delete(0,END)
        self.nome_entry.delete(0,END)
        self.telefone_entry.delete(0,END)
        self.cidade_entry.delete(0,END)
        self.estado_entry.delete(0,END)
    def conecta_bd(self):
        self.conn = sqlite3.connect("clientes.bd"); print("Conectando ao banco de dados")
        self.cursor = self.conn.cursor()
    def desconectar_bd(self):
        self.conn.close(); print("Desconectado do banco de dados")
    def montaTabelas(self):

        self.conecta_bd()
        ### Criar tabela
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            cod INTEGER PRIMARY KEY,
            nome_cliente CHAR(40) NOT NULL,
            telefone INTEGER(20),
            cidade CHAR(40),
            estado CHAR(10)
        );
        """)
        self.conn.commit(); print("Banco de dados criado")
        self.desconectar_bd()
    def add_cliente(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.cidade = self.cidade_entry.get()
        self.estado = self.estado_entry.get()
        self.conecta_bd()

        self.cursor.execute(""" INSERT INTO clientes (nome_cliente, telefone, cidade, estado)
            VALUES (?, ?, ?, ?)""", (self.nome, self.telefone, self.cidade, self.estado))
        self.conn.commit()
        self.desconectar_bd()
        self.select_lista()
        self.limpa_tela()
    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade, estado FROM clientes
            ORDER BY nome_cliente ASC;""")
        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconectar_bd()


class Application(Funcs): 

    # https://docs.python.org/3/tutorial/classes.html
    # https://www.hackerearth.com/practice/python/object-oriented-programming/classes-and-objects-i/tutorial/
    
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.montaTabelas()
        self.select_lista()
        root.mainloop() #Informação básica necessária para se abrir uma janela no Tkinter 
    def tela(self):
        self.root.title("Cadastro de Clientes") #title = titulo da janela que será aberta
        self.root.configure(background= "#1e3843") #configure background define a cor de fundo da janela (utilziar hexadecimal para cores mais agradáveis)
        self.root.geometry("700x500") #define o tamanho de inicio da janela horizontal x vertical
        self.root.resizable(True, True) #habilita se a tela vai ser responsiva quanto a modificação de tamanho true (horizontal), true (vertical)
        self.root.maxsize(width= 900, height= 700) #define o tamanho máximo que a janela pode adquirir
        self.root.minsize(width=500,height=400) #define o tamanho mínimo que a janela pode adquirir
    # AULA 2 DAQUI EM DIANTE
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd =4, bg = "#dfe3ee", 
                             highlightbackground= "#759fe6", highlightthickness=3)
        # place(coloca em x e y o objeto) pack(coloca apenas em posições especificas) grid(transforma a tela em uma planilha) - 3 tipos de packs para frames no tkinter
        self.frame_1.place(relx= 0.02, rely=0.02, relwidth = 0.96, relheight = 0.46) # Funciona de 0 a 1 (direita, esquerda / baixo, cima) em porcentagem
        
        self.frame_2 = Frame(self.root, bd =4, bg = "#dfe3ee", 
                             highlightbackground= "#759fe6", highlightthickness=3)
        # place(coloca em x e y o objeto) pack(coloca apenas em posições especificas) grid(transforma a tela em uma planilha) - 3 tipos de packs para frames no tkinter
        self.frame_2.place(relx= 0.02, rely=0.5, relwidth = 0.96, relheight = 0.46) # Funciona de
    # AULA 3 DAQUI EM DIANTE
    def widgets_frame1(self):
        ### Criação do botão limpar
        self.bt_limpar = Button(self.frame_1, text = "Limpar",bd=2,bg='#107bd2',fg='white',
                                font=('verdana',8,'bold'),command=self.limpa_tela)
        self.bt_limpar.place(relx = 0.2 , rely= 0.1, relwidth=0.1, relheight=0.16)

        ### Criação do botão buscar
        self.bt_buscar = Button(self.frame_1, text = "Buscar",bd=2,bg='#107bd2',fg='white',font=('verdana',8,'bold'))
        self.bt_buscar.place(relx = 0.3 , rely= 0.1, relwidth=0.1, relheight=0.16)

        ### Criação do botão novo
        self.bt_novo = Button(self.frame_1, text = "Novo",bd=2,bg='#107bd2',fg='white',
                              font=('verdana',8,'bold'),command=self.add_cliente)
        self.bt_novo.place(relx = 0.6 , rely= 0.1, relwidth=0.1, relheight=0.16)

        ### Criação do botão alternar
        self.bt_alternar = Button(self.frame_1, text = "Alternar",bd=2,bg='#107bd2',fg='white',font=('verdana',8,'bold'))
        self.bt_alternar.place(relx = 0.7 , rely= 0.1, relwidth=0.1, relheight=0.16)

        ### Criação do botão apagar
        self.bt_apagar = Button(self.frame_1, text = "Apagar",bd=2,bg='#107bd2',fg='white',font=('verdana',8,'bold'))
        self.bt_apagar.place(relx = 0.8 , rely= 0.1, relwidth=0.1, relheight=0.16)

        # AULA 4 DAQUI EM DIANTE

        #  Criação da Label e entrada do código
        self.lb_codigo = Label(self.frame_1, text = "Código",bg='#dfe3ee',fg='#107db2') #Label cria uma nota na tela
        self.lb_codigo.place(relx= 0.05, rely=0.05) 

        self.codigo_entry = Entry(self.frame_1) #Cria uma caixa de texto (input)
        self.codigo_entry.place(relx= 0.05, rely=0.15, relwidth=0.1)

        #  Criação da Label e entrada do nome
        self.lb_nome = Label(self.frame_1, text = "Nome",bg='#dfe3ee',fg='#107db2')
        self.lb_nome.place(relx= 0.05, rely=0.35)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx= 0.05, rely=0.45, relwidth=0.85, relheight=0.12)

        #  Criação da Label e entrada do telefone
        self.lb_telefone = Label(self.frame_1, text = "Telefone",bg='#dfe3ee',fg='#107db2')
        self.lb_telefone.place(relx= 0.05, rely=0.60)

        self.telefone_entry = Entry(self.frame_1)
        self.telefone_entry.place(relx= 0.05, rely=0.70, relwidth=0.4, relheight=0.12)

        #  Criação da Label e entrada do cidade
        self.lb_cidade = Label(self.frame_1, text = "Cidade",bg='#dfe3ee',fg='#107db2')
        self.lb_cidade.place(relx= 0.5, rely=0.6)

        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx= 0.5, rely=0.7, relwidth=0.25, relheight=0.12)


        ### NÃO PRESENTE NO CURSO, ADICIONADO POR CONTA

        #  Criação da Label e entrada do Estado
        self.lb_estado = Label(self.frame_1, text = "Estado",bg='#dfe3ee',fg='#107db2')
        self.lb_estado.place(relx= 0.795, rely=0.6)

        self.options = StringVar(root) #Opção selecionada pelo usuário será definida como self.options
        self.estados = ("AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO")
        self.estado_entry = ttk.Combobox(root,textvariable=self.options,values=self.estados)
        self.estado_entry.place(relx= 0.78, rely=0.335, relwidth=0.1, relheight=0.05)

        ### ATÉ AQUI
    # AULA 6 DAQUI EM DIANTE
    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height=3, columns=("col1","Col2","col3","col4","col5"))
        
        ### Definição do nome de cada uma das colunas criadas anteriormente na Treeview
        self.listaCli.heading("#0",text="")
        self.listaCli.heading("#1",text="Cód.")
        self.listaCli.heading("#2",text="Nome")
        self.listaCli.heading("#3",text="Telefone")
        self.listaCli.heading("#4",text="Cidade")
        self.listaCli.heading("#5",text="Estado")

        ### Definição do tamanho de cada uma das colunas
        self.listaCli.column("#0",width=0,stretch=NO)
        self.listaCli.column("#1",width=40)
        self.listaCli.column("#2",width=200)
        self.listaCli.column("#3",width=125)
        self.listaCli.column("#4",width=125)
        self.listaCli.column("#5",width=100)

        ### Posicionando a lista no frame 2
        self.listaCli.place(relx=0.02,rely=0.05, relwidth=0.95,relheight=0.9)

        self.scrollLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscrollcommand=self.scrollLista.set)
        self.scrollLista.place(relx=0.97, rely=0.05, relwidth=0.02, relheight=0.9)

Application()