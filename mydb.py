import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="17061985",
    auth_plugin="mysql_native_password",
)


# create a cursor object
curserObject = dataBase.cursor()

# create a database
curserObject.execute("CREATE DATABASE crm_db")
print("All Done! Database Created")
