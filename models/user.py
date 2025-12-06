class user:
    'user class OOPS applied here'

    def __init__(self,user_id=None, username=None, password=None,role_id=None):
       #constructor overloading (read) // method overloading and method oveerriding(read)
        self.__user_id = user_id
        self.__username=username
        self.__password=password
        self.__role_id=role_id

    #---------------
        #getters
    #----------------
    @property
    def user_id(self):
        return self.__user_id

    @property
    def username(self):
        return self.__username
    

    @property
    def password(self):
        return self.__password

    @property
    def role_id(self):
        return self.__role_id
    
    #display the user table 
    def __str__(self):
        return(
            f"USER ID: {self.__user_id},"
            f"USERNAME: {self.__username},"
            f"PASSWORD: {self.__password},"
            f"ROLE ID: {self.__role_id},"
        )

