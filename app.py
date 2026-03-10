from services.user_service import user_service
from model.user import userEntity



if __name__=="__main__":
    user = userEntity("teste2",123)
    user_service().saveUser(user)
    