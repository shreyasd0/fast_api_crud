from models.user_models import user
class user_repository:
    def __init__(self):
        self.users = []
    
    def add_user(self, user: user):
        self.users.append(user)
    
    def get_user(self, id: int):
        for user in self.users:
            if user.id == id:
                return user
        return None
    
    def update_user(self, id: int, name: str, email: str):
        for user in self.users:
            if user.id == id:
                user.name = name
                user.email = email
                return user
        return None
    
    def delete_user(self, id: int):
        for user in self.users:
            if user.id == id:
                self.users.remove(user)
                return True
        return False