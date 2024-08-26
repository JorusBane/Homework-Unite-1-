class User:
    def __init__(self,  nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return f'{self.nickname}'
class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        if nickname not in self.users:
            self.users.append(User(nickname, password, age))
        else:
            print(f"Пользователь с таким {nickname} уже существует")

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == password:
                self.current_user = str(user)

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)



# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
# Проверка входа в другой аккаунт
ur.register('valera', 'F8098FM8432423fjm9jmi', 45)
ur.register('Anton', 'qwerty', 16)
print(ur.users)
ur.log_in('vasya_pupkin', 'F8098FM8fjm9jmi')
ur.log_in('valera', 'F8098FM8432423fjm9jmi')
ur.log_in('Anton', 'qwerty')
print(ur.current_user)
