import mysql.connector
from mysql.connector import Error

hostname = "ognvv.h.filess.io"
database = "test_feathersto"
port = "61002"
username = "test_feathersto"
password = "fb175fb5c48b064ae626226606f7fa0a66d8cf00"

try:
    connection = mysql.connector.connect(host=hostname, database=database, user=username, password=password, port=port)
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

