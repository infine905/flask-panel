from app.Models import UserModel, SystemModel
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
        Validator.usernameValidator()
        Validator.passwordValidator()
        return self._register(username, password)
    
    def hasSub(self, username:str) -> bool:
        return self._sub(username) > 0
    
    def getSub(self, username:str) -> int:
        return self._sub(username)

class SystemController(SystemModel):
    def getOnlineStatus(self) -> bool:
        return self._onlineStatus()
    
    def getVersion(self) -> str:
        return self._version()
    
    def getUserCount(self) -> int:
        return self._userCount()
    
    def getLatestUser(self) -> str:
        return self._latestUser()