import cx_Oracle

username = 'STUDENT1'
password = 'STUDENT1'
databaseName = "192.169.1.105/orcl"

connection = cx_Oracle.connect(username, password, databaseName)

cursor = connection.cursor()

"""------------QUERY 1------------------------------"""

query = 'SELECT \'Hello from Oracle!\' FROM DUAL'
print(query)
cursor.execute(query)

data = cursor.fetchone()[0]
print(data)