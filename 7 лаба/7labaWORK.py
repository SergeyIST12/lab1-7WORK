import tkinter as tk
from tkinter import scrolledtext
from itertools import permutations

# Часть 1: Формирование всех возможных вариантов обхода точек
def algorithmic_method(points):
    """Алгоритмический метод формирования всех перестановок."""
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
    """Метод с использованием itertools.permutations."""
    return list(permutations(points))

# Часть 2: Ограничение и целевая функция
def calculate_distance(path):
    """Вычисление суммарного расстояния для заданного пути."""
    distance = 0
    for i in range(len(path) - 1):
        x1, y1 = path[i]
        x2, y2 = path[i + 1]
        distance += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance

def optimized_method(points, min_distance, max_total_distance):
    """
    Оптимизированный метод с ограничениями:
    - Минимальное расстояние между соседними точками.
    - Максимальная суммарная длина пути.
    """
    all_paths = python_method(points)
    optimal_paths = []
    for path in all_paths:
        # Проверка минимального расстояния между соседними точками
        valid = True
        for i in range(len(path) - 1):
            x1, y1 = path[i]
            x2, y2 = path[i + 1]
            if ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 < min_distance:
                valid = False
                break
        if valid and calculate_distance(path) <= max_total_distance:
            optimal_paths.append((path, calculate_distance(path)))
    return optimal_paths

# Функция для обработки нажатия кнопки
def calculate_paths():
    try:
        # Получение данных из текстового поля
        input_text = input_field.get("1.0", "end-1c").strip()
        lines = input_text.split("\n")
        K = int(lines[0].strip())  # Количество точек
        points = [tuple(map(float, line.split())) for line in lines[1:]]

        if len(points) != K:
            output_field.delete("1.0", "end")
            output_field.insert("1.0", "Ошибка: Количество точек не соответствует введенному числу!")
            return

        # Вычисление всех путей
        all_paths_algo = algorithmic_method(points)
        all_paths_python = python_method(points)

        # Вычисление оптимальных путей
        min_distance = 1.5
        max_total_distance = 10.0
        optimal_paths = optimized_method(points, min_distance, max_total_distance)

        # Формирование результата
        result = (
            f"Все возможные пути ({len(all_paths_algo)}):\n"
            + "\n".join(str(path) for path in all_paths_algo)
            + f"\n\nОптимальные пути ({len(optimal_paths)}):\n"
            + "\n".join(f"{i}) Путь: {path}, Длина: {distance:.2f}" for i, (path, distance) in enumerate(optimal_paths, 1))
        )

        # Вывод результата в текстовое поле
        output_field.delete("1.0", "end")
        output_field.insert("1.0", result)
    except Exception as e:
        output_field.delete("1.0", "end")
        output_field.insert("1.0", f"Ошибка: {str(e)}")

# Создание главного окна
root = tk.Tk()
root.title("Обход точек на плоскости")

# Окно ввода
input_label = tk.Label(root, text="Введите количество точек и их координаты\n(формат: K\nx1 y1\nx2 y2 ...):",
                       justify="left", font=("Arial", 12))  # Используем justify для выравнивания
input_label.pack(pady=10)

input_field = tk.Text(root, height=10, width=50)
input_field.pack(pady=5)

# Кнопка для запуска вычислений
calculate_button = tk.Button(root, text="Вычислить", command=calculate_paths)
calculate_button.pack(pady=10)

# Окно вывода с прокруткой
output_label = tk.Label(root, text="Результат:", font=("Arial", 12))
output_label.pack(pady=5)
output_field = scrolledtext.ScrolledText(root, height=15, width=70)
output_field.pack(pady=5)

# Запуск главного цикла
root.mainloop()
# Создание главного окна
root = tk.Tk()
root.title("Обход точек на плоскости")

# Окно ввода
input_label = tk.Label(root, text="Введите количество точек и их координаты (формат: K\nx1 y1\nx2 y2 ...):")
input_label.pack(pady=5)
input_field = tk.Text(root, height=10, width=50)
input_field.pack(pady=5)

# Кнопка для запуска вычислений
calculate_button = tk.Button(root, text="Вычислить", command=calculate_paths)
calculate_button.pack(pady=10)

# Окно вывода с прокруткой
output_label = tk.Label(root, text="Результат:")
output_label.pack(pady=5)
output_field = scrolledtext.ScrolledText(root, height=15, width=70)
output_field.pack(pady=5)

# Запуск главного цикла
root.mainloop()
