from tkinter import *
from tkinter import ttk
import sqlite3

from time import sleep
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics   
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser
import datetime

root = Tk()

class Relatorios():
    def printCliente(self):
        webbrowser.open("cliente.pdf")
    def gerarRelatCliente(self):
        self.c = canvas.Canvas("cliente.pdf")

        self.codigoRel = self.codigo_entry.get()
        self.nomeRel = self.nome_entry.get()
        self.telefoneRel = self.telefone_entry.get()
        self.cidadeRel = self.cidade_entry.get()
        self.estadoRel = self.estado_entry.get()

        self.c.setFont("Helvetica-Bold",24)
        self.c.drawString(50,795,'-'*60)
        self.c.drawString(200,775,'Ficha do Cliente')
        self.c.drawString(50,755,'-'*60)

        self.c.setFont("Helvetica-Bold",18)
        self.c.drawString(50,700,'Cód.: ')
        self.c.drawString(50,670,'Nome: ')
        self.c.drawString(50,630,'Telefone: ')
        self.c.drawString(50,600,'Cidade: ')
        self.c.drawString(50,570,'Estado: ')

        self.c.setFont("Helvetica",16)
        self.c.drawString(150,700, self.codigoRel)
        self.c.drawString(150,670, self.nomeRel)
        self.c.drawString(150,630, self.telefoneRel)
        self.c.drawString(150,600, self.cidadeRel)
        self.c.drawString(150,570, self.estadoRel)

        from datetime import datetime
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        self.c.setFont("Helvetica",10)
        self.c.drawString(50,450, "Este documento é fornecido para simples conferência e contém informações confidenciais")
        self.c.drawString(50,430, "que são de propriedade exclusiva da empresa/organização.")
        self.c.drawString(50,410,"Por favor, esteja ciente de que qualquer divulgação não autorizada dessas informações ")
        self.c.drawString(50,390,"é estritamente proibida. Agradecemos sua cooperação na proteção dessas informações e ")
        self.c.drawString(50,370,"na manutenção da confidencialidade dos dados contidos neste relatório.")
            
        self.c.drawString(50,330, 'Relatório gerado em: ' + dt_string)

        self.c.rect(40,300,500,190,fill=False,stroke=True)

        self.c.showPage()
        self.c.save()
        self.printCliente()


#AULA7

# https://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html#conectando-e-desconectando-do-banco

