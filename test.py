import numpy as np
import random as r

print("Выбирите 1 - автогенерация, 2 - ввод с клавиатуры")

select = int(input())
data = set()

if select == 1:
    n, m = int(input()), int(input())
    matrixA = np.random.randint(1, 100, size=(n, m))
elif select == 2:
    matrixA = np.random.randint(1, 20, size=(3, 3))



elementMax = np.max(matrixA)
matrixB = np.round(matrixA / elementMax, 1)

with open("test1111.txt", "w") as f:
    for line in matrixB:
        f.write(str(line) + "\n")


print(f"Исходная матрица \n{matrixA}")
print(f"Изминенная матрица \n {matrixB}")

