from Dao.AbstractCMSDao import CMSDaoService
from validation.validation import validate_username,validate_password
from models.user import user
from Dao.CMSDaoImple import CMSDaoImplementation

class loginLib:
    dao_service : CMSDaoService = CMSDaoImplementation()
    
    @staticmethod
    def login():
        while True:
            # cancel = input("Cancel login(Y/N):")
            # if cancel:
            #     break
            username = input("Enter username:")
            try:
                if(validate_username(username)):
                    break
            except Exception as e:
                print("Error:",e)
                print("Please try again!")
        
        while True:
            password = input("Enter password:")
            try:
                if(validate_password(password)):
                    break
            except Exception as e:
                print("Error:",e)
                print("Please try again!")

        loginLib.dao_service.verification_login(username, password)