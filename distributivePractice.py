import numpy as np

# # 1 ---> Найтu методом Лина корни алгебраического уравнения x^4 - 9x^3 -14x^2 + 50x - 600 = 0


def lins_method(f, x0, x1, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        if abs(x2 - x1) < tol:
            return x2
        x0 = x1
        x1 = x2
    return None  # если корни не нашлись

# объявляем функцию с нашим уравнением
def f(x):
    return x**4 - 9*x**3 - 14*x**2 + 50*x - 600

# ожидаемые к схождению корни
x0 = 5
x1 = 6


root = lins_method(f, x0, x1)

if root is not None:
    print("Корень уравнения:", root)
else:
    print("Корней с такой точностью и количеством итераций не существует")


# 2 ---> Методом последовательных сближений (метод Пикарда) найти решение уравнения y' = y + x, y(0) = 1, h = 0.1 на отрезке [0; 0,3] /// Какой то косяк, list index ouf of range, в шараге работало все



# import numpy as np

# def y_prime(y, x):
#   """Функция, задающая правой частью дифференциального уравнения y' = y + x."""
#   return y + x

# def picard_iteration(y0, x, h, num_iterations):
#   """
#   Реализует метод Пикарда для приближенного решения дифференциального уравнения.
#   """
#   y = [y0]
#   for i in range(num_iterations):
#     y_next = [y0]
#     for j in range(len(x) - 1):
#       # Численное интегрирование методом трапеций
#       integral = 0.5 * h * (y_next[j] + y_prime(y_next[j], x[j]) + y[j] + y_prime(y[j], x[j+1]))
#       y_next.append(y0 + integral)
#     y = y_next
#   return y
# # Параметры
# h = 0.1
# x = np.arange(0, 0.3 + h, h)
# y0 = 1
# num_iterations = 5
# # Выполнение итераций
# y_approx = picard_iteration(y0, x, h, num_iterations)
# # Вывод
# print("Приближенное решение для y(x) с использованием метода последовательных сближений:")
# for i in range(len(x)):
#   print(f"x = {x[i]:.1f}, y = {y_approx[i]:.4f}")

import numpy as np
import matplotlib.pyplot as plt

# Определение функции f(x, y) = y + x
def f(x, y):
    return y + x

# Начальные условия
x0 = 0
y0 = 1
h = 0.1
x_end = 0.3
n_steps = int((x_end - x0) / h)  # Число шагов

# Инициализация массивов для хранения значений
x_values = np.linspace(x0, x_end, n_steps + 1)
y_values = np.zeros(n_steps + 1)
y_values[0] = y0

# Метод последовательных сближений (метод Пикарда)
for n in range(100):  # 100 итераций, для достижения сходимости
    y_new = np.zeros(n_steps + 1)
    for i in range(n_steps):
        # Прибавляем результат предыдущей итерации, начиная с начального условия
        if n == 0:
            # Первоначальная итерация
            y_new[i + 1] = y_values[i] + h * f(x_values[i], y_values[i])

    # Обновляем массив значений
    y_values = y_new

# Вывод результатов
print("x values:", x_values)
print("y values:", y_values)
