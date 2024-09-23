
"""Sistema de Controle de Notas
Programador: Jardel da Rocha Pereira Silva
Data: 06/08/2019

Este software será feito em PYTHON 3.4 e controlará um pequeno BD SQLITE3
Biblioteca: Tkinter, SQLite3 e Ttk
Metodologia: Programação Imperativa/estrutura com uso de classes Nativas
"""

"""Tela da Empresa"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import os
os.system('cls');

#Criando a tabela do banco de dados

def criaDB():
    conecta = sqlite3.connect('emp.db')
    cursor = conecta.cursor()
    sqldb = '''
    CREATE TABLE IF NOT EXISTS EMPRESA(
    ID_EMP INTEGER PRIMARY KEY AUTOINCREMENT,
    NOME TEXT NOT NULL,
    CNPJ INTEGER,
    ENDERECO TEXT,
    EMAIL TEXT,
    TELEFONE INTEGER,
    QUANTFUN INTEGER,
    HORAFUN TEXT,
    REMUN FLOAT);
    '''
    cursor.execute(sqldb)
    conecta.commit()
    conecta.close()

#Código para exibição no Treeview

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

#Código de inserção/alteração dos dados na tabela ALUNOS
def teladados(op,vj,vt): #op = 0(inserção) e 1(alteração), vj(janela), vt(tabela)
    jan = Toplevel()
    jan.geometry('695x180+180+180')

    if op ==0:
        jan.title('INSERINDO DADOS')
    elif op==1:
        jan.title('ALTERANDO DADOS')
    jan.transient(vj)
    jan.focus_force()
    jan.grab_set()
    jan.configure(bg='#4169e1')
    
    #frame
    frame_form = Frame(jan)
    frame_form.place(x=15,y=15)
    frame_form.configure(bg='#4169e1')
    
    #campo nome
    t_nome = Label(frame_form, text='Nome: ', font=('Century Gothic', 10))
    t_nome.grid(row=0, column=0)
    t_nome.configure(bg='#4169e1', fg='white')

    edt_nome = Entry(frame_form, width=65)
    edt_nome.grid(row=0, column=3)

    #frame
    frame2_form = Frame(jan)
    frame2_form.place(x=465,y=15)
    frame2_form .focus_set()
    frame2_form.configure(bg='#4169e1')
    #campo 3
    t_cnpj = Label(frame2_form, text='CNPJ: ', font=('Century Gothic', 10))
    t_cnpj.grid(row=3, column=0)
    t_cnpj.configure(bg='#4169e1', fg='white')
    edt_cnpj = Entry(frame2_form, width=25)
    edt_cnpj.grid(row=3, column=3)


    
    #frame
    frame3_form = Frame(jan)
    frame3_form.place(x=15,y=45)
    frame3_form.configure(bg='#4169e1')
    
    #campo 2
    t_endereco = Label(frame3_form, text='Endereço: ', font=('Century Gothic', 10))
    t_endereco.grid(row=2, column=0)
    t_endereco.configure(bg='#4169e1', fg='white')
    edt_endereco = Entry(frame3_form, width=96)
    edt_endereco.grid(row=2, column=3)
    
    #frame
    frame4_form = Frame(jan)
    frame4_form.place(x=15,y=75)
    frame4_form.configure(bg='#4169e1')
    
    #campo 3
    t_email = Label(frame4_form, text='E-mail: ', font=('Century Gothic', 10))
    t_email.grid(row=3, column=0)
    t_email.configure(bg='#4169e1', fg='white')
    edt_email = Entry(frame4_form, width=65)
    edt_email.grid(row=3, column=3)

    #frame
    frame5_form = Frame(jan)
    frame5_form.place(x=466,y=75)
    frame5_form.configure(bg='#4169e1')
    
    #campo 1
    t_telefone = Label(frame5_form, text='Telefone: ', font=('Century Gothic', 10))
    t_telefone.grid(row=1, column=0)
    t_telefone.configure(bg='#4169e1', fg='white')
    edt_telefone = Entry(frame5_form, width=22)
    edt_telefone.grid(row=1, column=3)

    #frame
    frame6_form = Frame(jan)
    frame6_form.place(x=15,y=105)
    frame6_form.configure(bg='#4169e1')
    
    #campo 1
    t_horario = Label(frame6_form, text='Horário Func: ', font=('Century Gothic', 10))
    t_horario.grid(row=1, column=0)
    edt_horario = Entry(frame6_form, width=20)
    edt_horario.grid(row=1, column=3)
    t_horario.configure(bg='#4169e1', fg='white')

    #frame
    frame7_form = Frame(jan)
    frame7_form.place(x=250,y=105)
    frame7_form.configure(bg='#4169e1')
    
    #campo 1
    t_quant = Label(frame7_form, text='Quantidade Func: ', font=('Century Gothic', 10))
    t_quant.grid(row=1, column=0)
    t_quant.configure(bg='#4169e1', fg='white')
    edt_quant = Entry(frame7_form, width=10)
    edt_quant.grid(row=1, column=3)

    #frame
    frame8_form = Frame(jan)
    frame8_form.place(x=457,y=105)
    frame8_form.configure(bg='#4169e1')
    
    #campo 1
    t_remuneracao = Label(frame8_form, text='Remuneração: ', font=('Century Gothic', 10))
    t_remuneracao.grid(row=1, column=0)
    t_remuneracao.configure(bg='#4169e1', fg='white')
    edt_remuneracao = Entry(frame8_form, width=17)
    edt_remuneracao.grid(row=1, column=3)

    
    

    

    #insere dados nos ENTRYS caso op==1, ALTERAÇÃO ativada
    if op==1:
        dicionario = vt.item(vt.focus())
        linha = list(dicionario['values'])
        edt_nome.insert(0, linha[1])
        edt_cnpj.insert(0, linha[2])
        edt_endereco.insert(0, linha[3])
        edt_email.insert(0, linha[4])
        edt_telefone.insert(0, linha[5])
        edt_quant.insert(0, linha[6])
        edt_horario.insert(0, linha[7])
        edt_remuneracao.insert(0, linha[8])

    #barra dos botoes confirmar/cancelar
    barra_botoes = Frame(jan)
    barra_botoes.place(x=510, y=140)
    barra_botoes2 = Frame(jan)
    barra_botoes2.place(x=599, y=140)
    
    btn_confirmar = Button(barra_botoes, text = 'CONFIRMAR',
                           command= lambda: confirmadados(op, jan, edt_nome,
                                                         edt_cnpj, edt_endereco, edt_email,
                                                         edt_telefone,edt_quant,edt_horario,edt_remuneracao, vt))
    btn_confirmar.grid(row=0, column=0)
    btn_confirmar.configure(bg='white', fg='#4169e1')

    btn_cancelar = Button(barra_botoes2, text = 'CANCELAR',
                          command=jan.destroy)
    btn_cancelar.grid(row=0, column=1)
    btn_cancelar.configure(bg='white', fg='#4169e1')

#Código para Exclusão de dados
def excluidados(vt):
    dicionario = vt.item(vt.focus())
    linha = list(dicionario['values'])
    vsql = "DELETE FROM EMPRESA WHERE ID_EMP = {}".format(linha[0])

    conecta = sqlite3.connect('emp.db')  # ativa o banco de dados
    cursor = conecta.cursor()               #conecta o cursor
    cursor.execute(vsql)                    #executa o comando SQL
    conecta.commit()                        #confirma o SQL no BD
    conecta.close()                         #fecha o banco de dados
    mostra(vt,0,'')

#Código para CONFIRMAÇÂO dos dados alterados/inseridos
def confirmadados(tarefa, tela, vnm, vcnpj, vend, vemail, vtel,vquant,vhora,vremun, vt):
    #se tarefa for 0, a funçao INSERE dados
    #se tarefa for 1, funçao vai ALTERAR os dados
   
    #confirmaçao de dados de INCLUSÃO
    if tarefa==0:
        vsql = "INSERT INTO EMPRESA (NOME, CNPJ, ENDERECO, EMAIL, TELEFONE, QUANTFUN, HORAFUN, REMUN) VALUES \
                   ('{}','{}','{}','{}','{}','{}','{}','{}')".format(str(vnm.get()),
                                                                float(vcnpj.get()),
                                                                str(vend.get()),
                                                                str(vemail.get()),
                                                                float(vtel.get()),
                                                                float(vquant.get()),
                                                                str(vhora.get()),
                                                                float(vremun.get())
                                                                )

    #confirmação de dados de ALTERAÇÃO
    if tarefa==1:
        dicionario = vt.item(vt.focus())
        linha = list(dicionario['values'])
        vsql = "UPDATE EMPRESA SET NOME = '{}',CNPJ='{}',ENDERECO='{}',EMAIL='{}', \
                TELEFONE='{}',QUANTFUN='{}',HORAFUN='{}',REMUN='{}' \
                WHERE ID_EMP = '{}'".format(str(vnm.get()),
                                            float(vcnpj.get()),
                                            str(vend.get()),
                                            str(vemail.get()),
                                            float(vtel.get()),
                                            float(vquant.get()),
                                            str(vhora.get()),
                                            float(vremun.get()),
                                            linha[0])
   
    tela.destroy()                          #fechará a janela
    conecta = sqlite3.connect('emp.db')     #ativa o banco de dados
    cursor = conecta.cursor()               #conecta o cursor
    cursor.execute(vsql)                    #executa o comando SQL
    conecta.commit()                        #confirma o SQL no BD
    conecta.close()                         #fecha o banco de dados
    mostra(vt,0,'')                              #atualiza o Treeview
   

#codigo do botão sair

def sair(janela):
    if messagebox.askyesno("Sair","Deseja sair da aplicação ?"):
        janela.destroy()
       
#Código principal do programa
       
def Empresa():
    #chamada da função criaDB
    criaDB()
    #Construindo a tela
    janela = Tk()
    janela.geometry('740x580')
    janela.title('Sistema de Cadastramento de Empresas')
    janela.resizable(0,0)
    janela.configure(bg='#4169e1')
    janela.protocol("WM_DELETE_WINDOW", lambda: sair(janela))
    #definção e posicionamento dos widgets
    #cabeçalho
    frame_topo = Frame(janela)
    frame_topo.pack()
    frame_topo.configure(bg='#4169e1')
    t_titulo = Label(frame_topo, text='PARA A EMPRESA', font=('Century Gothic',16))
    t_titulo.pack()
    t_titulo.configure(bg='#4169e1', fg='white')
    #montando o filtro
    frame_filtro = Frame(janela)
    frame_filtro.pack()
    frame_filtro.configure(bg='#4169e1')
    t_filtro = Label(frame_filtro, text='Filtrar', font=('Century Gothic',12))
    t_filtro.grid(row=0, column=0)
    t_filtro.configure(bg='#4169e1', fg='white')

    edt_filtro = Entry(frame_filtro)
    edt_filtro.grid(row=0, column=1)

    
    btn_filtrar = Button(frame_filtro, text='Filtrar', command=lambda: mostra(tabela,1, edt_filtro.get()))
    btn_filtrar.grid(row=10, column=0, pady=10)
    btn_filtrar.configure(bg='white', fg='#4169e1')
   
    btn_mtudo =  Button(frame_filtro, text='Mostrar Tudo', command=lambda: mostra(tabela,0,edt_filtro.delete(0,END)))
    btn_mtudo.grid(row=10, column=1)
    btn_mtudo.configure(bg='white', fg='#4169e1')

    #corpo do formulario
    frame_meio = Frame(janela)
    frame_meio.pack()
    tabela = ttk.Treeview(frame_meio, columns = (1,2,3,4,5,6),
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
    

    #definindo o tamanho dos cabeçalhos
    tabela.column(1, width=50)
    tabela.column(2, width=170)
    tabela.column(3, width=95)
    tabela.column(4, width=150)
    tabela.column(5, width=130)
    tabela.column(6, width=85)
    

    #inserindo a barra de rolagem
    b_rolagem = ttk.Scrollbar(frame_meio, orient='vertical', command=tabela.yview)
    b_rolagem.pack(side='right',fill='y')
    tabela.configure(yscrollcommand=b_rolagem.set)

    #exibindo os dados no treeview
    mostra(tabela,0,'')

    #barra de ferramentas com botões INSERIR, ALTERAR e EXCLUIR
    frame_barra = Frame(janela)
    frame_barra.pack()
    frame_barra.configure(bg='#4169e1')
    btn_insere = Button(frame_barra, text='INSERIR', command=lambda: teladados(0, janela, tabela))
    btn_insere.grid(row=0, column=0, pady=10)
    btn_insere.configure(bg='white', fg='#4169e1')

    btn_altera = Button(frame_barra, text='ALTERAR', command=lambda: teladados(1, janela, tabela))
    btn_altera.grid(row=0, column=1)
    btn_altera.configure(bg='white', fg='#4169e1')

    btn_exclui = Button(frame_barra, text='EXCLUIR', command=lambda: excluidados(tabela))
    btn_exclui.grid(row=0, column=2)
    btn_exclui.configure(bg='white', fg='#4169e1')

   
   

    #loop principal
    janela.mainloop()

programa = Empresa()

