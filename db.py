import sqlite3


db = sqlite3.connect('db.sqlite')

def create_table():
    db.execute('create table if NOT exists products (id INTEGER PRIMARY KEY, name TEXT, price real)')

if __name__=='__main__':
    create_table()
    db.close()