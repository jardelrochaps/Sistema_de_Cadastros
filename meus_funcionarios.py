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

#Criando a tabela do banco de dados

def criaDB():
    conecta = sqlite3.connect('estagio.db')
    cursor = conecta.cursor()
    sqldb = '''
    CREATE TABLE IF NOT EXISTS ESTAGIARIOS (
    NOME TEXT NOT NULL,
    CURSO TEXT NOT NULL,
    CPF CHAR(14) PRIMARY KEY NOT NULL,
    ESCOLARIDADE TEXT NOT NULL,
    EXPERIENCIA VARCHAR(10),
    SEXO TEXT,
    ESTADO TEXT,
    CIDADE TEXT,
    TELEFONE INTEGER,
    EMAIL TEXT,
    DISPONIBILIDADE TEXT NOT NULL,
    ENDERECO TEXT NOT NULL,
    CELULAR INTEGER NOT NULL);
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
               
    conecta = sqlite3.connect('estagio.db')
    cursor = conecta.cursor()
    if op==0:
        vsql = 'SELECT * FROM ESTAGIARIOS'
    elif op==1:
        vsql = 'SELECT * FROM ESTAGIARIOS WHERE CPF LIKE "%{}%"'.format(texto)
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
    jan.geometry('510x300+400+150')
    jan.configure(bg='#4169E1')
    if op ==0:
        jan.title('Cadastro de estagiários')
    elif op==1:
        jan.title('ALTERANDO DADOS')
    jan.transient(vj)
    jan.focus_force()
    jan.grab_set()


#========================================================================

        #posiconamento de nome
    frame_form = Frame(jan)
    frame_form.place(x=15, y=15)
    frame_form.configure(bg='#4169E1')
    
    #campo nome
    t_nome = Label(frame_form, text='Nome: ', font=('Century Gothic', 10))
    t_nome.grid(row=0, column=0)
    t_nome.configure(bg='#4169E1', fg='white')
    edt_nome = Entry(frame_form, width=48)
    edt_nome.grid(row=0, column=3)


    
        #posicionamentos de curso
    frame2_form = Frame(jan)
    frame2_form.place(x=15, y=45)
    frame2_form.configure(bg='#4169E1')
    #campo curso
    t_curso = Label(frame2_form, text='Curso: ', font=('Century Gothic', 10))
    t_curso.grid(row=1, column=0)
    t_curso.configure(bg='#4169E1', fg='white')
    edt_curso = Entry(frame2_form, width=70)
    edt_curso.grid(row=1, column=3)


        #posicionamentos de cpf
    frame1_form = Frame(jan)
    frame1_form.place(x=365, y=15)
    frame1_form.configure(bg='#4169E1')
    #campo cpf
    t_cpf = Label(frame1_form, text='CPF: ', font=('Century Gothic', 10))
    t_cpf.grid(row=0, column=0)
    t_cpf.configure(bg='#4169E1', fg='white')
    edt_cpf = Entry(frame1_form, width=14)
    edt_cpf.grid(row=0, column=3)
    
        #posicionamentos de escolaridade
    frame3_form = Frame(jan)
    frame3_form.place(x=15, y=75)
    frame3_form.configure(bg='#4169E1')
    #campo escolaridade
    t_escolaridade = Label(frame3_form, text='Escolaridade: ', font=('Century Gothic', 10))
    t_escolaridade.configure(bg='#4169E1', fg='white')
    t_escolaridade.grid(row=2, column=0)
    edt_escolaridade = Entry(frame3_form, width=31)
    edt_escolaridade.grid(row=2, column=3)
    edt_escolaridade.focus_set()

    
        #posicionamentos de experiência
    frame01_form = Frame(jan)

    #campo experiência

    frame01_form.place(x=307, y=75)
    frame01_form.configure(bg='#4169E1')

    #campo de experiência dos botões sim e não
    
    t_experiencia =Label(frame01_form, text= 'Experiência ?: ', font=('Century Gothic', 10))
    t_experiencia.grid(row=4, column=0)
    t_experiencia.configure(bg='#4169E1', fg='white')



    ent_exp = Entry(jan, width=11)
    ent_exp.place(x=400, y=75)
    ent_exp.focus_set()



        #posicionamentos de disponibilidade
    frame69_form = Frame(jan)
    frame69_form.place(x=15, y=105)

  
    #campo sexo
    t_sexo =Label(frame69_form, text= 'Sexo:', font=('Century Gothic', 10))
    t_sexo.grid(row=4, column=0)
    t_sexo.configure(bg='#4169E1', fg='white')



    ent_sexo = ttk.Combobox(jan, width=9)
    ent_sexo.configure(values=["Masculino",
                            "Feminino",
                            "Outro"])
    ent_sexo.place(x=55, y=106)


        #posicionamentos de estado
    frameest_form = Frame(jan)
    frameest_form.place(x=380, y=105)

    #campo estado
    t_estado =Label(frameest_form, text= 'Estado: ', font=('Century Gothic', 10))
    t_estado.grid(row=4, column=0)
    t_estado.configure(bg='#4169E1', fg='white')



    ent_estado = ttk.Combobox(jan, width=5)
    ent_estado.configure(values=["AC","AL","AM","AP","BA","CE","DF",
                             "ES","GO","MA","MG","MS","MT","PA",
                             "PB","PE","PI","PR","RJ","RN","RO",
                             "RR","RS","SC","SE","SP","TO"])
    ent_estado.place(x=437, y=106)


        #posicionamentos de disponibilidade
    framecid_form = Frame(jan)
    framecid_form.place(x=136, y=105)
    framecid_form.configure(bg='#4169E1')
    #campo disponibilidade
    t_cidade = Label(framecid_form, text='Cidade: ', font=('Century Gothic', 10))
    t_cidade.grid(row=4, column=0)
    t_cidade.configure(bg='#4169E1', fg='white')
    edt_cidade = Entry(framecid_form, width=29)
    edt_cidade.grid(row=4, column=3)


            #posicionamentos de endereço
    frame9_form = Frame(jan)
    frame9_form.place(x=15, y=135)
    frame9_form.configure(bg='#4169E1')
    #campo endereço
    t_endereco = Label(frame9_form, text='Endereço: ', font=('Century Gothic', 10))
    t_endereco.grid(row=4, column=0)
    t_endereco.configure(bg='#4169E1', fg='white')
    edt_endereco = Entry(frame9_form, width=66)
    edt_endereco.grid(row=4, column=3)


    
        #posicionamentos de disponibilidade
    frame5_form = Frame(jan)
    frame5_form.place(x=15, y=165)
    frame5_form.configure(bg='#4169E1')
    #campo disponibilidade
    t_disponibilidade = Label(frame5_form, text='Disponível: ', font=('Century Gothic', 10))
    t_disponibilidade.grid(row=4, column=0)
    t_disponibilidade.configure(bg='#4169E1', fg='white')
    edt_disponibilidade = Entry(frame5_form, width=20)
    edt_disponibilidade.grid(row=4, column=3)


    
        #posicionamentos de celular
    frame6_form = Frame(jan)
    frame6_form.place(x=223, y=165)
    frame6_form.configure(bg='#4169E1')
    #campo celular
    t_celular = Label(frame6_form, text='Cel.: ', font=('Century Gothic', 10))
    t_celular.grid(row=4, column=0)
    t_celular.configure(bg='#4169E1', fg='white')
    edt_celular = Entry(frame6_form, width=15)
    edt_celular.grid(row=4, column=3)



        #posicionamentos de telefone
    frame7_form = Frame(jan)
    frame7_form.place(x=362, y=165)
    frame7_form.configure(bg='#4169E1')
    #campo telefone
    t_telefone = Label(frame7_form, text='Tel.: ', font=('Century Gothic', 10))
    t_telefone.grid(row=4, column=0)
    t_telefone.configure(bg='#4169E1', fg='white')
    edt_telefone = Entry(frame7_form, width=15)
    edt_telefone.grid(row=4, column=3)



        #posicionamentos de email
    frame8_form = Frame(jan)
    frame8_form.place(x=15, y=195)
    frame8_form.configure(bg='#4169E1')
    #campo email
    t_email = Label(frame8_form, text='Email:', font=('Century Gothic', 10))
    t_email.grid(row=4, column=0)
    t_email.configure(bg='#4169E1', fg='white')
    edt_email = Entry(frame8_form, width=71)
    edt_email.grid(row=4, column=3)



#==============================================================================
#==============================================================================


    
    #insere dados nos ENTRYS caso op==1, ALTERAÇÃO ativada
    if op==1:
        dicionario = vt.item(vt.focus())
        linha = list(dicionario['values'])
        edt_nome.insert(0, linha[0])
        edt_curso.insert(0, linha[1])
        edt_cpf.insert(0, linha[2])
        edt_escolaridade.insert(0, linha[3])
        ent_exp.insert(0, linha[4])
        ent_sexo.insert(0, linha[5])
        ent_estado.insert(0, linha[6])
        edt_cidade.insert(0, linha[7])
        edt_telefone.insert(0, linha[8])
        edt_email.insert(0, linha[9])
        edt_disponibilidade.insert(0, linha[10])
        edt_endereco.insert(0, linha[11])
        edt_celular.insert(0, linha[12])

    #barra dos botoes confirmar/cancelar
    barra_botoes = Frame(jan)
    barra_botoes.place(x=200, y=240)

#======================================================
#ajeita aqui
#======================================================
    
    btn_confirmar = Button(barra_botoes, text = 'Confirmar', font=('Arial',9,'bold'),
                           command= lambda: confirmadados(op, jan, edt_nome, edt_curso, edt_cpf, edt_escolaridade, ent_exp,
                                                                ent_sexo, ent_estado, edt_cidade, edt_telefone, edt_email,
                                                                edt_disponibilidade, edt_endereco, edt_celular, vt))

    
    btn_confirmar.grid(row=0, column=0)
    btn_confirmar.configure(bg='white', fg='#4169E1')
    
    btn_cancelar = Button(barra_botoes, text = 'Cancelar', font=('Arial',9,'bold'),
                          command=jan.destroy)
    btn_cancelar.configure(bg='white', fg='#4169E1')
    btn_cancelar.grid(row=0, column=1)

#Código para Exclusão de dados
def excluidados(vt):
    dicionario = vt.item(vt.focus())
    linha = list(dicionario['values'])
    vsql = "DELETE FROM ESTAGIARIOS WHERE CPF = {}".format(linha[0])

    conecta = sqlite3.connect('estagio.db')  #ativa o banco de dados
    cursor = conecta.cursor()               #conecta o cursor
    cursor.execute(vsql)                    #executa o comando SQL
    conecta.commit()                        #confirma o SQL no BD
    conecta.close()                         #fecha o banco de dados
    mostra(vt,0,'')

#Código para CONFIRMAÇÂO dos dados alterados/inseridos
def confirmadados(tarefa, tela, vnm, vcurso, vcpf, vescol, vexp, vsexo, vestado, vcidade, vtel, vemail, vdispon, vendereco, vcel, vt):
    #se tarefa for 0, a funçao INSERE dados
    #se tarefa for 1, funçao vai ALTERAR os dados

    
    #confirmaçao de dados de INCLUSÃO
    if tarefa==0:
        vsql = "INSERT INTO ESTAGIARIOS (NOME, CURSO, CPF, ESCOLARIDADE, EXPERIENCIA, SEXO, ESTADO, CIDADE, TELEFONE, EMAIL, DISPONIBILIDADE, ENDERECO, CELULAR) VALUES \
                   ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(str(vnm.get()),
                                                                                        str(vcurso.get()),
                                                                                        int(vcpf.get()),
                                                                                        str(vescol.get()),
                                                                                        str(vexp.get()),
                                                                                        str(vsexo.get()),
                                                                                        str(vestado.get()),
                                                                                        str(vcidade.get()),
                                                                                        int(vtel.get()),
                                                                                        str(vemail.get()),
                                                                                        str(vdispon.get()),
                                                                                        str(vendereco.get()),
                                                                                        int(vcel.get()))
                                                    

    #confirmação de dados de ALTERAÇÃO
    if tarefa==1:
        dicionario = vt.item(vt.focus())
        linha = list(dicionario['values'])
        vsql = "UPDATE ESTAGIARIOS SET NOME = '{}',CURSO='{}',CPF='{}',ESCOLARIDADE='{}',EXPERIENCIA='{}',SEXO='{}',ESTADO='{}', \
                CIDADE='{}',TELEFONE='{}',EMAIL='{}',DISPONIBILIDADE='{}',ENDERECO='{}',CELULAR='{}' \
                WHERE CPF= '{}'".format(str(vnm.get()),
                                    str(vcurso.get()),
                                    int(vcpf.get()),
                                    str(vescol.get()),
                                    str(vexp.get()),
                                    str(vsexo.get()),
                                    str(vestado.get()),
                                    str(vcidade.get()),
                                    int(vtel.get()),
                                    str(vemail.get()),
                                    str(vdispon.get()),
                                    str(vendereco.get()),
                                    int(vcel.get()),
                                    linha[2])
    
    tela.destroy()                          #fechará a janela
    conecta = sqlite3.connect('estagio.db')  #ativa o banco de dados
    cursor = conecta.cursor()               #conecta o cursor
    cursor.execute(vsql)                    #executa o comando SQL
    conecta.commit()                        #confirma o SQL no BD
    conecta.close()                         #fecha o banco de dados
    mostra(vt,0,'')                              #atualiza o Treeview
    




#======================================================
#ajeita aqui
#======================================================
    

#codigo do botão sair

def sair(janela):
    if messagebox.askyesno("Sair","Deseja sair da aplicação ?"):
        janela.destroy()
       
#Código principal do programa
       
def Main():
    #chamada da função criaDB
    criaDB()
    #Construindo a tela
    janela = Tk()
    janela.geometry('1061x480+250+100')
    janela.configure(bg='#4169E1')
    janela.title('Estagio')
    janela.resizable(0,0)
    janela.protocol("WM_DELETE_WINDOW", lambda: sair(janela))
    #definção e posicionamento dos widgets

    #Barra DE Ferramentas
    #===================================================================
    barraferramentas = Frame(janela)
    barraferramentas.pack(fill=X)



        #cabeçalho
    frame_topo = Frame(janela)
    frame_topo.pack()
    t_titulo = Label(frame_topo, text='FUNCIONÁRIOS CONTRADOS', font=('Century Gothic',16))
    t_titulo.pack()
    t_titulo.grid(ipady=7)
    t_titulo.configure(bg='#4169E1', fg='white')
    #montando o filtro
    frame_filtro = Frame(janela)
    frame_filtro.pack()
    frame_filtro.configure(bg='#4169E1')

    
    t_filtro = Label(frame_filtro, text='Filtrar: ', font=('Century Gothic',12))
    t_filtro.grid(row=0, column=0)
    t_filtro.configure(bg='#4169E1', fg='white')

    edt_filtro = Entry(frame_filtro)
    edt_filtro.grid(row=0, column=1)
    edt_filtro.configure(bg='white', fg='white')

    btn_filtrar =  Button(frame_filtro, text='Filtrar', font=('Arial',9,'bold'), command=lambda: mostra(tabela,1, edt_filtro.get()))
    btn_filtrar.grid(row=1,column=0, pady=10)
    btn_filtrar.configure(bg='white', fg='#4169E1')
   
    btn_mtudo =  Button(frame_filtro, text='Mostrar Tudo', font=('Arial',9,'bold'), command=lambda: mostra(tabela,0,edt_filtro.delete(0,END)))
    btn_mtudo.grid(row=1,column=1)
    btn_mtudo.configure(bg='white', fg='#4169E1')

    #corpo do formulario
    frame_meio = Frame(janela)
    frame_meio.place(x=15, y=120)
    tabela = ttk.Treeview(frame_meio, columns = (1,2,3,4,5,6,7),
                          show = 'headings', selectmode='browse',
                          displaycolumns='#all')
    tabela.pack(side='left')
    
    #definindo os titulos dos cabeçalhos
    tabela.heading(1, text='Nome')
    tabela.heading(2, text='Curso')
    tabela.heading(3, text='CPF')
    tabela.heading(4, text='Escolaridade')
    tabela.heading(5, text='EXP')
    tabela.heading(6, text='Sexo')
    tabela.heading(7, text='Estado')
#acho que ele vai seguir a sequencia das informarções ou do formulario
#ou a sequencia do banco de dados
    
    #definindo o tamanho dos cabeçalhos
    tabela.column(1, width=250)
    tabela.column(2, width=150)
    tabela.column(3, width=210)
    tabela.column(4, width=100)
    tabela.column(5, width=100)
    tabela.column(6, width=100)
    tabela.column(7, width=100)
    #inserindo a barra de rolagem
    b_rolagem = ttk.Scrollbar(frame_meio, orient='vertical', command=tabela.yview)
    b_rolagem.pack(side='right',fill='y')
    tabela.configure(yscrollcommand=b_rolagem.set)

    #exibindo os dados no treeview
    mostra(tabela,0,'')

    #barra de ferramentas com botões INSERIR, ALTERAR e EXCLUIR


    frame_barra = Frame(janela)
    frame_barra.place(x=439,y=360)

    btn_insere = Button(frame_barra, text='Inserir', font=('Arial',9,'bold'), command=lambda: teladados(0, janela, tabela))
    btn_insere.grid(row=0, column=0)
    btn_insere.configure(bg='white', fg='#4169E1')

    btn_altera = Button(frame_barra, text='Alterar', font=('Arial',9,'bold'), command=lambda: teladados(1, janela, tabela))
    btn_altera.grid(row=0, column=2)
    btn_altera.configure(bg='white', fg='#4169E1')


    btn_exclui = Button(frame_barra, text='Excluir', font=('Arial',9,'bold'), command=lambda: excluidados(tabela))
    btn_exclui.grid(row=0, column=3)
    btn_exclui.configure(bg='white', fg='#4169E1')

   
   

    #loop principal
    janela.mainloop()

programa = Main()
