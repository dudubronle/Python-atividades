from tkinter import *
import customtkinter as tk

janela = tk.CTk()
janela.geometry('500x300')
janela.title("Pergunta de sexo")
janela.resizable(False, False)

def verifica_sexo():
    if sexo.get() == 'Feminino':
        print('Ola moça')
    elif sexo.get() == 'Masculino':
        print('ola Moço')
    else:
        print('Sexo inválido')

sexo = tk.StringVar()

Label(janela, text='Qual é o seu sexo?', width=50).pack()
Entry(janela, textvariable=sexo, width=50).place(x=100, y=100)
Button(janela, text='Confirmar', command=verifica_sexo).place(x=100, y=70)



janela.mainloop()