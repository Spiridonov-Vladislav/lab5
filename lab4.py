import csv

# Класс сессии с id и nickname
class BaseSession():
    def __init__(self, id, nickname):
        setattr(self, "id", id)
        setattr(self, "nickname", nickname)

# Класс хранящий результаты сессии
class ResultSession():
    def __init__(self, result):
        setattr(self, "result", result )

# Основной класс, который наследует от BaseSession и ResultSession
class GameSession(BaseSession, ResultSession):
    def __init__(self, id, nickname, game, date, start_time, end_time, duration_min, result):

        # Инициализация классов от которых начледуем
        BaseSession.__init__(self, id, nickname)
        ResultSession.__init__(self, result)

        #Атрибуты сессии
        setattr(self, "game", game )
        setattr(self, "date", date )
        setattr(self, "start_time", start_time )
        setattr(self, "end_time", end_time )
        setattr(self, "duration_min", int(duration_min))

    # Перегрузка оператора __repr__ для наглядного вывода
    def __repr__(self):
        return f"{self.id}, {self.nickname}, {self.game}, {self.date}, {self.start_time}, {self.end_time}, {self.duration_min}, {self.result}"

# Класс колекция  
class GameCollection():
    def __init__(self):
        # Объекты хранящиеся в сессии
        self.session = []

    # Добовление сессий в класс
    def add(self, session):
        self.session.append(session)

    # Получение сессии по индексу и обращене к ней
    def __getitem__(self, index):
        return self.session[index]
    
    # Итератор для обхода сессии
    def __iter__(self):
        self.index = 0
        return self
    
    # Возвращает сессию при итерации
    def __next__(self):
        if self.index >= len(self.session):
            raise StopIteration
        
        value = self.session[self.index]
        self.index += 1
        return value
    
    # Генератор с условием < 50, возвращает сессии которые меньше 50
    def short_session(self):
        for s in self.session:
            if s.duration_min < 50:
                yield s

    # Загружает сессии из файла
    @classmethod
    def load_csv(cls, filename):
        games = cls()

        with open(filename, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:

                session = GameSession(
                    id = int(row["id"]),
                    nickname = row["nickname"],
                    game = row["game"], 
                    date = row["date"],
                    start_time = row["start_time"], 
                    end_time = row["end_time"], 
                    duration_min= int(row["duration_min"]), 
                    result = (row["result"])
                )
                games.add(session)

            return games
        
# Класс для работы с коллекциями
class Utils():
    @staticmethod 
    # Сортирует сессию по длительности
    def sort_by_duration(date):
        return sorted(date, key=lambda x:x.duration_min)

# Загрузка сессии из файла
games_from_file = GameCollection.load_csv("data.csv")
for g in games_from_file:
    print(g)

# Фаил для записи
with open("lab4.txt", "w") as f:  
    f.write("Сессии из CSV:\n")
    for g in games_from_file:
        f.write(repr(g) + "\n")  

    f.write("Данные у условием\n")
    games_from_file = GameCollection.load_csv("data.csv")
    for g in games_from_file.short_session():
        f.write(repr(g) + "\n")

    f.write("Сортироака по длительности\n")
    sorted_session = Utils.sort_by_duration(games_from_file.session)
    for t in sorted_session:
        f.write(repr(t) + "\n")
        

    # Работа с пользователем
    answer = input("Хотите ли вы ввести данные для новой сессии (y/n)? ")

    if answer == "y":
        try:
            user_input = input("Введите данные для новой сессии: ")
            f.write("\nДанные, введённые пользователем:\n")
            f.write(user_input + "\n")

        except Exception as e:
            print(f"Произошла ошибка при записи: {e}")
    else:
        print("Данные для записи пропущены")
                
    
    



