"""Sistema de Cadastramento de Estagiários
Programador: Jardel da Rocha Pereira Silva
Data: 17/10/2019

Este software será feito em PYTHON 3.4 e controlará um BD SQLITE3
Bibliotecas: Tkinter, SQLite3 e Ttk
Metodologia: Programação baseada em PRINCE2
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import os

os.system('cls')
def sair(janela):
    if messagebox.askyesno("Sair","Deseja sair da aplicação ?"):
        janela.destroy()


def telaemp1(janela):
    from Telaemp1 import Emps

def telaest1(janela):
    from Telaest1 import Ests
    
#Código principal do programa
        
def Main():
    #chamada da função criaDB
    
    #Construindo a tela
    janela = Tk()
    janela.geometry('940x580')
    janela.title('Sistema Cadastramento de Estágiarios 1.0')
    janela.resizable(0,0)
    janela.configure(bg='#4169E1')

    #definção e posicionamento dos widgets

    #BARRA DE FERRAMENTAS
    #==========================
    barraferramentas = Frame(janela)
    barraferramentas.pack()

    
    #cabeçalho
    frame_topo = Frame(janela)
    frame_topo.pack()
    frame_topo.configure(bg='#4169E1')
    t_titulo = Label(frame_topo, text='SISTEMA DE CADASTRAMENTO DE ESTAGIÁRIOS', font=('Century Gothic',16))
    t_titulo.grid(row=0, column=0)
    t_titulo.pack(pady=20)
    t_titulo.configure(bg='#4169E1', fg='white')
    
    

    #frame buttons
    frame_meio = Frame(janela)
    frame_meio.pack()
    
    #imagem de logo do programa
    imagem = PhotoImage(file="IMAGENS/logo_est.png")
    w = Label(frame_meio, image=imagem)
    w.imagem = imagem
    w.config(image=imagem, width=250, height=100)
    w.grid(row=0, column=0)
    w.configure(bg='#4169E1')
    t_titulo.pack(pady=40)
    
    
    #frame 2
    frame_2 = Frame(janela)
    frame_2.pack()
    frame_2.configure(bg='#4169E1')


    
    #botoes de acesso as outras telas
    btn_ent = Button(frame_2, text='ESTAGIARIOS',command=lambda:telaest1(janela),bg='white')
    img_ent = PhotoImage(file='IMAGENS/btn_ent.png')
    btn_ent.config(image=img_ent, width=200, height=100)
    btn_ent.grid(row=0, column=0,pady=90, padx=10)

    btn_emp = Button(frame_2, text='EMPRESA',command=lambda:telaemp1(janela),bg='white')
    img_emp = PhotoImage(file='IMAGENS/btn_emp.png')
    btn_emp.config(image=img_emp, width=200, height=100)
    btn_emp.grid(row=0, column=1,padx=10)
    
    btn_sai = Button(frame_2, text='SAIR',command=lambda:sair(janela),bg='white')
    img_sai = PhotoImage(file='IMAGENS/btn_sai.png')
    btn_sai.config(image=img_sai, width=200, height=100)
    btn_sai.grid(row=0, column=2,padx=10)
    
   
    
    #loop principal
    janela.mainloop()
    

programa = Main()
