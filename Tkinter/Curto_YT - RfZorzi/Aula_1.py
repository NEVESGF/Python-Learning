from tkinter import *

root = Tk() 

class Application(): 
    
    # https://docs.python.org/3/tutorial/classes.html
    # https://www.hackerearth.com/practice/python/object-oriented-programming/classes-and-objects-i/tutorial/
    
    def __init__(self):
        self.root = root
        self.tela()
        root.mainloop() #Informação básica necessária para se abrir uma janela no Tkinter
    
    def tela(self):
        self.root.title("Cadastro de Clientes") #title = titulo da janela que será aberta
        self.root.configure(background= "#1e3843") #configure background define a cor de fundo da janela (utilziar hexadecimal para cores mais agradáveis)
        self.root.geometry("700x500") #define o tamanho de inicio da janela horizontal x vertical
        self.root.resizable(True, True) #habilita se a tela vai ser responsiva quanto a modificação de tamanho true (horizontal), true (vertical)
        self.root.maxsize(width= 900, height= 700) #define o tamanho máximo que a janela pode adquirir
        self.root.minsize(width=400,height=300) #define o tamanho mínimo que a janela pode adquirir

Application()