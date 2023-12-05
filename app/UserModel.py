from hashlib import md5 as get_hash
from datetime import datetime

from app.Database import Database

class UserModel(Database):     
    def _usernameValidator(self, username:str) -> None:
        if len(username) < 4:
            raise Exception("Username must be at least 4 characters")
        if len(self.fetchData(f"SELECT * FROM Users WHERE username = '{username}';")) > 0:
            raise Exception("The username already exists")
    
    def _passwordValidator(self, password:str , confirm_password:str) -> None:
        if len(password) < 8:
            raise Exception("Password must be at least 8 characters")
        if password != confirm_password:
            raise Exception("Passwords don't match")
        
    def _adminCheck(self, username:str):
        request = f"SELECT admin FROM Users WHERE username = '{username}';"
        query_result = self.fetchOneData(request)
        return bool(query_result[0])
    
    def _banCheck(self, username:str) -> bool:
        request = f"SELECT banned FROM Users WHERE username = '{username}';"
        query_result = self.fetchOneData(request)
        return bool(query_result[0])
    
    def _banReason(self, username:str) -> str:
        request = f"SELECT banreason FROM Users WHERE username = '{username}';"
        return str(self.fetchOneData(request)[0])
    
    def _login(self, username:str, password:str) -> bool:
        request = f"SELECT * FROM Users WHERE username = '{username}' AND password = '{get_hash(password.encode()).hexdigest()}';"
        return len(self.fetchData(request)) > 0
    
    def _register(self, username:str, password:str) -> bool:
        date = datetime.now().strftime("%d %B %Y")
        request = (f"INSERT INTO Users (username, password, admin, registration_date) VALUES (?, ?, ?, ?)", (username, get_hash(password.encode()).hexdigest(), False, date))
        return self.executeData(request)