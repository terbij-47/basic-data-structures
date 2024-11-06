import time

class User:

    def __init__(self, nickname, password : int, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname

    def __eq__(self, other):
        if isinstance(other, str):
            return self.nickname == other
        if isinstance(other, User):
            return self.nickname == other.nickname
        return False


class Video:

    def __init__(self, title, duration, *, adult_mode = False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = 0

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'Video(title= "{self.title}", duration= {self.duration}, adult_mode= {self.adult_mode})'

    def __eq__(self, other):
        if isinstance(other, str):
            return self.title == other
        if isinstance(other, Video):
            return self.title == other.title
        return False

    def __contains__(self, item : str):
        return isinstance(item, str) and item.lower() in self.title.lower()


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password : str):
        psw = hash(password)
        for user in self.users:
            if user == nickname and psw == user.password:
                self.current_user = user
                break

    def register(self, nickname, password : str, age):
        for user in self.users:
            if user == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        self.current_user = User(nickname, hash(password), age)
        self.users.append(self.current_user)

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        titles = [video.title for video in self.videos]

        for new_video in args:
            if isinstance(new_video, Video) and new_video.title not in titles:
                self.videos.append(new_video)
                titles.append(new_video.title)

    def get_videos(self, key_word : str):
        res = []
        for video in self.videos:
            if key_word in video:
                res.append(video.title)
        return res

    def watch_video(self, title):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        video = None
        for vid in self.videos:
            if vid == title:
                video = vid
                break

        if video:
            if video.adult_mode and self.current_user.age < 18:
                print('Вам нет 18, пожалуйста, покиньте страницу')
            else:
                while video.time_now < video.duration:
                    time.sleep(1)
                    video.time_now += 1
                    print(video.time_now, sep=' ', end= ' ', flush= True)
                print('Конец видео')
                video.time_now = 0

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

print(v1)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
