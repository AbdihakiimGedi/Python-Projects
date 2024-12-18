import mysql.connector as my
db=my.connect(
    host="localhost",
    user="root",
    password="",
    database="last"
    )
cr=db.cursor()
