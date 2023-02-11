import pandas as pd
import mysql.connector

# Configurações do banco de dados
host = 'localhost'
user = 'CesarSun'
password = '080888'
database = 'projetos_pessoais'

# cria a conexão com o banco de dados
mydb = mysql.connector.connect(host=host, user=user, password=password, database=database)

# cria o cursor para executar comandos SQL
cursor = mydb.cursor()

# define as colunas da tabela do banco de dados
columns = ['uid', 'title', 'synopsis', 'genre', 'aired', 'episodes', 'members', 'popularity', 'ranked', 'score', 'link']

# carrega o arquivo csv para um DataFrame do pandas
df = pd.read_csv('C:\\Users\\cesar\\Documents\\Projetos\\Projetos_P\\Gerenciador de Animes\\MAL - archive\\animes.csv', usecols=columns)

# limita o tamanho dos campos para 100 caracteres
df = df.apply(lambda x: x.str.slice(0, 100) if x.dtype == "object" else x)

# preenche os valores nulos com a palavra 'null'
df = df.fillna('null')

# converte as colunas do DataFrame para listas de valores
df = df.values.tolist()

# define a consulta SQL para apagar os dados da tabela
delete_query = "DELETE FROM animes"

# executa a consulta SQL para apagar os dados da tabela
cursor.execute(delete_query)

# define a consulta SQL para inserir os dados na tabela do banco
insert_query = f"INSERT INTO animes ({', '.join(columns)}) VALUES ({', '.join(['%s']*len(columns))})"

# executa a consulta SQL para inserir os dados na tabela do banco
cursor.executemany(insert_query, df)

# faz o commit da transação
mydb.commit()

# fecha a conexão com o banco de dados
mydb.close()
