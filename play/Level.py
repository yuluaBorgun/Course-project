from Levels_matrix import *

class Level:
    """ Класс Level представляет уровень игры и его матрицы. """

    def __init__(self, complexity, level_number):
        """ Инициализация уровня.
              Аргументы: level_number -- номер уровня, который нужно установить."""

        # Получаем все уровни по сложности
        all_levels = get_levels_by_complexity(complexity)
        # Проверка существования уровня
        if level_number < len(all_levels):
            self.num = level_number # Устанавливаем номер текущего уровня
        else:
            self.num = 0 # Уровень по умолчанию

        # Установка матриц уровня и решения
        self.level_matrix = all_levels[self.num][0]
        self.solve_matrix = all_levels[self.num][1]