"""Sistema de Controle de Notas
Programador: Jardel da Rocha Pereira Silva
Data: 06/08/2019

Este software será feito em PYTHON 3.4 e controlará um pequeno BD SQLITE3
Biblioteca: Tkinter, SQLite3 e Ttk
Metodologia: Programação Imperativa/estrutura com uso de classes Nativas
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import os
os.system('cls');



def mostra(t, op, texto):# O 't' é o objeto Treeview passado como parametro
                #OP é a variavel que irá ativar a filtragem
                # 0 = Mostrar tudo
                # 1 = Filtrar dados a partir do parametro 'texto'
                # texto = texto base de filtro do BD
               
    conecta = sqlite3.connect('emp.db')
    cursor = conecta.cursor()
    if op==0:
        vsql = 'SELECT * FROM EMPRESA'
    elif op==1:
        vsql = 'SELECT * FROM EMPRESA WHERE NOME LIKE "%{}%"'.format(texto)
    cursor.execute(vsql)
    linhas = cursor.fetchall()
    for i in t.get_children():
        t.delete(i)
    for linha in linhas:
        t.insert('',END, values=linha)
    conecta.close()

def sair(janela):
    if messagebox.askyesno("Sair","Deseja sair da aplicação ?"):
        janela.destroy()

def Empresa():
    #chamada da função criaDB
    #Construindo a tela
    janela = Tk()
    janela.geometry('940x380')
    janela.title('Sistema de Cadastramento de Empresas')
    janela.resizable()
    janela.configure(bg='#4169e1')
    janela.protocol("WM_DELETE_WINDOW", lambda: sair(janela))

    #corpo do formulario
    frame_meio = Frame(janela)
    frame_meio.pack()
    tabela = ttk.Treeview(frame_meio, columns = (1,2,3,4,5,6,7,8,9),
                          show = 'headings', selectmode='browse',
                          displaycolumns='#all')
    tabela.pack(side='left')

    #definindo os titulos dos cabeçalhos
    tabela.heading(1, text='ID')
    tabela.heading(2, text='NOME')
    tabela.heading(3, text='CNPJ')
    tabela.heading(4, text='ENDEREÇO')
    tabela.heading(5, text='E-MAIL')
    tabela.heading(6, text='TELEFONE')
    tabela.heading(7, text='QUANT.FUNC.')
    tabela.heading(8, text='HORA.FUNC.')
    tabela.heading(9, text='REMUN.')

    #definindo o tamanho dos cabeçalhos
    tabela.column(1, width=50)
    tabela.column(2, width=170)
    tabela.column(3, width=95)
    tabela.column(4, width=150)
    tabela.column(5, width=70)
    tabela.column(6, width=85)
    tabela.column(7, width=85)
    tabela.column(8, width=90)
    tabela.column(9, width=90)

    #inserindo a barra de rolagem
    b_rolagem = ttk.Scrollbar(frame_meio, orient='vertical', command=tabela.yview)
    b_rolagem.pack(side='right',fill='y')
    tabela.configure(yscrollcommand=b_rolagem.set)
    

    #exibindo os dados no treeview
    mostra(tabela,0,'')

    
    janela.mainloop()

programa = Empresa()
    
