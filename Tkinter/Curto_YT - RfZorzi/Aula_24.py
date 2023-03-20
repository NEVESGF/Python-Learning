from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import base64

from time import sleep
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics   
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser
import datetime

root1 = Tk()
class GradienteFrame(Canvas):
    def __init__(self,parent,color1 = "#C6CCFF", color2="gray35", **kwargs)
        Canvas.__init__(self,parent,**kwargs)
        self._color1 = color1
        self._color2 = color2
        self.bind("<Configure>",self._draw_gradient)



class Relatorios():
    def printCliente(self):
        webbrowser.open("cliente.pdf")
    def gerarRelatCliente(self):
        self.c = canvas.Canvas("cliente.pdf")

        self.codigoRel = self.codigo_entry.get()
        self.nomeRel = self.nome_entry.get()
        self.emailRel = self.email_entry.get()
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
        self.c.drawString(50,640,'E-mail: ')
        self.c.drawString(50,600,'Telefone: ')
        self.c.drawString(50,570,'Cidade: ')
        self.c.drawString(50,540,'Estado: ')

        self.c.setFont("Helvetica",16)
        self.c.drawString(150,700, self.codigoRel)
        self.c.drawString(150,670, self.nomeRel)
        self.c.drawString(150,640, self.emailRel)
        self.c.drawString(150,600, self.telefoneRel)
        self.c.drawString(150,570, self.cidadeRel)
        self.c.drawString(150,540, self.estadoRel)

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

        if self.nome_entry.get() == '':
            msg = "Para cadastrar novo cliente é necessário que seja digistrado pelo menos um nome !"
            messagebox.showwarning("Cadastro de Clientes - Aviso!!!",msg)
        else:
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
        
        self.root1 = root1
        self.tela_login()
        self.widgets_login()
        
        root1.mainloop() #Informação básica necessária para se abrir uma janela no Tkinter 

    def tela_login(self):
        self.root1.title("Login")
        self.root1.configure(background= "#1e3843") #configure background define a cor de fundo da janela (utilziar hexadecimal para cores mais agradáveis)
        self.root1.geometry("300x380") #define o tamanho de inicio da janela horizontal x vertical
        self.root1.resizable(False, False) #habilita se a tela vai ser responsiva quanto a modificação de tamanho true (horizontal), true (vertical)
        self.status = Label(self.root1,text='Digite o Usuário e Senha',bg="#1e3843",fg='white')
        self.status.place(relx=0.259,rely=0.67)

    def login_try(self):
        global username
        self.senha = self.senha_entry.get()
        username = self.usuario_entry.get()
        senhakey = ["12345"]
        if self.senha == senhakey[0] and username != "":
            self.status.destroy()
            self.status = Label(self.root1,text='Digite o Usuário e Senha',bg="#1e3843",fg='white')
            self.status.place(relx=0.259,rely=0.67)
            self.senha_entry.delete(0,END)
            self.root1.withdraw()
            self.telaprincipal()
            return True
        elif username == "":
            messagebox.showerror('Atenção','Usuário e Senha são obrigatórios para continuar !')
        elif self.senha != senhakey[0]:
            self.status.destroy()
            self.status = Label(self.root1,text='Senha Incorreta!',bg="#1e3843",fg='red')
            self.status.place(relx=0.359,rely=0.67)
            self.senha_entry.delete(0,END)
            return False
        

    def telaprincipal(self):
            global root
            root = Toplevel(root1)
            self.root = root         
            self.tela()
            self.frames_da_tela()
            self.widgets_frame1()
            self.lista_frame2()
            self.montaTabelas()
            self.select_lista()
            self.Menus()

    def widgets_login(self):
            self.userpic = PhotoImage(data=base64.b64decode('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'))

            self.userpic = self.userpic.subsample(3,3)
            self.bt_userpic = Button(root1,image=self.userpic,border=0,background= "#1e3843",highlightbackground="#1e3843",activebackground="#1e3843",command=self.login_try)
            
            self.bt_userpic.place(relx=0.23,rely=0.035)

            #Labels
            Label(root1,text="Usuário:",bg="#1e3843",fg='white').place(relx=0.17,rely=0.75,width=60,relheight=0.09)
            Label(root1,text="Senha  :",bg="#1e3843",fg='white').place(relx=0.17,rely=0.88,width=60,relheight=0.09) 
            #self.usuario_entry
            #Entries
            
            self.usuario_entry = Entry(root1)
            self.usuario_entry.place(relx=0.42,rely=0.75, relwidth=0.4, relheight=0.09)
            self.senha_entry = Entry(root1,show="*")
            self.senha_entry.place(relx=0.42,rely=0.88, relwidth=0.4, relheight=0.09)
            self.senha_entry.bind('<Return>', lambda event: self.login_try())
            self.usuario_entry.bind('<Return>', lambda event: self.login_try())


    def tela(self):
        self.root.title("Cadastro de Clientes") #title = titulo da janela que será aberta
        self.root.configure(background= "#1e3843") #configure background define a cor de fundo da janela (utilziar hexadecimal para cores mais agradáveis)
        self.root.geometry("700x500") #define o tamanho de inicio da janela horizontal x vertical
        self.root.resizable(True, True) #habilita se a tela vai ser responsiva quanto a modificação de tamanho true (horizontal), true (vertical)
        self.root.maxsize(width= 900, height= 700) #define o tamanho máximo que a janela pode adquirir
        self.root.minsize(width=500,height=400) #define o tamanho mínimo que a janela pode adquirir
        
        self.root.wm_protocol("WM_DELETE_WINDOW", lambda: self.root1.destroy())
        
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
        self.abas.add(self.aba2, text = "Complemento")

        self.abas.place(relx=0, rely=0,relwidth=0.98, relheight=0.98)

        #self.canvas_bt = Canvas(self.frame_1, bd=0, bg='black', highlightbackground='gray',highlightthickness=3)
        #self.canvas_bt.place(relx=0.19,rely=0.08,relwidth=0.22,relheight=0.19)

        ### Criação do botão limpar
        Label(root,text= "Connected user: " + username,bg="#1e3843", font=("Arial", 10)).place(relx=0.02,rely=0.96)

        self.bt_limpar = Button(self.aba1, text = "Limpar\n (F2)",bd=2,bg='#107bd2',fg='white',
                                font=('verdana',8,'bold'),command=self.limpa_tela,)
        self.bt_limpar.place(relx = 0.2 , rely= 0.1, relwidth=0.1, relheight=0.16)
        
        ### Criação do botão buscar
        self.bt_buscar = Button(self.aba1, text = "Buscar\n (F3)",bd=2,bg='#107bd2',fg='white',
                                font=('verdana',8,'bold'),command=self.busca_cliente)
        self.bt_buscar.place(relx = 0.3 , rely= 0.1, relwidth=0.1, relheight=0.16)

        ### Criação do botão novo
        self.bt_novo = Button(self.aba1, text = "Novo\n (F4)",bd=2,bg='#107bd2',fg='white',
                              font=('verdana',8,'bold'),command=self.add_cliente)
        self.bt_novo.place(relx = 0.6 , rely= 0.1, relwidth=0.1, relheight=0.16)
        

        ### Criação do botão alternar
        self.bt_alternar = Button(self.aba1, text = "Alterar\n (F5)",bd=2,bg='#107bd2',fg='white',
                                  font=('verdana',8,'bold'),command=self.alterar_clientes)
        self.bt_alternar.place(relx = 0.7 , rely= 0.1, relwidth=0.1, relheight=0.16)

        ### Criação do botão apagar
        self.bt_apagar = Button(self.aba1, text = "Apagar\n (Del)",bd=2,bg='#107bd2',fg='white',
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


        self.root.bind("<F2>", lambda event: self.limpa_tela())
        self.root.bind("<F4>",lambda event: self.add_cliente())
        self.root.bind("<F3>",lambda event: self.busca_cliente())
        self.root.bind("<F5>",lambda event: self.alterar_clientes())
        self.root.bind("<Delete>",lambda event:self.deleta_cliente())
        self.root.bind("<F12>",lambda event: self.gerarRelatCliente())
        self.root.bind("<Escape>",lambda event: self.root1.destroy() if messagebox.askquestion("Encerrar", "Deseja realmente encerrar o programa?") == "yes" else "")

        ### NÃO PRESENTE NO CURSO, ADICIONADO POR CONTA

        #  Criação da Label e entrada do Estado
        self.lb_estado = Label(self.aba1, text = "Estado",bg='#dfe3ee',fg='#107db2')
        self.lb_estado.place(relx= 0.795, rely=0.6)

        self.options = StringVar(root) #Opção selecionada pelo usuário será definida como self.options
        self.estados = ("AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO")
        self.estado_entry = ttk.Combobox(self.aba1,textvariable=self.options,values=self.estados)
        self.estado_entry.place(relx= 0.8, rely=0.7, relwidth=0.10, relheight=0.119)


        ### drop down button

        self.Tipvar = StringVar()
        self.TipV = ("Solteiro(a)","Casado(a)","Divorciado(a)","Viúvo(a)")
        self.Tipvar.set("Solteiro(a)")
        self.popupMenu = OptionMenu(self.aba2,self.Tipvar, *self.TipV)
        self.popupMenu.place(relx=0.1,rely=0.1,relwidth=0.2, relheight=0.2)

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

        def Quit(): self.root.destroy();root1.deiconify()

        menubar.add_cascade(label = "Opções", menu= filemenu)
        menubar.add_cascade(label = "Relatórios", menu= filemenu2)

        filemenu.add_command(label="Sair", command= Quit)
        filemenu.add_command(label="Limpa Cliente", command=self.limpa_tela)
        filemenu2.add_command(label="Relatório PDF (F12)", command=self.gerarRelatCliente)
    
Application()
