from models.user import User


class UserController:
    def __init__(self):
        self.users = User()

    def create_user(self, name: str) -> str:
        user = User()
        user.name = name
        user.save()

        return user.name

    def list_users(self) -> list[str]:
        user_list = []

        for user in self.users.getAll():
            user_list.append(user.name)

        return user_list

    def user_exists(self, name: str) -> bool:
        user = self.users.findByName(name)

        return (user != None)
