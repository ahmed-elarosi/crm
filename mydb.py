import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="17061985",
)


# create a cursor object
curserObject = dataBase.cursor()

# create a database
curserObject.execute("CREATE DATABASE crm_db")
print("All Done! Database Created")
