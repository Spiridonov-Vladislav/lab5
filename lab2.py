#Выполнить обработку элементов прямоугольной матрицы A, 
#имеющей N строк и M столбцов. Разделить элементы матрицы 
# на элемент матрицы с наибольшим значением.

import numpy as np
import random

# Ввод размера матрицы
def InputNumber():
    while True:
        try:
            print("Введите 2 числа каждое с новой строки")
            n, m = int(input()), int(input())
            return n, m
        except:
            print("Введите число")
    
# Диапозон генерации элементов матрицы
def RandomInputMatrixElement():
    while True:
        try:
            print("С каго числа по какое будет строиться матрица")
            print("Введите 2 числа каждое с новой строки")
            start, end = int(input()), int(input())
            return start, end
        except:
            print("Введите число")
    
# Создание матрицы
def CreateMatrix(n, m, start, end):
    arr = np.random.randint(start, end, size=(n, m)) 
    print(f"Целевая матрица:\n {arr}")
    return arr
    
# Максимальный элемент матрицы
def MaxValue(arr):
    max_value = np.max(arr)
    return max_value

# Деление матрицы
def FinalMatrix(arr, max_value):
    finalMatrix = arr / max_value
    return finalMatrix

# Округление элементов до 2 знаков
def Round(finalMatrix):
    result = np.round(finalMatrix, 2)
    return result

# Сохранение результатов в фаил
def SaveFile(arr, max_value, result):
    with open("lab2.txt", "w") as f:
        f.write(f"Целевая матрица:\n {str(arr)}")
        f.write(f"\nНаибольшее значение матрицы:\n {str(max_value)}")
        f.write(f"\nФинальная матрица:\n {str(result)}")


def Main():
    # Кол-во строк и столбцоы
    n, m = InputNumber() 
    # Диапозон генерации элементов матрицы
    start, end = RandomInputMatrixElement()
    arr = CreateMatrix(n, m, start, end) 
    max_value = MaxValue(arr)
    print(f"Наибольшее значение матрицы: {max_value}")
    finalMatrix = FinalMatrix(arr, max_value)
    result = Round(finalMatrix)
    
    print(f"Финальная матрица:\n {result}")

    #Сохраняет матрицу в фаил
    SaveFile(arr, max_value, result) 

if __name__ == "__main__":
    Main()