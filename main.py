import tkinter as tk
from tkinter import ttk
import datetime as dt
import mysql.connector

#Conexao banco de dados

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='neto1234',
    database='bd_cadastro',
)
cursor = conexao.cursor()

nome = "nome"
whatsapp = "nome"
endereco = "resposta0"
pergunta1 = "resposta1"
pergunta2 = "resposta2"
pergunta3 = "resposta3"
pergunta4 = "resposta4"
especifique4 = "resposta4"
pergunta5 = "resposta5"
pergunta6 = "resposta6"
especifique6 = "resposta6"
pergunta7 = "resposta7"
pergunta8 = "resposta8"
especifique8 = "resposta8"
pergunta9 = "resposta9"
autorizacao = "resposta8"
data_cadastro = "data"
comando = f'INSERT INTO cadastros (nome, whatsapp, endereco, pergunta1, pergunta2, pergunta3, pergunta4, especifique4, pergunta5, pergunta6, especifique6, pergunta7, pergunta8, especifique8, pergunta9, autorizacao, data_cadastro) VALUES ("{nome}", "{whatsapp}", "{endereco}","{pergunta1}", "{pergunta2}", "{pergunta3}", "{pergunta4}", "{especifique4}", "{pergunta5}", "{pergunta6}", "{especifique6}", "{pergunta7}", "{pergunta8}", "{especifique8}", "{pergunta9}", "{autorizacao}", "{data_cadastro}")'
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()

#fim da conexão banco de dados.

#List

lista_opcoes = ["Não","Sim"]
lista_codigos = []


janela = tk.Tk()
janela.title('Cadastro de Clientes')


# Função

def cadastrar_cliente():
    nome = entry_nome.get()
    whatsapp = entry_whatsapp.get()
    endereco = entry_endereco.get()
    pergunta1 = combobox_pergunta1.get()
    pergunta2 = combobox_pergunta2.get()
    pergunta3 = combobox_pergunta3.get()
    pergunta4 = combobox_pergunta4.get()
    especifique4 = entry_especifique4.get()
    pergunta5 = combobox_pergunta5.get()
    pergunta6 = combobox_pergunta6.get()
    especifique6 = entry_especifique6.get()
    pergunta7 = combobox_pergunta7.get()
    pergunta8 = combobox_pergunta8.get()
    especifique8 = entry_especifique8.get()
    pergunta9 = combobox_pergunta9.get()
    autorizacao = combobox_autorizacao.get()
    data_cadastro = dt.datetime.now()
    data_cadastro = data_cadastro.strftime("%d/%m/%Y %H:%M")
    codigo = len(lista_codigos) + 1
    codigo_str = "COD-{}".format(codigo)
    lista_codigos.append((
                         codigo_str, nome, whatsapp, endereco, pergunta1, pergunta2, pergunta3, pergunta4, especifique4,
                         pergunta5, pergunta6, especifique6, pergunta7, pergunta8, especifique8, pergunta9, autorizacao,
                         data_cadastro))



#Labels

label_nome = tk.Label(janela, text='Nome',)
label_nome.grid(row=0, column=0, padx=10, pady=10, )

label_whatsapp = tk.Label(janela, text='Whatsapp')
label_whatsapp.grid(row=1, column=0, padx=10, pady=10)

label_endereco = tk.Label(janela, text='Endereço')
label_endereco.grid(row=2, column=0, padx=10, pady=10)

label_anamnese = tk.Label(janela, text='Ficha De Anamnese')
label_anamnese.grid(row=3, column=1, padx=20, pady=20)

label_pergunta1 = tk.Label(janela, text='Está De Rímel?')
label_pergunta1.grid(row=4, column=0, padx=10, pady=10)

label_pergunta2 = tk.Label(janela, text='É gestante?')
label_pergunta2.grid(row=4, column=2, padx=10, pady=10)

label_pergunta3 = tk.Label(janela, text='Fez Algum Procedimento Recente Nos Olhos?')
label_pergunta3.grid(row=6, column=0, padx=10, pady=10)

label_pergunta4 = tk.Label(janela, text='Alergia á Esmaltes/Cosméticos/Cianocrilato?')
label_pergunta4.grid(row=7, column=0, padx=10, pady=10)
label_especifique4 = tk.Label(janela, text='Sim? Especifique:')
label_especifique4.grid(row=8, column=0, padx=10, pady=10)

label_pergunta5 = tk.Label(janela, text='Possui Problemas De Tireoide?')
label_pergunta5.grid(row=7, column=2, padx=10, pady=10)

