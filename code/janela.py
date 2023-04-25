from tkinter import *
from tkinter import ttk
from create import criar_user
from read import listar_usuarios, procurar_usuario
from update import up_usuario
from delete import del_usuario
import pyautogui

pyautogui.PAUSE = 2
janela = Tk()
usuarios = []
idades = []


class Aplicacao:
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames()
        self.botoes()
        self.labels()
        self.inputs()
        self.lista_frame2()
        self.select_list()
        self.inpIDUsuario.focus_set()

        janela.mainloop()

    def tela(self):
        self.janela.title('Seaflix')
        self.janela.geometry('700x800')
        self.janela.iconbitmap('sea.ico')
        self.janela.configure(background='#0591af')
        self.janela.resizable(True, True)
        self.janela.maxsize(width=700, height=800)

    def frames(self):
        self.frame_0 = Frame(self.janela, bg='#ceebf2', highlightthickness=1, highlightbackground='#011013')
        self.frame_0.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.07)

        self.frame_1 = Frame(self.janela, bg='#ceebf2', highlightthickness=1, highlightbackground='#011013')
        self.frame_1.place(relx=0.03, rely=0.125, relwidth=0.94, relheight=0.15)

        self.frame_2 = Frame(self.janela, bg='#ceebf2', highlightthickness=1, highlightbackground='#011013')
        self.frame_2.place(relx=0.03, rely=0.3, relwidth=0.94, relheight=0.24)

    def botoes(self):
        self.btBuscar = Button(self.frame_0, text='Buscar', fg='#fff', bg='#011013', relief='flat', command=self.select_user)
        self.btBuscar.place(relx=0.15, rely=0.25, relwidth=0.1, relheight=0.5)

        self.btLimpar = Button(self.frame_0, text='Limpar', fg='#fff', bg='#011013', relief='flat', command=self.limpa_tela)
        self.btLimpar.place(relx=0.28, rely=0.25, relwidth=0.1, relheight=0.5)

        self.btCreate = Button(self.frame_0, text='Criar', fg='#fff', bg='#011013', relief='flat', command=self.insert_user)
        self.btCreate.place(relx=0.45, rely=0.25, relwidth=0.1, relheight=0.5)

        self.btRead = Button(self.frame_0, text='Listar', fg='#fff', bg='#011013', relief='flat', command=self.select_list)
        self.btRead.place(relx=0.57, rely=0.25, relwidth=0.1, relheight=0.5)

        self.btUpdate = Button(self.frame_0, text='Atualizar', fg='#fff', bg='#011013', relief='flat', command=self.update_user)
        self.btUpdate.place(relx=0.70, rely=0.25, relwidth=0.1, relheight=0.5)

        self.btDelete = Button(self.frame_0, text='Deletar', fg='#fff', bg='#011013', relief='flat', command=self.delete_user)
        self.btDelete.place(relx=0.82, rely=0.25, relwidth=0.1, relheight=0.5)

        self.btDimensao = Button(self.janela, text='Tela', fg='#fff', bg='#011013', command=self.monitor)
        self.btDimensao.place(relx=0.05, rely=0.6, relwidth=0.15, relheight=0.1)

        self.btPosicao = Button(self.janela, text='Posicao', fg='#fff', bg='#011013', command=self.posicao)
        self.btPosicao.place(relx=0.20, rely=0.6, relwidth=0.15, relheight=0.1)

        self.btMover = Button(self.janela, text='Mover', fg='#fff', bg='#011013', command=self.move_mouse)
        self.btMover.place(relx=0.35, rely=0.6, relwidth=0.15, relheight=0.1)

        self.btBot = Button(self.janela, text='Bot', fg='#fff', bg='#011013', command=self.bot)
        self.btBot.place(relx=0.50, rely=0.6, relwidth=0.15, relheight=0.1)

        self.btAlerta = Button(self.janela, text='Alerta', fg='#fff', bg='#011013', command=self.alerta)
        self.btAlerta.place(relx=0.65, rely=0.6, relwidth=0.15, relheight=0.1)

        self.btCaptura = Button(self.janela, text='Captura', fg='#fff', bg='#011013', command=self.delete_user)
        self.btCaptura.place(relx=0.80, rely=0.6, relwidth=0.15, relheight=0.1)

    def labels(self):
        self.lbIDUsuario = Label(self.frame_0, text='ID', bg='#ceebf2')
        self.lbIDUsuario.place(relx=0.005, rely=0.01, relwidth=0.1, relheight=0.25)

        self.lbIDNome = Label(self.frame_1, text='Nome:', bg='#ceebf2')
        self.lbIDNome.place(relx=0.005, rely=0.08, relwidth=0.1, relheight=0.22)

        self.lbIDEmail = Label(self.frame_1, text='E-Mail:', bg='#ceebf2')
        self.lbIDEmail.place(relx=0.005, rely=0.36, relwidth=0.1, relheight=0.22)

        self.lbIDPlano = Label(self.frame_1, text='Plano:', bg='#ceebf2')
        self.lbIDPlano.place(relx=0.005, rely=0.64, relwidth=0.1, relheight=0.22)

        self.lbIDTipo = Label(self.frame_1, text='Tipo:', bg='#ceebf2')
        self.lbIDTipo.place(relx=0.35, rely=0.64, relwidth=0.1, relheight=0.22)

        self.lbIDIdade = Label(self.frame_1, text='Idade:', bg='#ceebf2')
        self.lbIDIdade.place(relx=0.675, rely=0.64, relwidth=0.1, relheight=0.22)

    def inputs(self):
        self.inpIDUsuario = Entry(self.frame_0)
        self.inpIDUsuario.place(relx=0.005, rely=0.45, relwidth=0.1, relheight=0.5)

        self.inpNome = Entry(self.frame_1)
        self.inpNome.place(relx=0.12, rely=0.08, relwidth=0.8, relheight=0.22)

        self.inpEmail = Entry(self.frame_1)
        self.inpEmail.place(relx=0.12, rely=0.36, relwidth=0.8, relheight=0.22)

        self.inpPlano = Entry(self.frame_1)
        self.inpPlano.place(relx=0.12, rely=0.64, relwidth=0.2, relheight=0.22)

        self.inpTipo = Entry(self.frame_1)
        self.inpTipo.place(relx=0.44, rely=0.64, relwidth=0.2, relheight=0.22)

        self.inpIdade = Entry(self.frame_1)
        self.inpIdade.place(relx=0.77, rely=0.64, relwidth=0.15, relheight=0.22)

    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height=3, columns=('col1',
                                                                      'col2',
                                                                      'col3',
                                                                      'col4',
                                                                      'col5',
                                                                      'col6'))
        self.listaCli.heading('#0', text='')
        self.listaCli.heading('#1', text='ID')
        self.listaCli.heading('#2', text='Nome')
        self.listaCli.heading('#3', text='E-Mail')
        self.listaCli.heading('#4', text='Plano')
        self.listaCli.heading('#5', text='Tipo')
        self.listaCli.heading('#6', text='Idade')

        self.listaCli.column('#0', width=0)
        self.listaCli.column('#1', width=15)
        self.listaCli.column('#2', width=170)
        self.listaCli.column('#3', width=213)
        self.listaCli.column('#4', width=65)
        self.listaCli.column('#5', width=65)
        self.listaCli.column('#6', width=50)

        self.listaCli.place(relx=0.025, rely=0.05, relwidth=0.95, relheight=0.90)

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscrollcommand=self.scroolLista.set)
        self.scroolLista.place(relx=0.9745, rely=0.05, relwidth=0.02, relheight=0.90)

    def select_list(self):
        self.listaCli.delete(*self.listaCli.get_children())
        for i in listar_usuarios():
            self.listaCli.insert(parent='', index=0, values=i)
            usuarios.append(i[1])
            idades.append(i[5])

    def insert_user(self):
        criar_user(self.inpNome.get().title(),
                   self.inpIdade.get(),
                   self.inpEmail.get(),
                   self.inpPlano.get().title(),
                   self.inpTipo.get().title())

        self.limpa_tela()
        self.select_list()

    def delete_user(self):
        del_usuario(self.inpIDUsuario.get())
        self.limpa_tela()
        self.select_list()

    def limpa_tela(self):
        self.inpIDUsuario.delete(0, END)
        self.inpNome.delete(0, END)
        self.inpEmail.delete(0, END)
        self.inpIdade.delete(0, END)
        self.inpPlano.delete(0, END)
        self.inpTipo.delete(0, END)
        self.listaCli.delete(*self.listaCli.get_children())

    def update_user(self):
        if self.inpNome.get():
            self.inpIDUsuario.update()
            self.inpNome.update()
            self.inpEmail.update()
            self.inpPlano.update()
            self.inpTipo.update()
            self.inpIdade.update()
            up_usuario(self.inpIDUsuario.get(), self.inpNome.get(), self.inpEmail.get(), self.inpPlano.get(),
                       self.inpTipo.get(), self.inpIdade.get())
            self.limpa_tela()
            self.select_list()
        else:
            self.status = 'Os campos não podem estar vazios.'

    def select_user(self):
        self.listaCli.delete(*self.listaCli.get_children())
        usuario = procurar_usuario(self.inpIDUsuario.get())
        self.listaCli.insert(parent='', index=0, values=usuario[0])
        self.inpNome.insert(0, usuario[0][1])
        self.inpEmail.insert(0, usuario[0][2])
        self.inpPlano.insert(0, usuario[0][3])
        self.inpTipo.insert(0, usuario[0][4])
        self.inpIdade.insert(0, usuario[0][5])

    def monitor(self):
        x, y = pyautogui.size()
        print(x)
        print(y)

    def posicao(self):
        x, y = pyautogui.position()
        print(x)
        print(y)

    def move_mouse(self):
        pyautogui.moveTo(100, 150)

    def bot(self):
        pyautogui.press("Win")
        pyautogui.write("Bloco")
        pyautogui.press("Enter")
        pyautogui.write("Meus amigos")
        pyautogui.hotkey('ctrl', 's')
        pyautogui.write("Cafe")
        # for i in range(10):
        #     pyautogui.press('tab')
        # pyautogui.press('up')
        pyautogui.press('enter')
        pyautogui.hotkey('alt', 't')
        pyautogui.hotkey('win', 'd')

    def alerta(self):
        print(pyautogui.confirm(text="Teste", title="Caixa de Texto", buttons=["Ok", "Cancel"]))

    def captura(self):
        img = pyautogui.screenshot("Minha Captura")
        print(img)