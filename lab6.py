from peewee import *
import telebot
from datetime import datetime

db = SqliteDatabase('telegramBot')

class Player(Model):
    nickname = CharField(unique=True)

    class Meta:
        database = db

class GameSession(Model):
    player = ForeignKeyField(Player, backref='games')
    game = CharField()
    data = DateField()
    start_time = TimeField()
    end_time = TimeField()
    duration_min = IntegerField()
    result = CharField()

    class Meta:
        database = db

db.connect()
db.create_tables([Player, GameSession])

bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['help'])
def help(message):
    text = (
        "В данном боте вы можете:\n"
        "Добовлять пользователя /add_user\n"
        "Добовлять данные сессии /add_data\n"
        "Выводить список игроков /output\n"
        "Выводить всю сессию /all_session\n"
        "Очищать добавленные данные /clear\n"
    )
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['add_user'])
def add_user(message):

    args = message.text.split(maxsplit=1)
        
    if len(args) > 1:
        nickname = args[1]
        Player.create(nickname=nickname) 
        bot.send_message(message.chat.id, f"Игрок {nickname} добавлен!")
    else:
        bot.send_message(message.chat.id, "Напишите имя! /add_user имя")

@bot.message_handler(commands=['add_data'])
def add_data(message):
    args = message.text.split()

    if len(args) != 8:
        bot.send_message(
            message.chat.id,
            "Формат:\n/add_data nickname game date start end duration result"
        )
        return

    _, nickname, game, date_str, start_str, end_str, duration, result = args

    # Проверяем игрока
    try:
        player = Player.get(Player.nickname == nickname)
    except Player.DoesNotExist:
        bot.send_message(message.chat.id, "Игрок не найден. Сначала добавь его.")
        return

    # Конвертация даты и времени
    date = datetime.strptime(date_str, "%d.%m.%Y").date()
    start_time = datetime.strptime(start_str, "%H:%M").time()
    end_time = datetime.strptime(end_str, "%H:%M").time()

    GameSession.create(
        player=player,
        game=game,
        data=date,
        start_time=start_time,
        end_time=end_time,
        duration_min=int(duration),
        result=result
    )

    bot.send_message(message.chat.id, "Игровая сессия добавлена!")


# Вывод информации
@bot.message_handler(commands=['output'])
def output(message):
    users = Player.select()

    if users.count() == 0:
        bot.send_message(message.chat.id, "Игроков нет.")
        return
    
    text = "\nСписок игроков\n"
    for user in users:
        text += f"{user.nickname}\n"
        
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['all_session'])
def all_session(message):
    session = GameSession.select().join(Player)

    if session.count() == 0:
        bot.send_message(message.chat.id, "Сессий нет.")
        return
    text = "Все игровые сессии \n\n"

    for s in session:
        text += (
            f"{s.player.nickname}, "
            f"{s.game}, "
            f"{s.data.strftime('%d.%m.%Y')}, "
            f"{s.start_time.strftime('%H:%M')}, "
            f"{s.end_time.strftime('%H:%M')}, "
            f"{s.duration_min}, "
            f"{s.result}\n"
        )
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['clear'])
def clear(message):
    GameSession.delete().execute()
    Player.delete().execute()
    bot.send_message(message.chat.id, "Таблица очищена")

bot.polling(non_stop=True)
