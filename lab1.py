#Из списка удалить элементы, стоящие после максимального и 
#имеющие значение меньше среднего арифметического всех элементов списка.
#Пример: из списка A[5]: 8 6 9 4 5 должен получиться
#список A[3]: 8 6 9 (среднее арифметическое четных элементов
#=(8+6+9+4+5)/5=6.4).
import random

def RandomGenerated():
    n = [random.randint(1, 10) for i in range(5)]
    return n


def InputList():
    try:
        return list(map(int, input().split()))
    except ValueError:
        print("Ошибка введите число")

def IndexElements(n):
    max_element = max(n)
    index_max_element = n.index(max_element)
    average = sum(n) / len(n)
    return index_max_element, average

def Slices(n, index_max_element):
    chapter_one = n[:index_max_element + 1]
    chapter_two = n[index_max_element + 1:]
    return chapter_one, chapter_two

def Filter(chapter_one, chapter_two, average):
    res_filter = [x for x in chapter_two if not (x < average)]
    result = chapter_one + res_filter
    return result

def Output(n, result, average):
    print(f"A[{len(n)}]: {n}")
    print(f"Результат A[{len(result)}]: {result}")
    print(f"Среднее: {average}")

def Main():
    try:
        print("Выберите способ ввода (0) авто-генерация, (1) ввод пользователя")
        choice = input("Ваш выбор: ")

    
        if choice == "0":
            n = RandomGenerated()
        elif choice == "1":
            print("Введите числа через пробел:")
            n = InputList()
        else:
            print("Неверный выбор")  
            return  

        index_max_element, average = IndexElements(n)
        chapter_one, chapter_two = Slices(n, index_max_element)
        result = Filter(chapter_one, chapter_two, average)
        Output(n, result, average)

    except Exception as e:
        print(e)

Main()









