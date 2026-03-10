class userEntity:
    def __init__(self,name,password,id=None):
        self.id = id
        self.name = name
        self.password = password
        
    def getName(self):
        return self.name
    
    def getPassword(self):
        return self.password

    def setName(self,name):
        self.name = name

    def setPassword(self,password):
        self.password = password