from enum import Enum
import pygame


class Images(Enum):
    start1 = pygame.image.load('pictures/start1.jpg')
    start2 = pygame.image.load('pictures/start2.jpg')
    start3 = pygame.image.load('pictures/start3.jpg')
    start4 = pygame.image.load('pictures/start4.jpg')

    start1_light = pygame.image.load('pictures/start1-light.jpg')
    start2_light = pygame.image.load('pictures/start2-light.jpg')
    start3_light = pygame.image.load('pictures/start3-light.jpg')
    start4_light = pygame.image.load('pictures/start4-light.jpg')

    line = pygame.image.load('pictures/line.jpg')
    angle = pygame.image.load('pictures/angle.jpg')
    triple = pygame.image.load('pictures/triple.jpg')

    alpha_fill = pygame.image.load('pictures/alpha_fill.png')

IMAGE_SWITCHER = {
    1: Images.start1.value,
    2: Images.line.value,
    3: Images.angle.value,
    4: Images.triple.value,
}

CORES = {
    0: Images.start1.value,
    1: Images.start2.value,
    2: Images.start3.value,
    3: Images.start4.value,
}

CORES_LIGHT = {
    0: Images.start1_light.value,
    1: Images.start2_light.value,
    2: Images.start3_light.value,
    3: Images.start4_light.value,
}