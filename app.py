from repository.user_repository import user_repository
from model.user import userEntity



if __name__=="__main__":
    user = userEntity("Lucas",123)
    user_repository().saveUser(user)