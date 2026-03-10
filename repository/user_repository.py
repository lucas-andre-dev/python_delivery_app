from database.connection import sqliteConnection
from model.user import userEntity
from sqlite3 import Error
from model.user import userEntity

class user_repository:
    def __init__(self):
        self.conexao = sqliteConnection()
        self.table = "user"
    

    def saveUser(self,user,password):
        try:

            if(password ==None and user==None):
                raise Exception('Password ans user is empty') 
            
            connect = self.conexao.connect()
            cursor = connect.cursor()
            sql = (f"INSERT INTO {self.table}(user,password) VALUES(?,?)")
            cursor.execute(sql,(user,password))
            connect.commit()
            connect.close()

        except Error as e:
            print(f"Erro no banco {e}")