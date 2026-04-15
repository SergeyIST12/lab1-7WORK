import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def load_matrix(fname):
    """Загрузить матрицу из текстового файла."""
    return np.loadtxt(fname)

def process_matrix(A, K):
    """
    Обработать матрицу A для создания матрицы F на основе заданных условий.
    Выполнить матричные операции и вернуть результаты.
    """
    # Разделить матрицу A на подматрицы B, C, D, E
    n = A.shape[0] // 2
    E = A[:n, :n]
    B = A[:n, n:]
    C = A[n:, n:]
    D = A[n:, :n]

    # Условие: Подсчитать числа в нечетных столбцах B, которые меньше K
    odd_columns_B = B[:, 1::2]
    count_less_than_K = np.sum(odd_columns_B < K)

    # Сумма чисел в четных строках B
    even_rows_B = B[1::2, :]
    sum_even_rows = np.sum(even_rows_B)

    # Создать матрицу F как копию A
    F = A.copy()

    # Проверить условие для модификации F
    if count_less_than_K > sum_even_rows:
        # Поменять местами C и E симметрично
        F[:n, :n], F[n:, n:] = np.flip(C, axis=(0, 1)), np.flip(E, axis=(0, 1))
        print("C и E поменяны симметрично")
    else:
        # Поменять местами B и E несимметрично
        F[:n, n:], F[:n, :n] = E, B
        print("B и E поменяны несимметрично")

    # Вычислить определитель A и сумму диагональных элементов F
    det_A = np.linalg.det(A)
    sum_diag_F = np.trace(F) + np.trace(np.fliplr(F))

    # Выполнить матричные операции на основе условия определителя
    if det_A > sum_diag_F:
        try:
            result = np.linalg.inv(A) @ A.T - K * F
        except np.linalg.LinAlgError:
            result = None
    else:
        G = np.tril(A)  # Нижняя треугольная матрица из A
        result = (np.linalg.inv(A) + G - F.T) * K

    return F, result

def plot_matrix(F):
    """Построить графики матрицы F с использованием трех различных визуализаций."""
    fig = plt.figure(figsize=(15, 5))

    # Тепловая карта F
    plt.subplot(131)
    plt.imshow(F, cmap='viridis')
    plt.colorbar()
    plt.title("Тепловая карта F")

    # График диагональных элементов F
    plt.subplot(132)
    plt.plot(np.diag(F), 'r-', label='Главная диагональ')
    plt.plot(np.diag(np.fliplr(F)), 'b-', label='Побочная диагональ')
    plt.legend()
    plt.title("Диагонали F")

    # 3D-поверхность F
    ax = fig.add_subplot(133, projection='3d')
    x, y = np.meshgrid(range(F.shape[0]), range(F.shape[1]))
    ax.plot_surface(x, y, F, cmap='plasma')
    ax.set_title("3D-поверхность F")

    plt.tight_layout()
    plt.show()

def main():
    try:
        # Ввод K от пользователя
        K = float(input("Введите K: "))

        # Загрузить матрицу A из файла
        A = load_matrix('matrix.txt')

        # Проверить размер матрицы
        if A.shape[0] != A.shape[1] or A.shape[0] % 2 != 0:
            raise ValueError("Матрица должна быть квадратной с четными размерами.")

        print("\nИсходная матрица A:\n", A)

        # Обработать матрицу A для получения F и выполнения операций
        F, result = process_matrix(A, K)
        print("\nПреобразованная матрица F:\n", F)

        if result is not None:
            print("\nРезультат матричных операций:\n", result)

        # Построить графики матрицы F
        plot_matrix(F)

    except Exception as e:
        print(f"\nОшибка: {e}")

if __name__ == "__main__":
    main()
