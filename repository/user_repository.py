from database.connection import sqliteConnection
from model.user import userEntity
class user_repository:
    def __init__(self):
        self.conn = sqliteConnection()
        self.table = "user"
    

    def saveUser(self,user:userEntity):
        try:
            name = user.getName()
            password = user.getPassword()
            cursor = self.conn.connect()
            sql = (f"""INSERT INTO {self.table}(name,password) VALUES(?,?)""")
            cursor.execute(sql,(name,password))
            cursor.commit()

        except cursor.Error as e:
            print(f"Erro no banco: {e}")
            return self.conn.close()
        finally:
            cursor.close()