label_pergunta6 = tk.Label(janela, text='Possui Glaucoma/Blefarite ou Algum Problema Ocular?')
label_pergunta6.grid(row=10, column=0, padx=10, pady=10)
label_especifique6 = tk.Label(janela, text='Sim? Especifique:')
label_especifique6.grid(row=11, column=0, padx=10, pady=10)

label_pergunta7 = tk.Label(janela, text='Está Em Tratamento Oncológico?')
label_pergunta7.grid(row=10, column=2, padx=10, pady=10)

label_pergunta8 = tk.Label(janela, text='Existe Algo Que Julge Importante Informar?')
label_pergunta8.grid(row=13, column=0, padx=10, pady=10)
label_especifique8 = tk.Label(janela, text='Sim? Especifique:')
label_especifique8.grid(row=14, column=0, padx=10, pady=10)

label_pergunta9 = tk.Label(janela, text='Dorme De Lado?')
label_pergunta9.grid(row=13, column=2, padx=10, pady=10)


label_autorizacao = tk.Label(janela, text='Autorizo a realização do procedimento de Alogamento de Cilios.'
                                          ' Autorizo o registro fotográfico do ANTES e DEPOIS, Para documentação e divulgação profissional.' '\n'
                                          'As declarações acima são verdadeiras, não cabendo ao profissional a '
                                          'responsabilidade por informações omitidas nesta avaliação.' '\n'
                                          'Me comprometo a seguir todos os cuidados necessários após o procedimento')
label_autorizacao.grid(row=15, column=0, columnspan=100, padx=20, pady=20)


# Entrys

entry_nome = tk.Entry(janela, text='Nome',width=50)
entry_nome.grid(row=0, column=1, columnspan=1, padx=10, pady=20)

entry_whatsapp = tk.Entry(janela, text='Whatsapp',width=50)
entry_whatsapp.grid(row=1, column=1, padx=10, pady=20)

entry_endereco = tk.Entry(janela, text='Endereco',width=50)
entry_endereco.grid(row=2, column=1, padx=10, pady=20)

entry_especifique4 = tk.Entry(janela, text='Especifique4',width=40)
entry_especifique4.grid(row=8, column=1, padx=10, pady=10)

entry_especifique6 = tk.Entry(janela, text='Especifique6',width=40)
entry_especifique6.grid(row=11, column=1, padx=10, pady=10)

entry_especifique8 = tk.Entry(janela, text='Especifique8',width=40)
entry_especifique8.grid(row=14, column=1, padx=10, pady=10)

#lista_opção

combobox_pergunta1 = ttk.Combobox(values=lista_opcoes)
combobox_pergunta1.grid(row=4, column=1, padx=10, pady=10,)

combobox_pergunta2 = ttk.Combobox(values=lista_opcoes)
combobox_pergunta2.grid(row=4, column=3, padx=10, pady=10,)

combobox_pergunta3 = ttk.Combobox(values=lista_opcoes)
combobox_pergunta3.grid(row=6, column=1, padx=10, pady=10,)

combobox_pergunta4 = ttk.Combobox(values=lista_opcoes)
combobox_pergunta4.grid(row=7, column=1, padx=10, pady=10,)

combobox_pergunta5 = ttk.Combobox(values=lista_opcoes)
combobox_pergunta5.grid(row=7, column=3, padx=10, pady=10,)

combobox_pergunta6 = ttk.Combobox(values=lista_opcoes)
combobox_pergunta6.grid(row=10, column=1, padx=10, pady=10,)

combobox_pergunta7 = ttk.Combobox(values=lista_opcoes)
combobox_pergunta7.grid(row=10, column=3, padx=10, pady=10,)

combobox_pergunta8 = ttk.Combobox(values=lista_opcoes)
combobox_pergunta8.grid(row=13, column=1, padx=10, pady=10,)

combobox_pergunta9 = ttk.Combobox(values=lista_opcoes)
combobox_pergunta9.grid(row=13, column=3, padx=10, pady=10,)

combobox_autorizacao = ttk.Combobox(values=lista_opcoes)
combobox_autorizacao.grid(row=16, column=1, padx=10, pady=10,)

# Botao

botao_cadastrar = tk.Button(janela, text='Cadastrar Cliente', command=cadastrar_cliente,width=20)
botao_cadastrar.grid(row=20, column=0, columnspan=40, padx=50, pady=50)

janela.mainloop()

print(lista_codigos)

