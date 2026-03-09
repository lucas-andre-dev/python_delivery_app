import sqlite3 as sq

class sqliteConnection:
    def __init__(self,data_base="delivery"):
        self.conn = None
        self.data_base = data_base
    
    def connect(self):
        try:
            self.conn = sq.connect(self.data_base)
            return self.conn
        except sq.Error as e:
            print(f"Erro {e}")
    
    def close(self):
        self.conn.close()

if __name__=="__main__":
    sql = sqliteConnection().connect()

    sql.cursor().execute("""CREATE TABLE user(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   user TEXT NOT NULL UNIQUE,
                   password TEXT NOT NULL
                   )""")
    sql.commit()
    sql.close()