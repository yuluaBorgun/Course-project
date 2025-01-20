import numpy as np
import time
from Field import Field

def test_asymptotics_create_mega_matrix():
    """
    Тестирует время выполнения метода create_mega_matrix при увеличении размера уровня.
    """
    sizes = [10, 50, 100, 200]  # Размеры матрицы уровня
    for size in sizes:
        level_matrix = np.ones((size, size))  # Создаем матрицу уровня из 1
        field = Field(level_matrix)

        start_time = time.time()
        field.create_mega_matrix()
        end_time = time.time()

        print(f"Matrix size: {size}x{size}, Time taken: {end_time - start_time:.5f}s")

def test_asymptotics_check_win_state():
    """
    Тестирует время выполнения метода check_win_state при увеличении размера уровня.
    """
    sizes = [10, 50, 100, 200]  # Размеры матрицы
    for size in sizes:
        solve_matrix = np.ones((size, size))  # Решение
        level_matrix = np.ones((size, size))  # Уровень
        field = Field(level_matrix)
        field.create_mega_matrix()  # Генерируем мега-матрицу

        start_time = time.time()
        result = field.check_win_state(solve_matrix)  # Проверяем состояние выигрыша
        end_time = time.time()

        print(f"Matrix size: {size}x{size}, Result: {result}, Time taken: {end_time - start_time:.5f}s")

if __name__ == "__main__":
    print("Testing create_mega_matrix:")
    test_asymptotics_create_mega_matrix()
    print("\nTesting check_win_state:")
    test_asymptotics_check_win_state()
