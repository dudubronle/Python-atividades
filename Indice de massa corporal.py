import customtkinter as ct
from tkinter import *

janela = ct.CTk()

class Application():

    def __init__(self):
        pass
        self.janela=janela
        self.tema()
        self.tela()
        self.sistemalogin()
        janela.mainloop()
    def tema(self):
        ct.set_appearance_mode('White')
        ct.set_default_color_theme('dark-blue')

    # Criação da tela de login
    def tela(self):
        janela.geometry('700x400')
        janela.title('Login')
        janela.iconbitmap('lobo.ico')
        janela.resizable(False, False)

    def sistemalogin(self):
        img = PhotoImage(file='login.png')
        label_img= ct.CTkLabel(master= janela, image= img, text=None)
        label_img.place(x=3, y=1)

        frame = ct.CTkFrame(master= janela, width= 300, height= 396)
        frame.pack(side='right')

        label = ct.CTkLabel(master=frame, text='', font=('Roboto-Condensed.ttf', 80))
        label.place(x=25, y=5)

        usuario_entry= ct.CTkEntry(master=frame, placeholder_text='Nome de usuário', width=250, font=('Roboto', 15)).place(x=25, y=78)
        usuario_entry = ct.CTkLabel(master=frame, text='Usuário:', text_color='white', font=('Roboto-Condensed.ttf', 20)).place(x=15, y=45)
        senha_entry2 = ct.CTkEntry(master=frame, placeholder_text='Digite sua senha', width=250,show='*', font=('Roboto', 15)).place(x=25, y=175)
        senha_entry2 = ct.CTkLabel(master=frame, text='Senha:', text_color='white', font=('Roboto-Condensed.ttf', 20)).place(x=15, y=130)

        checkbox = ct.CTkCheckBox(master=frame, text='Lembrar login').place(x=25, y=275)

        button_confimar = ct.CTkButton(master=frame, text='confirmar',fg_color='black', width=20, command='botao1').place(x=25, y=320)





        def tela_register():
            pass
            comfirmar = ct.CTkButton(master=frame, text='cadastrar',fg_color='black', width=150, command=tela_register).place(x=75, y=234)



Application()