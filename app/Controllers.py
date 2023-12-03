from app.Models import UserModel

class UserController(UserModel):
    def isAdmin(self, username:str) -> bool:
        return self._adminCheck(username)
    
    def userLogin(self, username:str , password:str) -> bool: 
        return self._login(username, password)

    def userRegister(self, username:str, password:str , confirm_password:str) -> bool:
        self._usernameValidator(username)
        self._passwordValidator(password, confirm_password)
        return self._register(username, password)