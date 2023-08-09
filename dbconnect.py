import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='mysqldatabase@29',
    port='3306',
    database='library'
)
mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM books')
books = mycursor.fetchall()
for i in books:
    print(i)