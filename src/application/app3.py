import psycopg2
import mysql.connector

def connect_to_db(host,
                  user,
                  database_type,
                  password,
                  port
                  ):
    if database_type == "mysql":
        print(f"Conectando com o MySQL: with user: {user}.")
        try:
            conn = mysql.connector.connect(host=host,
                                           user=user,
                                           password=password,
                                           port=port)
            print(f"Conexão com o MySQL: deu bom.")
            return conn
        except mysql.connector.Error as error:
            print(f"Fail to connect with MySQL with error: {error}.")

    if database_type == "postgres":
        print(f"Conectando com o POSTGRES: with user: {user}.")
        try:
            conn = psycopg2.connect(host=host,
                                    user=user,
                                    password=password,
                                    port=port)
            print(f"Conexão com o MySQL: deu bom.")
            return conn
        except UnboundLocalError as error:
            print(f"Fail to connect with POSTGRES with error: {error}.")

    else:
        print("Tipo de banco de dados ainda não implementado.")


def executa_query_dml(query, connection):
    print(f"Executando a query dml no banco.")
    cur = connection.cursor()
    cur.execute(query)
    connection.commit()
    print(f"Query dml executada com sucesso.")


def executa_select(query, connection):
    print(f"Executando o select no banco.")
    cur = connection.cursor()
    cur.execute(query)
    print(f"Parseando os resultados para uma lista.")
    recset = cur.fetchall()
    registros = []
    for rec in recset:
        registros.append(rec)
    return registros


mysql_conn = connect_to_db(database_type='mysql',
                           host='localhost',
                           user='root',
                           password='root',
                           port="3306")

postgres_conn = connect_to_db(database_type='postgres',
                              host='localhost',
                              user='postgres',
                              password='postgres',
                              port="5432")

# executa_query_dml(query="Create table test_mysql.test_mysql (id char, nome char)", connection=mysql_conn)
#
# executa_query_dml(query="Create table public.test_postgres (id char, nome char)", connection=postgres_conn)

executa_query_dml(query="insert into test_mysql.test_mysql values ('1', 't')", connection=mysql_conn)

executa_query_dml(query="insert into public.test_postgres values ('1', 't')", connection=postgres_conn)

mysql_result = executa_select(query="select * from test_mysql.test_mysql", connection=mysql_conn)

postgres_result = executa_select(query="select * from public.test_postgres", connection=postgres_conn)

print(mysql_result)
print(postgres_result)