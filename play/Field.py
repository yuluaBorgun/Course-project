import numpy as np
from Default_matrix import *
from Pipe import *

class Field:
    def __init__(self, level):
        """ Инициализация поля с заданным уровнем. """

        self.pipes = []
        self.mega_matrix = []
        self.level_map = level
        self.matrix_size = len(level)

    def create_mega_matrix(self):
        """Создает мега-матрицу из мини-матриц на основе уровня."""

        reset_rotation_matrix()# Сброс состояния матрицы вращения
        print(np.array(rotation_state))
        level_matrix = self.level_map
        horizontal_matrix = [] # Для хранения горизонтальной матрицы текущего столбца
        col = 0

        while col < self.matrix_size:
            print(level_matrix)
            print("Column index:", col)
            for row in range(len(level_matrix[col])):
                block_index = level_matrix[col][row]
                tmp_matrix = self.get_mini_matrix(block_index)
                if len(horizontal_matrix) == 0:
                    horizontal_matrix = tmp_matrix
                else:
                    horizontal_matrix = np.hstack((horizontal_matrix, tmp_matrix))

            if len(self.mega_matrix) == 0:
                self.mega_matrix = horizontal_matrix
            else:
                self.mega_matrix = np.vstack((self.mega_matrix, horizontal_matrix))

            horizontal_matrix = []
            col += 1


    def get_mini_matrix(self, type_of_pipe):
        """Возвращает мини-матрицу в зависимости от типа трубы."""

        if type_of_pipe == 0:
            return empty
        if type_of_pipe == 1:
            return start_matrix
        if type_of_pipe == 2:
            return line_matrix
        if type_of_pipe == 3:
            return angle_matrix
        if type_of_pipe == 4:
            return triple_matrix


    def draw_empty_tiles(self, screen):
        """Отрисовывает пустые клетки на экране."""

        screen.fill(WHITE_COLOR)
        pygame.draw.rect(screen, BACKGROUND_COLOR, (0, Y_INDENT, WINDOW_WIDTH, WINDOW_WIDTH), 0)
        for i in range(self.matrix_size):
            for j in range(self.matrix_size):
                block_fill_size = CELL_SIZE - BORDER_SIZE
                pygame.draw.rect(screen, EMPTY_TILE_COLOR, (BORDER_SIZE + i * CELL_SIZE, Y_INDENT + BORDER_SIZE + j * CELL_SIZE, block_fill_size, block_fill_size), 0)

    def draw_pipes(self, screen):
        """Отрисовывает трубы на экране на основе матрицы уровня."""

        level_matrix = self.level_map
        index = 0
        for i in range(self.matrix_size):
            for j in range(self.matrix_size):
                p_type = level_matrix[j][i]
                if p_type != 0:
                    new_pipe = Pipe(BORDER_SIZE + i * CELL_SIZE, Y_INDENT + BORDER_SIZE + j * CELL_SIZE, index, IMAGE_SWITCHER[p_type], p_type)
                    self.pipes.append(new_pipe)
                    new_pipe.draw(screen)
                    index += 1


    def update_frame(self, screen):
        """Обновляет кадры, рисуя все трубы на экране."""

        for pipe in self.pipes:
            pipe.draw(screen)

    def rotate_pipe(self, screen_x, screen_y):
        """Вращает трубу, находящуюся по координатам и обновляет матрицу."""

        # Получаем трубу по заданным экранным координатам
        rotate_pipe: Pipe = self.get_pipe_for_xy(screen_x, screen_y)
        # Проверяем, существует ли труба
        if rotate_pipe != 0:
            # Выполняем вращение и получаем новые координаты
            x, y = rotate_pipe.rotate_self()
            # Обновляем мега-матрицу в соответствии с новым состоянием трубы
            self.rebuild_mega_matrix(x, y, rotate_pipe.type)

    def get_pipe_for_xy(self, x, y):
        """Возвращает трубу по заданным координатам, если таковая найдена."""

        for pipe in self.pipes:
            if pipe.x < x < pipe.x + CELL_SIZE:
                if pipe.y < y < pipe.y + CELL_SIZE:
                    return pipe
        return 0


    def check_win_state(self, solve_matrix):
        """Проверяет, является ли текущее состояние выигрышным, сравнивая с матрицей решения."""

        print(" ")
        print(np.array(solve_matrix))
        print(" ")
        print(self.mega_matrix)
        if np.array_equal(self.mega_matrix, solve_matrix):
            return True
        return False


    def rebuild_mega_matrix(self, pos_x_pixels, pos_y_pixels, matrix_type):
        """Восстанавливает мегаматрицу на основе пиксельных координат и типа матрицы."""

        # Перевод пиксельных координат в индексы
        pos_x = int(pos_x_pixels / CELL_SIZE)
        pos_y = int(pos_y_pixels / CELL_SIZE) - 1

        # Инициализация пустой карты уровня
        self.mega_matrix = []
        horizontal_matrix = []

        col = 0

        while col < self.matrix_size:
            for row in range(len(self.level_map[col])):
                # Проверяем на соответствие координат
                if row == pos_x and col == pos_y:
                    tmp_matrix = self.rotate_sub_matrix(col, row, 1, matrix_type)  # Вращаем матрицу
                else:
                    tmp_matrix = self.rotate_sub_matrix(col, row, 0, self.level_map[col][row])  # Первоначальное состояние

                if len(horizontal_matrix) == 0:
                    horizontal_matrix = tmp_matrix
                else:
                    horizontal_matrix = np.hstack((horizontal_matrix, tmp_matrix))

            # Обновление мегаматрицы
            if len(self.mega_matrix) == 0:
                self.mega_matrix = horizontal_matrix
            else:
                self.mega_matrix = np.vstack((self.mega_matrix, horizontal_matrix))

            horizontal_matrix = []  # Сброс временной матрицы
            col += 1

    def rotate_sub_matrix(self, col, row, rotate_num, matrix_type):
        """Вращает подматрицу в зависимости от типа матрицы и количества вращений."""

        # Получаем тип матрицы
        original_matrix_type = matrix_type
        # Максимальное количество поворотов для этой матрицыи
        max_rotations = self.get_max_rotations(original_matrix_type)
        # Копия оригинальной матрицы
        original_matrix = self.get_mini_matrix(original_matrix_type)
        # Первоначальное состояние всегда оригинальное
        return_matrix = original_matrix
        # Текущее количество поворотов в матрице поворотов
        default_rotate_count = rotation_state[col][row]
        # Добавляем новый поворот, ограничивая количество вращений
        rotate_count = (default_rotate_count + rotate_num) % (max_rotations + 1)

        # Устанавливаем минимальное число поворотов в 1, чтобы избежать пустого результата
        if rotate_count == 0:
            rotate_count = 1

        # Поворачиваем матрицу rotate_count - 1 раз
        for i in range(rotate_count - 1):
            return_matrix = np.rot90(return_matrix)
        # Обновляем состояние вращений
        rotation_state[col][row] = rotate_count

        return return_matrix

    def get_max_rotations(self, original_matrix_type):
        """Определяет максимальное количество вращений в зависимости от типа матрицы.
        Возвращает максимальное количество вращений для заданного типа матрицы."""

        if original_matrix_type == 1 or original_matrix_type == 3 or original_matrix_type == 4:
            return 4
        if original_matrix_type == 2:
            return 2
        return 0

    def light_on(self):
        """Включает свет для труб определённого типа."""

        for pipe in self.pipes:
            if pipe.type == 1:
                pipe.image = CORES_LIGHT[pipe.rotate_state]


def reset_rotation_matrix():
    """Сбрасывает значения матрицы rotation_state к 1."""

    for i in range(len(rotation_state)):
        for j in range(len(rotation_state[i])):
            rotation_state[i][j] = 1