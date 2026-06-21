import sqlite3

def conector():
    return sqlite3.connect("SV_AI.db")

def armazem():
    con = conector()
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS palavra (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    palavras TEXT,
    id TEXT UNIQUE
    )  
""")  
    con.commit()  
    con.close()