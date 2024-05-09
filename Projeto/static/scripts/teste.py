import mysql.connector
import json
from datetime import date, datetime
import os

conexao = mysql.connector.connect(host='localhost', database='d_mais',user='root', password='aas798118')
if conexao.is_connected():
    comando = ("SELECT * FROM clientes")
    cursor= conexao.cursor()
    cursor.execute(comando)
    retorno = cursor.fetchall()
    conexao.commit()
    clientes=[]
    niver =[]
   # print(retorno)
    for i in retorno:
        
        z = i[3]
        y = z.strftime('%Y/%m/%d')
        clie= [i[0],i[1],i[2],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]]  
        clientes.append(clie)
        niver.append(y)
    
    clientes=json.dumps(clientes)
    niver = json.dumps(niver)

# Cria os arquivos json
    with open("niver.json", "w") as arquivo:
        arquivo.write(niver)
    with open("clientes.json", "w") as arquivo:
        arquivo.write(clientes)

# Exclui os arquivos json
    if os.path.exists("clientes.json"):
        os.remove("clientes.json")

    if os.path.exists("niver.json"):
        os.remove("niver.json")    


    #print(clientes)
    #print("Conectado ao banco de dados
    if conexao.is_connected():
        cursor.close()
        conexao.close()
        print("Desconectado do banco de dados")