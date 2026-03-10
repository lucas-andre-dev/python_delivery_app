from repository.user_repository import user_repository
from model.user import userEntity
class user_service:
    def __init__(self):
        self.repository = user_repository()

    def saveUser(self,user: userEntity):
        name = user.getName()
        password = user.getPassword()
        self.repository.saveUser(name,password)