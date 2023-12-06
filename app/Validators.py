from app.Database import Database

class UserValidators(Database):
    def _init_(self, username:str, password:str, confirm_password:str):
        self._username = username
        self._password = password
        self._confirm_password = confirm_password
        
    def usernameValidator(self) -> None:
        if len(self._username) < 4:
            raise Exception("Username must be at least 4 characters")
        if len(self.fetchData(f"SELECT * FROM Users WHERE username = '{self._username}';")) > 0:
            raise Exception("The username already exists")
    
    def passwordValidator(self) -> None:
        if len(self._password) < 8:
            raise Exception("Password must be at least 8 characters")
        if self._password != self._confirm_password:
            raise Exception("Passwords don't match")