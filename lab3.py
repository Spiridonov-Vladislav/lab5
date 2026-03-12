import os
import csv

# Директория кол-во файлов
def CountDirectory():
    file = os.listdir()

    count = 0
    for i in file:
        count += 1
    return count

# Добовляет данные в словарь
def CsvFile():
    data = []

    with open("data.csv", "r") as f:
        reader = csv.DictReader(f)
        for i in reader:
            data.append(i)

    return data

# Функуия для сортировки данных по строке
def SortString(data):
    sorted_data_string = sorted(data, key=lambda x: x["result"])
    return sorted_data_string

# Функция для сортировки данных по числу
def SortInt(data):
    sorted_data_Integer = sorted(data, key=lambda x: int(x["duration_min"]))
    return sorted_data_Integer

# Функция с условием
def Filter(data):
    result = [x for x in data if int(x["duration_min"]) < 50]
    return result

# Сохранение данных в фаил
def SaveTOFile(count, data, sorted_data_String, sorted_data_Integer, result):
    with open("lab3.txt", "w") as f:
        f.write(f"\nКол-во файлов в директории {count}\n")

        f.write(f"\nДанные в словаре\n")
        for i in data:
            f.write(f"{i['id']}, {i['nickname']}, {i['game']}, {i['date']}, {i['start_time']}, {i['end_time']}, {i['duration_min']}, {i['result']}\n")
        
        f.write(f"\nОтсортированные данные по строке\n")
        for i in sorted_data_String:
            f.write(f"{i['id']}, {i['nickname']}, {i['game']}, {i['date']}, {i['start_time']}, {i['end_time']}, {i['duration_min']}, {i['result']}\n")
        
        f.write(f"\nОтсортированные данные по числу\n")
        for i in sorted_data_Integer:
            f.write(f"{i['id']}, {i['nickname']}, {i['game']}, {i['date']}, {i['start_time']}, {i['end_time']}, {i['duration_min']}, {i['result']}\n")
        
        f.write(f"\nОтсортированные данные по числу")
        for i in sorted_data_Integer:
            f.write(f"{i['id']}, {i['nickname']}, {i['game']}, {i['date']}, {i['start_time']}, {i['end_time']}, {i['duration_min']}, {i['result']}\n")
        
        f.write(f"\nОтсортированные данные с условием меньше 50\n")
        for i in result:
            f.write(f"{i['id']}, {i['nickname']}, {i['game']}, {i['date']}, {i['start_time']}, {i['end_time']}, {i['duration_min']}, {i['result']}\n")

# Добовление новых данных
def AddNewData():
    id_data = int(input("Введите id: "))
    nickname = input("Введите ник: ")
    game = input("Введите игру: ")
    date = input("Введите дату: ")
    start_time = input("Введите время начала: ")
    end_time = input("Введите время окончания: ")
    duration_min = int(input("Введите длительность (мин): "))
    result = input("Введите результат: ")

    with open("data.csv", "a", newline="") as f:
        fieldnames = ["id", "nickname", "game", "date",
                      "start_time", "end_time", "duration_min", "result"]

        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writerow({
            "id": id_data,
            "nickname": nickname,
            "game": game,
            "date": date,
            "start_time": start_time,
            "end_time": end_time,
            "duration_min": duration_min,
            "result": result
        })


def Main():
    count = CountDirectory()
    my_data = CsvFile()
    sort_string = SortString(my_data)

    sort_integer = SortInt(my_data)
    filter = Filter(my_data)
    SaveTOFile(count, my_data, sort_string, sort_integer, filter)

    answer = input("Добавить новую запись? y/n: ")

    if answer == "y":
        AddNewData()

Main()