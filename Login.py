from tkinter import *
from tkinter import messagebox
from datetime import datetime
import pwinput
import pyglet
pyglet.font.add_file("digital-7/digital-7.ttf")


janela = Tk()
janela.title("Login Python")
janela.geometry("600x300")
janela.configure(background="white")
janela.resizable(width=FALSE, height=FALSE)
janela.attributes("-alpha", 0.9)
janela.iconbitmap(default="img/l.ico")

logo = PhotoImage(file="img/people.png")

cor1 = "#3d3d3d"
cor2 = "#fafcff"
cor3 = "#21c25c"
cor4 = "#eb463b"
cor5 = "#dedcdc"
cor6 = "#3080f0"

fundo = cor1
cor = cor5

EsquerdaFrame = Frame(janela, width=200, height=300,
                      background="MIDNIGHTBLUE", relief="raise")
EsquerdaFrame.pack(side=LEFT)

DireitaFrame = Frame(janela, width=395, height=300,
                     background="MIDNIGHTBLUE", relief="raise")
DireitaFrame.pack(side=RIGHT)

LogoLabel = Label(EsquerdaFrame, image=logo, background="MIDNIGHTBLUE")
LogoLabel.place(x=30, y=80)


def Calculadora():

    BotaoSis.place(x=500, y=140)
    BotaoCal.place(x=500, y=140)
    titulo = Label(DireitaFrame, text="Calculadora", font=(
        "Century Gothic", 20), background="MIDNIGHTBLUE", fg="white")
    titulo.place(x=130, y=0)

    BotaoCal11 = Label(DireitaFrame, text="Digite o Valor [1]", font=(
        "Century Gothic", 10), background="MIDNIGHTBLUE", fg="white")
    BotaoCal11.place(x=100, y=50)
    BotaoCal1 = Entry(DireitaFrame, width=8)
    BotaoCal1.place(x=220, y=50)

    BotaoCal12 = Label(DireitaFrame, text="Digite o Valor [2]", font=(
        "Century Gothic", 10), background="MIDNIGHTBLUE", fg="white")
    BotaoCal12.place(x=100, y=100)
    BotaoCal2 = Entry(DireitaFrame, width=8)
    BotaoCal2.place(x=220, y=100)

    radio_valor = IntVar()
    radio_valor.set(1)

    rdio1 = Radiobutton(DireitaFrame, variable=radio_valor,
                        activebackground="Red", text='+', value=1, indicator=0, width=5)
    rdio2 = Radiobutton(DireitaFrame, variable=radio_valor,
                        activebackground="Red", text='-', value=2, indicator=0, width=5)
    rdio3 = Radiobutton(DireitaFrame, variable=radio_valor,
                        activebackground="Red", text='*', value=3, indicator=0, width=5)
    rdio4 = Radiobutton(DireitaFrame, variable=radio_valor,
                        activebackground="Red", text='/', value=4, indicator=0, width=5)

    rdio1.place(x=100, y=150)
    rdio2.place(x=150, y=150)
    rdio3.place(x=200, y=150)
    rdio4.place(x=250, y=150)

    def exibe():
        x1 = float(BotaoCal1.get())
        x2 = float(BotaoCal2.get())
        nome = str(radio_valor.get())
        v1 = x1
        v2 = x2
        if nome == '1':
            messagebox.showinfo('Resultado:', v1 + v2)
        if nome == '2':
            messagebox.showinfo('Resultado:', v1 - v2)
        if nome == '3':
            messagebox.showinfo('Resultado:', v1 * v2)
        if nome == '4':
            messagebox.showinfo('Resultado:', v1 / v2)

    botao = Button(DireitaFrame, text='Exibe', command=exibe, width=27)
    botao.place(x=100, y=180)


