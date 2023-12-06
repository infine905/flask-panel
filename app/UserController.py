from app.UserModel import UserModel
from app.Validators import UserValidators

class UserController(UserModel):
    def getIdByName(self, username:str) -> str:
        return self._idByName(username)
    
    def isBanned(self, username:str) -> bool:
        return self._banCheck(username)
    
    def isAdmin(self, username:str) -> bool:
        return self._adminCheck(username)
    
    def getBanReason(self, username) -> str:
        return self._banReason(username)
    
    def userLogin(self, username:str , password:str) -> bool: 
        return self._login(username, password)

    def userRegister(self, username:str, password:str , confirm_password:str) -> bool:
        Validator = UserValidators(username, password, confirm_password)
        Validator.usernameValidator(username)
        Validator.passwordValidator(password, confirm_password)
        return self._register(username, password)