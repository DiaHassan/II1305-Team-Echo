import sqlite3

def connect():
    connection = sqlite3.connect("echo.db")
    return connection

def build():
    connection = connect()
    cursor = connection.cursor()

    sql_file = open("Project\db\db_sqlite.sql", "r")
    sql_script = sql_file.read()
    sql_file.close()

    cursor.executescript(sql_script)
    cursor.close()
    connection.close()


if __name__ == '__main__':
    build()