def loginn():

    BotaoSis.place(x=500, y=140)
    BotaoCal.place(x=500, y=140)
    Titulol = Label(DireitaFrame, text="Tela de Login", font=(
        "Century Gothic", 20), background="MIDNIGHTBLUE", fg="white")
    Titulol.place(x=105, y=5)

    UserLabel = Label(DireitaFrame, text="Login:", background="MIDNIGHTBLUE", font=(
        "Century Gothic", 20), fg="white")
    UserLabel.place(x=5, y=45)
    UserInput = Entry(DireitaFrame, width=30)
    UserInput.place(x=100, y=60)

    SenLabel = Label(DireitaFrame, text="Senha:", background="MIDNIGHTBLUE", font=(
        "Century Gothic", 20), fg="white")
    SenLabel.place(x=5, y=90)
    SenInput = Entry(DireitaFrame, width=30, show="*")
    SenInput.place(x=100, y=105)

    def get_line(word):
        with open('cadastro.txt') as f:
            for l_num, l in enumerate(f, 1):
                if word in l:
                    return l_num
            return False

    def consultar():
        Nom = str(UserInput.get())
        Sen = str(SenInput.get())
        nome = Nom
        senha = Sen

        str1 = get_line(nome+'.'+senha)
        if nome != '':
            if str1:
                messagebox.showinfo(title="Cadastro Py",
                                    message="Seja bem vindo "+nome)
            else:
                messagebox.showinfo(title="Cadastro Py",
                                    message="Usuario ou Senha Invalido!")
        else:
            messagebox.showinfo(title="Cadastro Py",
                                message="Usuario ou Senha vazio!")

    BotaoLogin = Button(DireitaFrame, text="Enviar",
                        width=10, command=consultar)
    BotaoLogin.place(x=205, y=140)

    def Cadastro():
        BotaoLogin.place(x=500)
        BotaoCadastro.place(x=500)
        UserLabel.place(x=500)
        UserInput.place(x=500)
        SenLabel.place(x=500)
        SenInput.place(x=500)
        Tituloc = Label(DireitaFrame, text="Tela de Cadastro", font=(
            "Century Gothic", 20), background="MIDNIGHTBLUE", fg="white")
        Tituloc.place(x=75, y=5)

        NomeLabel = Label(DireitaFrame, text="Nome:", font=(
            "Century Gothic", 20), background="MIDNIGHTBLUE", fg="white")
        NomeLabel.place(x=5, y=45)
        NomeInput = Entry(DireitaFrame, width=30)
        NomeInput.place(x=100, y=60)

        SenhaLabel = Label(DireitaFrame, text="Senha:", font=(
            "Century Gothic", 20), background="MIDNIGHTBLUE", fg="white")
        SenhaLabel.place(x=5, y=90)
        SenhaInput = Entry(DireitaFrame, width=30,  show="*")
        SenhaInput.place(x=100, y=105)

        def Register():
            Nome = str(NomeInput.get())
            Senha = str(SenhaInput.get())
            Linha_Entry_1 = Nome
            Linha_Entry_2 = Senha
            if ((Linha_Entry_1 == "") or (Linha_Entry_2 == "")):
                messagebox.showinfo(title="Cadastro Py",
                                    message="Usuario ou Senha Vazio!!!")
                Volt()
            else:
                with open("cadastro.txt", "a") as arquivo:
                    arquivo.write(Linha_Entry_1+"."+Linha_Entry_2+"\n")
                with open("cadastro.txt", "r") as arquivo:
                    arquivo.read()
                print("Cadastro Efetuado")
                messagebox.showinfo(
                    title="Cadastro Py", message="Usuario "+Linha_Entry_1+" Cadastrado!")
                Volt()
        BotaoCad = Button(DireitaFrame, text="Cadastrar",
                          width=10, command=Register)
        BotaoCad.place(x=150, y=140)

        def Volt():
            BotaoLogin.place(x=205, y=140)
            BotaoCadastro.place(x=100, y=140)
            UserLabel.place(x=5, y=45)
            UserInput.place(x=100, y=60)
            SenLabel.place(x=5, y=90)
            SenInput.place(x=100, y=105)
            BotaoCad.place(x=550, y=140)

            voltar.place(x=550, y=170)
            Tituloc.place(x=575, y=5)
            NomeLabel.place(x=500, y=45)
            NomeInput.place(x=500, y=60)
            SenhaLabel.place(x=500, y=90)
            SenhaInput.place(x=500, y=105)

        voltar = Button(DireitaFrame, text="Voltar", width=10, command=Volt)
        voltar.place(x=150, y=170)

    BotaoCadastro = Button(DireitaFrame, text="Cadastrar",
                           width=10, command=Cadastro)
    BotaoCadastro.place(x=100, y=140)


BotaoSis = Button(DireitaFrame, font=(
    "20"), text="SISTEMA", width=20, command=loginn)
BotaoSis.place(x=5, y=140)

BotaoCal = Button(DireitaFrame, font=(
    "20"), text="CALCULADORA", width=20, command=Calculadora)
BotaoCal.place(x=200, y=140)


def relogio():
    tempo = datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    l1.config(text=hora)
    l1.after(200, relogio)


l1 = Label(DireitaFrame, text="  ", font=("digital-7 30"),
           background="MIDNIGHTBLUE", fg="white")
l1.place(x=270, y=250)
relogio()


janela.mainloop()
