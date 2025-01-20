from Consts import *
from Images import *



class Pipe(object):
    def __init__(self, x, y, index, image, pipe_type):
        """
        Инициализация трубы.

        Аргументы:
        x -- координата по оси X
        y -- координата по оси Y
        index -- индекс трубы
        image -- изображение трубы
        pipe_type -- тип трубы
        """

        self.x = x
        self.y = y
        self.index = index
        self.image = image
        self.type = pipe_type
        self.rotate_state = 0

    def draw(self, screen):
        """ Метод рисует прямоугольник, представляющий трубу, и ее изображения на экране.
        Включает доработку размеров с учетом границ."""

        #screen = pygame.display.set_mode((540, 540))
        block_fill_size = CELL_SIZE - BORDER_SIZE
        pygame.draw.rect(screen, BLOCK_TILE_COLOR, (self.x, self.y, block_fill_size, block_fill_size), 0)
        screen.blit(self.image, (self.x, self.y))

    def rotate_self(self):
        """ Метод вращает изображение трубы. """

        if self.type != 1:
            # Поворот картинки для блоков
            orig_rect = self.image.get_rect()
            rot_image = pygame.transform.rotate(self.image, ROTATE_ANGLE)
            rot_rect = orig_rect.copy()
            rot_rect.center = rot_image.get_rect().center
            rot_image = rot_image.subsurface(rot_rect).copy()
            self.image = rot_image
            # Поворачиваем и перезаписываем главную матрицу
        else:
            # Для узлового блока не поворачиваем картинку, а рисуем другую
            self.rotate_state = (self.rotate_state + 1) % 4
            self.image = CORES[self.rotate_state]

        return self.x, self.y