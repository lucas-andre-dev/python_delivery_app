import sqlite3 as sq

class sqliteConnection:
    def __init__(self,data_base="delivery"):
        self.conn = None
        self.data_base = data_base
        self.erro = None
    def connect(self):
        try:
            self.conn = sq.connect(self.data_base)
            return self.conn
        except sq.Error as e:
            self.erro = e
    
    def close(self):
        self.conn.close()

    def getErro(self):
        return self.erro