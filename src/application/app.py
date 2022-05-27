"""
Objetivo 1: se conectar ao banco de dados

    Para se conectar, a aplicação deverá receber:
        -   host
        -   porta
        -   database
        -   usuário
        -   senha
        -   tipo de banco de dados

Objetivo 2:

    Após se conectar, a aplicação terá que receber uma query de select e retornar
    o resultado da consulta.
"""
import psycopg2


def connect_to_db(host,
                  user,
                  database,
                  password,
                  database_type):
    if database_type == "postgres":
        print(f"Conectando com o posgres: database {database}, user: {user}")
        try:
            conn = psycopg2.connect(host=host,
                                    database=database,
                                    user=user,
                                    password=password)
            print(f"Conexão com o database: {database} deu bom.")
        except UnboundLocalError:
            print(f"Conexão com o database: {database} não deu bom.")


    else:
        print(f"Tipo de banco de dados ainda não implementado.")

    return conn


def executa_select(query, connection):
    cur = connection.cursor()
    cur.execute(query)
    recset = cur.fetchall()
    registros = []
    for rec in recset:
        registros.append(rec)
    connection.close()
    return registros


def executa_query_dml(query, connection):
    cur = connection.cursor()
    cur.execute(query)
    connection.commit()
    connection.close()


connection = connect_to_db(database="postgres",
                           host="localhost",
                           user="postgres",
                           password="postgres",
                           database_type="postgres")

resultado = executa_select(query="Select * from test_docker", connection=connection)

print(resultado)
