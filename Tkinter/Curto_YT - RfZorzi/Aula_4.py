from tkinter import *

root = Tk()

class Application(): 
    
    # https://docs.python.org/3/tutorial/classes.html
    # https://www.hackerearth.com/practice/python/object-oriented-programming/classes-and-objects-i/tutorial/
    
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
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
        self.bt_limpar = Button(self.frame_1, text = "Limpar")
        self.bt_limpar.place(relx = 0.2 , rely= 0.1, relwidth=0.1, relheight=0.15)

        ### Criação do botão buscar
        self.bt_buscar = Button(self.frame_1, text = "Buscar")
        self.bt_buscar.place(relx = 0.3 , rely= 0.1, relwidth=0.1, relheight=0.15)

        ### Criação do botão novo
        self.bt_novo = Button(self.frame_1, text = "Novo")
        self.bt_novo.place(relx = 0.6 , rely= 0.1, relwidth=0.1, relheight=0.15)

        ### Criação do botão alternar
        self.bt_alternar = Button(self.frame_1, text = "Alternar")
        self.bt_alternar.place(relx = 0.7 , rely= 0.1, relwidth=0.1, relheight=0.15)

        ### Criação do botão apagar
        self.bt_apagar = Button(self.frame_1, text = "Apagar")
        self.bt_apagar.place(relx = 0.8 , rely= 0.1, relwidth=0.1, relheight=0.15)


        # AULA 4 DAQUI EM DIANTE

        #  Criação da Label e entrada do código
        self.lb_codigo = Label(self.frame_1, text = "Código")
        self.lb_codigo.place(relx= 0.05, rely=0.05)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx= 0.05, rely=0.15, relwidth=0.08)

        #  Criação da Label e entrada do nome
        self.lb_nome = Label(self.frame_1, text = "Nome")
        self.lb_nome.place(relx= 0.05, rely=0.35)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx= 0.05, rely=0.45, relwidth=0.80, relheight=0.12)

        #  Criação da Label e entrada do telefone
        self.lb_telefone = Label(self.frame_1, text = "Telefone")
        self.lb_telefone.place(relx= 0.05, rely=0.60)

        self.nome_telefone = Entry(self.frame_1)
        self.nome_telefone.place(relx= 0.05, rely=0.70, relwidth=0.4, relheight=0.12)

        #  Criação da Label e entrada do cidade
        self.lb_nome = Label(self.frame_1, text = "Cidade")
        self.lb_nome.place(relx= 0.5, rely=0.6)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx= 0.5, rely=0.7, relwidth=0.2, relheight=0.12)

        #  Criação da Label e entrada do Estado
        self.lb_nome = Label(self.frame_1, text = "Estado")
        self.lb_nome.place(relx= 0.75, rely=0.6)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx= 0.75, rely=0.7, relwidth=0.1, relheight=0.12)

Application()