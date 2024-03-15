import pandas as pd
import psycopg2
import matplotlib.pyplot as plt
import os


#Conectar ao banco de dados
conn = psycopg2.connect(
    host="ip", 
    database="nome banco",
    user="usuario bd",
    password="senha")

#Query SQL
sql = "select * from tabela as nome_desejado where a.filtro ilike '%TESTE%'"

#Ler a tabela usando pandas
df = pd.read_sql(sql, conn)

#Salvar o DataFrame em um arquivo Excel em outro diretório
caminho = 'C:/aqui/salvar_sql'
nome_arquivo = 'tabela.xlsx'
caminho_completo = os.path.join(caminho, nome_arquivo)

df.to_excel(caminho_completo, index=False)

#Fechar a conexão
conn.close()