class Funcs():
    def limpa_tela(self):
        self.codigo_entry.delete(0,END)
        self.nome_entry.delete(0,END)
        self.telefone_entry.delete(0,END)
        self.cidade_entry.delete(0,END)
        self.estado_entry.delete(0,END)
        self.email_entry.delete(0,END)
    def conecta_bd(self):
        self.conn = sqlite3.connect("clientes.bd"); Label(root,text="Conectado ao banco de dados...",bg="#1e3843", font=("Arial", 10)).place(relx=0.65,rely=0.96) #print("Conectando ao banco de dados")

        self.cursor = self.conn.cursor()
    def desconectar_bd(self):
        self.conn.close(); Label(root,text="Desconectado do banco de dados...",bg="#1e3843", font=("Arial", 10)).place(relx=0.65,rely=0.96) #print("Desconectado do banco de dados")
    def montaTabelas(self):

        self.conecta_bd()
        ### Criar tabela
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            cod INTEGER PRIMARY KEY,
            nome_cliente CHAR(40) NOT NULL,
            telefone INTEGER(20),
            cidade CHAR(40),
            estado CHAR(10),
            email CHAR(20)
        );
        """)
        self.conn.commit(); Label(root,text="Banco de dados criado...",bg="#1e3843", font=("Arial", 10)).place(relx=0.65,rely=0.96) #print("Banco de dados criado")
        self.desconectar_bd()
    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.cidade = self.cidade_entry.get()
        self.estado = self.estado_entry.get()
        self.email = self.email_entry.get()
    def add_cliente(self):
        self.variaveis()
        self.conecta_bd()

        self.cursor.execute(""" INSERT INTO clientes (nome_cliente, telefone, cidade, estado, email)
            VALUES (?, ?, ?, ?, ?)""", (self.nome, self.telefone, self.cidade, self.estado, self.email))
        self.conn.commit()
        self.desconectar_bd()
        self.select_lista()
        self.limpa_tela()
    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade, estado, email FROM clientes
            ORDER BY nome_cliente ASC;""")
        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconectar_bd()
    def onDoubleClick(self,event):
        self.limpa_tela()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1, col2, col3, col4, col5,col6 = self.listaCli.item(n,'values')
            self.codigo_entry.insert(END,col1)
            self.nome_entry.insert(END,col2)
            self.telefone_entry.insert(END,col3)
            self.cidade_entry.insert(END,col4)
            self.estado_entry.insert(END,col5)
            self.email_entry.insert(END,col6)
    def deleta_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute("""DELETE FROM clientes WHERE cod = ? """, [self.codigo])
        self.conn.commit()
        self.desconectar_bd()
        self.limpa_tela()
        self.select_lista()
    def alterar_clientes(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute("""UPDATE clientes SET nome_cliente = ?, telefone = ?, cidade = ?, estado = ?, email = ?
            WHERE cod = ? """, (self.nome, self.telefone, self.cidade, self.estado, self.email, self.codigo))
        self.conn.commit()
        self.desconectar_bd()
        self.select_lista()
        self.limpa_tela()
    def busca_cliente(self):
        self.conecta_bd()
        self.listaCli.delete(*self.listaCli.get_children())

        self.nome_entry.insert(END,'%')
        nome = self.nome_entry.get()
        self.cursor.execute(
            """ SELECT cod, nome_cliente, telefone, cidade, estado, email FROM clientes
            WHERE nome_cliente LIKE '%s' ORDER BY nome_cliente ASC """ % nome)
        buscanomeCli = self.cursor.fetchall()
        for i in buscanomeCli:
            self.listaCli.insert("",END,values=i)
        self.limpa_tela()
        self.desconectar_bd()

class Application(Funcs,Relatorios): 

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
        self.Menus()
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

        self.abas = ttk.Notebook(self.frame_1)
        self.aba1 = Frame(self.abas)
        self.aba2 = Frame(self.abas)

        self.aba1.configure(background="#dfe3ee")
        self.aba2.configure(background="#dfe3ee")

        self.abas.add(self.aba1,text = "Cadastro e Visualização")
        self.abas.add(self.aba2, text = "Aba 2")

        self.abas.place(relx=0, rely=0,relwidth=0.98, relheight=0.98)

        #self.canvas_bt = Canvas(self.frame_1, bd=0, bg='black', highlightbackground='gray',highlightthickness=3)
        #self.canvas_bt.place(relx=0.19,rely=0.08,relwidth=0.22,relheight=0.19)

        ### Criação do botão limpar
        self.bt_limpar = Button(self.aba1, text = "Limpar",bd=2,bg='#107bd2',fg='white',
                                font=('verdana',8,'bold'),command=self.limpa_tela,)
        self.bt_limpar.place(relx = 0.2 , rely= 0.1, relwidth=0.1, relheight=0.16)

        ### Criação do botão buscar
        self.bt_buscar = Button(self.aba1, text = "Buscar",bd=2,bg='#107bd2',fg='white',
                                font=('verdana',8,'bold'),command=self.busca_cliente)
        self.bt_buscar.place(relx = 0.3 , rely= 0.1, relwidth=0.1, relheight=0.16)

        ### Criação do botão novo
        self.bt_novo = Button(self.aba1, text = "Novo",bd=2,bg='#107bd2',fg='white',
                              font=('verdana',8,'bold'),command=self.add_cliente)
        self.bt_novo.place(relx = 0.6 , rely= 0.1, relwidth=0.1, relheight=0.16)

        ### Criação do botão alternar
        self.bt_alternar = Button(self.aba1, text = "Alternar",bd=2,bg='#107bd2',fg='white',
                                  font=('verdana',8,'bold'),command=self.alterar_clientes)
        self.bt_alternar.place(relx = 0.7 , rely= 0.1, relwidth=0.1, relheight=0.16)

        ### Criação do botão apagar
        self.bt_apagar = Button(self.aba1, text = "Apagar",bd=2,bg='#107bd2',fg='white',
                                font=('verdana',8,'bold'),command=self.deleta_cliente)
        self.bt_apagar.place(relx = 0.8 , rely= 0.1, relwidth=0.1, relheight=0.16)

        # AULA 4 DAQUI EM DIANTE

        #  Criação da Label e entrada do código
        self.lb_codigo = Label(self.aba1, text = "Código",bg='#dfe3ee',fg='#107db2') #Label cria uma nota na tela
        self.lb_codigo.place(relx= 0.05, rely=0.05) 

        self.codigo_entry = Entry(self.aba1) #Cria uma caixa de texto (input)
        self.codigo_entry.place(relx= 0.05, rely=0.15, relwidth=0.1)

        #  Criação da Label e entrada do nome
        self.lb_nome = Label(self.aba1, text = "Nome",bg='#dfe3ee',fg='#107db2')
        self.lb_nome.place(relx= 0.05, rely=0.35)

        self.nome_entry = Entry(self.aba1)
        self.nome_entry.place(relx= 0.05, rely=0.45, relwidth=0.4, relheight=0.12)

        #  Criação da Label e entrada do E-mail
        self.lb_email = Label(self.aba1, text = "E-mail",bg='#dfe3ee',fg='#107db2')
        self.lb_email.place(relx= 0.5, rely=0.35)

        self.email_entry = Entry(self.aba1)
        self.email_entry.place(relx= 0.5, rely=0.45, relwidth=0.401, relheight=0.12)

        #  Criação da Label e entrada do telefone
        self.lb_telefone = Label(self.aba1, text = "Telefone",bg='#dfe3ee',fg='#107db2')
        self.lb_telefone.place(relx= 0.05, rely=0.60)

        self.telefone_entry = Entry(self.aba1)
        self.telefone_entry.place(relx= 0.05, rely=0.70, relwidth=0.4, relheight=0.12)

        #  Criação da Label e entrada do cidade
        self.lb_cidade = Label(self.aba1, text = "Cidade",bg='#dfe3ee',fg='#107db2')
        self.lb_cidade.place(relx= 0.5, rely=0.6)

        self.cidade_entry = Entry(self.aba1)
        self.cidade_entry.place(relx= 0.5, rely=0.7, relwidth=0.25, relheight=0.12)


        ### NÃO PRESENTE NO CURSO, ADICIONADO POR CONTA

        #  Criação da Label e entrada do Estado
        self.lb_estado = Label(self.aba1, text = "Estado",bg='#dfe3ee',fg='#107db2')
        self.lb_estado.place(relx= 0.795, rely=0.6)

        self.options = StringVar(root) #Opção selecionada pelo usuário será definida como self.options
        self.estados = ("AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO")
        self.estado_entry = ttk.Combobox(self.aba1,textvariable=self.options,values=self.estados)
        self.estado_entry.place(relx= 0.8, rely=0.7, relwidth=0.10, relheight=0.119)


        

        ### ATÉ AQUI
    # AULA 6 DAQUI EM DIANTE
    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height=3, columns=("col1","col2","col3","col4","col5","col6"))
        
        ### Definição do nome de cada uma das colunas criadas anteriormente na Treeview
        self.listaCli.heading("#0",text="")
        self.listaCli.heading("#1",text="Cód.")
        self.listaCli.heading("#2",text="Nome")
        self.listaCli.heading("#3",text="Telefone")
        self.listaCli.heading("#4",text="Cidade")
        self.listaCli.heading("#5",text="UF")
        self.listaCli.heading("#6",text="E-mail")

        ### Definição do tamanho de cada uma das colunas
        self.listaCli.column("#0",width=0,stretch=NO)
        self.listaCli.column("#1",width=40)
        self.listaCli.column("#2",width=160)
        self.listaCli.column("#3",width=160)
        self.listaCli.column("#4",width=125)
        self.listaCli.column("#5",width=50)
        self.listaCli.column("#6",width=250)

        ### Posicionando a lista no frame 2
        self.listaCli.place(relx=0.02,rely=0.05, relwidth=0.95,relheight=0.9)

        self.scrollLista = Scrollbar(self.frame_2, orient='vertical',command=self.listaCli.yview)
        self.listaCli.configure(yscrollcommand=self.scrollLista.set)
        self.scrollLista.place(relx=0.97, rely=0.05, relwidth=0.02, relheight=0.91)

        self.scrollLista2 = Scrollbar(self.frame_2, orient='horizontal',command=self.listaCli.xview)
        self.listaCli.configure(xscrollcommand=self.scrollLista2.set)
        self.scrollLista2.place(relx=0.02, rely=0.90, relwidth=0.95, relheight=0.06)

        self.listaCli.bind("<Double-1>",self.onDoubleClick)

    def Menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def Quit(): self.root.destroy()

        menubar.add_cascade(label = "Opções", menu= filemenu)
        menubar.add_cascade(label = "Relatórios", menu= filemenu2)

        filemenu.add_command(label="Sair", command= Quit)
        filemenu.add_command(label="Limpa Cliente", command=self.limpa_tela)
        filemenu2.add_command(label="Relatório PDF", command=self.gerarRelatCliente)

Application()