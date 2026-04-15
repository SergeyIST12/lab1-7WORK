from math import prod

# Чтение матрицы из файла
def read_matrix(filename):
    return [list(map(int, line.split())) for line in open(filename)]

# Вывод матрицы
def print_matrix(m, name):
    print(f"\n{name}:")
    for row in m:
        print(" ".join(f"{x:4}" for x in row))

#Транспонирование матрицы
def transpose(m):
    return [list(row) for row in zip(*m)]

#Получение индексов для четырех областей матрицы
def get_diagonal_regions(n):
    a1, a2, a3, a4 = [], [], [], []
    for i in range(n):
        for j in range(n):
            if i < j and i + j < n - 1: a1.append((i, j))#Области от1-4
            elif i < j and i + j > n - 1: a2.append((i, j))  
            elif i > j and i + j > n - 1: a3.append((i, j))  
            elif i > j and i + j < n - 1: a4.append((i, j))
    return a1, a2, a3, a4

# Тут идёт построение матрицы F
def build_F(A, K):
    n = len(A)
    F = [row[:] for row in A]  # Копируем матрицу A в F
    a1, a2, a3, _ = get_diagonal_regions(n)

    # Подсчет количества чисел, больших K, в четных столбцах области 1
    count_greater_K = sum(1 for i, j in a1 if j % 2 == 0 and A[i][j] > K)

    # Сумма чисел в нечетных строках области 3
    sum_odd_rows = sum(A[i][j] for i, j in a3 if i % 2 == 1)

     # Проверяется условия
    if count_greater_K > sum_odd_rows:
        print("\nУсловие выполнено: количество чисел, больших K, в четных столбцах области 1 больше суммы чисел в нечетных строках области 3.")
        print("Выполняется симметричная замена областей 1 и 3...")
        for (i1, j1), (i3, j3) in zip(a1, a3[::-1]):
            F[i1][j1], F[i3][j3] = F[i3][j3], F[i1][j1]
    else:
        print("\nУсловие не выполнено: количество чисел, больших K, в четных столбцах области 1 меньше или равно сумме чисел в нечетных строках области 3.")
        print("Выполняется несимметричная замена областей 2 и 3...")
        for (i2, j2), (i3, j3) in zip(a2, a3):
            F[i2][j2], F[i3][j3] = F[i3][j3], F[i2][j2]
    return F, count_greater_K, sum_odd_rows

# Вычисление выражения A * F - K * A^T
def compute_result(A, F, K):
    n = len(A)
    A_T = transpose(A)  # Транспонированная матрица A
    F_T = transpose(F)  # Транспонированная матрица F

    # Умножение матриц A и F
    AF = [[sum(A[i][k] * F[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

    # Умножение матрицы A^T на K
    KAT = [[K * A_T[i][j] for j in range(n)] for i in range(n)]

    # Вычитание матриц
    result = [[AF[i][j] - KAT[i][j] for j in range(n)] for i in range(n)]

    return result

K = int(input("Введите K: "))
A = read_matrix("matrix.txt")

# Формирование матрицы F
F, count_greater_K, sum_odd_rows = build_F(A, K)

# Вычисление результата выражения
R = compute_result(A, F, K)

print_matrix(A, "Исходная матрица A")
print(f"\nКоличество чисел, больших K, в четных столбцах области 1: {count_greater_K}")
print(f"Сумма чисел в нечетных строках области 3: {sum_odd_rows}")
print_matrix(F, "Матрица F после замены")
print_matrix(R, "Результат выражения A * F - K * A^T")
