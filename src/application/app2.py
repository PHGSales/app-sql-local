import mysql.connector

try:
    connection_mysql = mysql.connector.connect(host='localhost',
                                         database='test_mysql',
                                         user='root',
                                         password='root')

    print("Conectado ao MySQ!")

    query = """CREATE TABLE CIDADE (CEP int(3) NOT NULL) """
    cursor = connection_mysql.cursor()
    result = cursor.execute(query)
    print("Tabela criada com sucesso!")

except mysql.connector.Error as error:
    print("Falha ao criar tabela no MySQL: {}".format(error))

