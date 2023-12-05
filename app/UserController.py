from app.UserModel import UserModel

class UserController(UserModel):
    def isBanned(self, username:str) -> bool:
        return self._banCheck(username)
    
    def isAdmin(self, username:str) -> bool:
        return self._adminCheck(username)
    
    def getBanReason(self, username) -> str:
        return self._banReason(username)
    
    def userLogin(self, username:str , password:str) -> bool: 
        return self._login(username, password)

    def userRegister(self, username:str, password:str , confirm_password:str) -> bool:
        self._usernameValidator(username)
        self._passwordValidator(password, confirm_password)
        return self._register(username, password)