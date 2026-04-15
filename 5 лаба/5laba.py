"""Задание состоит из двух частей. 
1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов) и целевую функцию для нахождения оптимального  решения. 
Вариант 14. На плоскости задано К точек. Сформировать все возможные варианты обхода этих точек."""


import timeit
from itertools import permutations

# Часть 1: Формирование всех возможных вариантов обхода точек
def algorithmic_method(points):
    """Алгоритмический метод формирования всех перестановок"""
    result = [[]]
    for _ in range(len(points)):
        temp = []
        for path in result:
            for point in points:
                if point not in path:
                    temp.append(path + [point])
        result = temp
    return result

def python_method(points):
    """Метод с использованием itertools.permutations"""
    return list(permutations(points))

# Часть 2: Ограничение и целевая функция
def calculate_distance(path):
    """Вычисляем суммарное расстояние для заданного пути"""
    distance = 0
    for i in range(len(path) - 1):
        x1, y1 = path[i]
        x2, y2 = path[i + 1]
        distance += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance

def optimized_method_with_min_distance(points, min_distance):
    """
    Оптимизированный метод с одним ограничением:
    Минимальное расстояние между соседними точками.
    1. zip работает быстро, так как он создает итератор (а не копирует данные). Это особенно важно при работе с большими списками точек.
2. Используя zip, можно легко проверить условие для всех пар соседних точек с помощью генератора

    """
    valid_paths = []
    for path in python_method(points):
#all проверяет все значения :
#Генератор создает последовательность булевых значений (True или False) для каждой пары соседних точек.
#Функция all проверяет, что все значения в этой последовательности равны True.

        if all(
            ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 >= min_distance
            for (x1, y1), (x2, y2) in zip(path, path[1:])
        ):
            valid_paths.append((path, calculate_distance(path)))
    return valid_paths

# Ввод данных
K = 4  # Количество точек
points = [(1, 1), (2, 3), (3, 2), (4, 4)]  #координаты точек

# Часть 1: Сравнение времени выполнения двух методов
print("Часть 1: Все возможные варианты обхода точек")
all_paths_algo = algorithmic_method(points)
all_paths_python = python_method(points)

print(f"Алгоритмический метод: {len(all_paths_algo)} путей")
for path in all_paths_algo:
    print(path)
print(f"Метод с itertools.permutations: {len(all_paths_python)} путей")
for path in all_paths_python:
    print(path)

time_algo = timeit.timeit(lambda: algorithmic_method(points), number=1000)
time_python = timeit.timeit(lambda: python_method(points), number=1000)

print("\nСравнение времени выполнения:")
print(f"Алгоритмический метод: {time_algo:.6f} секунд")
print(f"Метод с itertools.permutations: {time_python:.6f} секунд")
print("Быстрее -", "алгоритмический метод" if time_algo < time_python else "метод itertools.permutations")

# Часть 2: Оптимизация с одним ограничением
min_distance = 1.5  # Минимальное расстояние между соседними точками

optimal_paths = optimized_method_with_min_distance(points, min_distance)
print("\nЧасть 2: Оптимизированные пути с ограничением на минимальное расстояние")
if optimal_paths:
    print(f"Найдено {len(optimal_paths)} оптимальных путей:")
    for i, (path, distance) in enumerate(optimal_paths, 1):
        print(f"{i}) Путь: {path}, Длина: {distance:.2f}")
else:
    print("Оптимальных путей не найдено.")
