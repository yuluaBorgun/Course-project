from operator import truediv

import pygame
import sys
import time
import pygame.freetype
import numpy as np
from Images import *
from Level import *
from Field import  *
from Records import *

USER_EVENT = pygame.USEREVENT + 1
pygame.init()

"""Установка фона, названия ,иконки игры"""
#icon = pygame.image.load('pictures/icon.png').convert_alpha()
#pygame.display.set_icon(icon)

label = pygame.font.Font('fonts/OpenSans-Bold.ttf', 40)


def draw_main_menu():
    """
    Отображает главное меню игры.

    Загружает фон меню и кнопки, затем рисует их на экране.
    Возвращает прямоугольники кнопок для дальнейшего использования.
    """

    pygame.display.set_caption("Меню")
    menu_background = pygame.image.load('pictures/menu_background.png').convert_alpha()

    screen.blit(menu_background, (0, 0))

    button_play = pygame.image.load('pictures/button.png').convert_alpha()
    label_play = label.render('Играть', True, 'black')
    button_play.blit(label_play, (100, 85))
    screen.blit(button_play, (90, 20))
    button_play_rect = button_play.get_rect(topleft=(90, 20))

    button_record = pygame.image.load('pictures/button.png').convert_alpha()
    label_record = label.render('Рекорды', True, 'black')
    button_record.blit(label_record, (90, 85))
    screen.blit(button_record, (90, 140))
    button_record_rect = button_record.get_rect(topleft=(90, 140))

    button_ext = pygame.image.load('pictures/button.png').convert_alpha()
    label_ext = label.render('Выход', True, 'black')
    button_ext.blit(label_ext, (90, 85))
    screen.blit(button_ext, (90, 260))
    button_ext_rect =  button_ext.get_rect(topleft=(90, 260))

    return button_play_rect,button_record_rect, button_ext_rect

def draw_difficulty_menu():
    """
    Отображает меню выбора сложности игры.

    Загружает фон меню, создает кнопки для уровней сложности и
    кнопку для возврата в главное меню.

    Возвращает прямоугольники кнопок для дальнейшего использования.
    """

    screen = pygame.display.set_mode((512, 512))
    pygame.display.set_caption("Меню сложности")
    menu_background = pygame.image.load('pictures/menu_background.png').convert_alpha()
    screen.blit(menu_background, (0, 0))

    easy_level_button = pygame.image.load('pictures/button.png').convert_alpha()
    label_ext = label.render('9Х9', True, 'black')
    easy_level_button.blit(label_ext, (140, 85))
    screen.blit(easy_level_button, (90, 20))
    easy_level_button_rect = easy_level_button.get_rect(topleft=(90, 20))

    mean_level_button= pygame.image.load('pictures/button.png').convert_alpha()
    label_ext = label.render('12Х12', True, 'black')
    mean_level_button.blit(label_ext, (120, 85))
    screen.blit(mean_level_button, (90, 140))
    mean_level_button_rect = mean_level_button.get_rect(topleft=(90, 140))

    back_button = pygame.image.load('pictures/button.png').convert_alpha()
    label_ext = label.render('Назад', True, 'black')
    back_button.blit(label_ext, (120, 85))
    screen.blit(back_button, (90, 260))
    back_button_rect = back_button.get_rect(topleft=(90, 260))

    return easy_level_button_rect,mean_level_button_rect,back_button_rect

def draw_record():
    """
    Отображает экран рекордов игры.
    Загружает фон экрана и отображает список рекордов.
    """

    screen = pygame.display.set_mode((512, 512))
    pygame.display.set_caption("Рекорды")
   # menu_background = pygame.image.load('pictures/menu_background.png').convert_alpha()
    #screen.blit(menu_background, (0, 0))

    back_button = pygame.image.load('pictures/button.png').convert_alpha()
    label_ext = label.render('Назад', True, 'black')
    back_button.blit(label_ext, (120, 85))
    screen.blit(back_button, (90, 300))
    back_button_rect = back_button.get_rect(topleft=(90, 300))
    records: Records = Records()

    label_ext = label.render('9x9', True, 'White')
    (y, x) = label_ext.get_size()
    screen.blit(label_ext, (256 - x/2, 10))


    label_num = 0
    for i in range(get_level_count_by_compexity(1)):
       rec = records.get_record(1,i)
       if rec is not None:
           seconds = int(rec / 1000 % 60)
           minutes = int(rec / 60000 % 24)
           out = '{i} : {minutes:02d}:{seconds:02d}'.format(i=i,minutes=minutes, seconds=seconds)
           label_ext = label.render(out, True, 'White')
           screen.blit(label_ext, (30, (label_num +1) * 40))
           label_num += 1  # Увеличиваем номер строки
    label_ext = label.render('12х12', True, 'White')
    (y, x) = label_ext.get_size()
    screen.blit(label_ext, (256 - x/2, (label_num +1) * 40))
    label_num += 1

    # Вывод рекордов 12x12
    for i in range(get_level_count_by_compexity(2)):
        rec = records.get_record(2, i)
        if rec is not None:
            seconds = int(rec / 1000 % 60)
            minutes = int(rec / 60000 % 24)
            out = '{i} : {minutes:02d}:{seconds:02d}'.format(i=i, minutes=minutes, seconds=seconds)
            label_ext = label.render(out, True, 'White')
            screen.blit(label_ext, (30, (label_num + 1) * 40))
            label_num += 1  # Увеличиваем номер строки

    return  back_button_rect

def draw_finisf_menu():
   # text = label.render("GAME OVER", True, 'black')
    #textPos = (165, 320)
    restart_btnPos = (90, 20)
    next_level_btnPos = (90, 140)
    menu_btnPos = (90, 260)

    label_finish = pygame.font.Font('fonts/OpenSans-Bold.ttf', 30)

    label_restart = label_finish.render('Рестарт', True, 'black')
    restart_btn = pygame.image.load('pictures/button.png').convert_alpha()
    restart_btn.blit(label_restart, (90, 85))
    restart_btn_rect = restart_btn.get_rect(topleft=restart_btnPos)
    screen.blit(restart_btn, restart_btnPos)


    label_next = label_finish.render('Следующий', True, 'black')
    next_level_btn = pygame.image.load('pictures/button.png').convert_alpha()
    next_level_btn.blit(label_next, (90, 85))
    next_level_btn_rect = next_level_btn.get_rect(topleft=next_level_btnPos)
    screen.blit(next_level_btn, next_level_btnPos)


    label_next = label_finish.render('В меню', True, 'black')
    menu_btn = pygame.image.load('pictures/button.png').convert_alpha()
    menu_btn.blit(label_next, (90, 85))
    menu_btn_rect = menu_btn.get_rect(topleft=menu_btnPos)
    screen.blit(menu_btn, menu_btnPos)

    return restart_btn_rect, next_level_btn_rect, menu_btn_rect

def main_menu():
    """
    Отображает главное меню игры и обрабатывает взаимодействия пользователя.
    Возвращает соответствующее состояние игры в зависимости от нажатой кнопки.
    """
    screen = pygame.display.set_mode((512, 512))
    button_play_rect, button_record_rect, button_ext_rect = draw_main_menu()
    while True:
        #draw_main_menu()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                print(mouse) # Отладочный вывод позиции мыши
                if button_play_rect.collidepoint(mouse):
                    return DIFFICULTY_MENU # Переход к меню сложности
                if button_record_rect.collidepoint(mouse):
                    return RECORD # Переход к экрану рекордов
                if button_ext_rect.collidepoint(mouse):
                    running = False
                    return -1
            if event.type == pygame.QUIT:
                running = False
                return -1

        pygame.display.update()

def difficulty_menu():
    """
    Отображает меню выбора сложности и обрабатывает взаимодействия пользователя.
    Возвращает соответствующее состояние игры в зависимости от нажатой кнопки.
    """

    easy_level_button_rect, mean_level_button_rect, back_button_rect = draw_difficulty_menu()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if easy_level_button_rect.collidepoint(mouse):
                    return EASY_LEVEL # Переход к легкому уровню
                if mean_level_button_rect.collidepoint(mouse):
                    return MEAN_LEVEL
                if back_button_rect.collidepoint(mouse):
                    return MAIN_MENU  # Возврат в главное меню
        pygame.display.update()

def record():
    back_button_rect = draw_record()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if back_button_rect.collidepoint(mouse):
                    return MAIN_MENU  # Возврат в главное меню
        pygame.display.update()

def Init(complexity, level_number):
    """
    Инициализация уровня и создание поля для игры.
    Создает данные уровня, инициализирует основную доску и отображает пустые клетки и трубы.
    Возвращает матрицу решений уровня и основную доску.
    """
    # Создание данных уровня
    level_data: Level = Level(complexity, level_number) # Инициализация первого уровня
    level_matrix = level_data.level_matrix
    level_solve_matrix = level_data.solve_matrix

    # Создание игрового поля
    main_field: Field = Field(level_matrix)
    main_field.create_mega_matrix() # Создание мега-матрицы для поля
    main_field.draw_empty_tiles(screen)  # Отрисовка пустых клеток на экране
    main_field.draw_pipes(screen)   # Отрисовка труб на экране
    return level_solve_matrix, main_field

def save_time_to_file(minutes, seconds, lvl_num):
    with open('game_results.txt', 'a') as file:
        file.write(f'Level {lvl_num }: {minutes:02d}:{seconds:02d}\n')

def game(complexity):
    """
    Главная функция игры, отвечающая за цикл игры и обработку событий.
    Аргументы:
        complexity: Уровень сложности игры.
    """

    print(f'Starting game with complexity: {complexity}')
    records: Records = Records()
    lvl_size = get_matrix_size_by_complexity(complexity)
    pygame.display.set_mode((lvl_size * CELL_SIZE, (lvl_size + 1) * CELL_SIZE))  # Инициализация игрового окна
    font = pygame.freetype.SysFont(None, 14)
    font.origin = True

    lvls = get_levels_by_complexity(complexity)
    lvl_size = get_matrix_size_by_complexity(complexity)
    print(f'Level size: {lvl_size}')
    lvl_num = 0

    while lvl_num < len(lvls):
        next_lxl = False
        win_game = False
        light_on = False
        level_solve_matrix,main_field = Init(complexity, lvl_num) # Инициализация уровня и поля
        clock = pygame.time.Clock()# Создание объекта часы
        start_time = pygame.time.get_ticks()
        while not next_lxl:
            main_field.draw_empty_tiles(screen) # Отрисовка пустых клеток
            main_field.update_frame(screen)
            ticks = pygame.time.get_ticks() - start_time# Получение прошедшего времени

            seconds = int(ticks / 1000 % 60)
            minutes = int(ticks / 60000 % 24)
            out = '{minutes:02d}:{seconds:02d}'.format(minutes=minutes, seconds=seconds)
            font.render_to(screen, (400, 20), out, pygame.Color('black'))
            pygame.display.flip()
            clock.tick(60)
            finish_result = -1

            # Обработка событий
            for event in pygame.event.get():
                #Выход из игры
                if event.type == pygame.QUIT or  (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                    running = False
                    return -1

                # Поворот трубы
                if event.type == pygame.MOUSEBUTTONDOWN and not win_game:
                    x, y = event.pos
                    main_field.rotate_pipe(x, y) # Поворот трубы
                    win_state = main_field.check_win_state(level_solve_matrix) # Проверка состояния выигрыша
                    print(win_state)

                    # Проверка выигрыша
                    if win_state:
                        win_game = True
                        continue

                if event.type == pygame.MOUSEBUTTONDOWN and win_game and light_on:
                    screen.blit(Images.alpha_fill.value, (0, Y_INDENT, WINDOW_WIDTH, WINDOW_WIDTH))
                    # Запись времени в файл
                    records.save_record(complexity, lvl_num, ticks)
                    finish_result = finish()
                    next_lxl = True
                    if finish_result == -1:
                        return -1 #выход из игры
                    if finish_result == 1:
                        break
                    if finish_result == 2:
                        lvl_num = lvl_num + 1
                    if finish_result == 0:
                        return 0 # В основное меню
                    # Рестарт

                    #end_game = False
                    #light_on = False

                # Вызов подсветки
                if event.type == pygame.MOUSEBUTTONDOWN and win_game:
                    main_field.light_on()
                    light_on = True
                    continue

def finish():
    restart_btn_rect, next_level_btn_rect, menu_btn_rect = draw_finisf_menu()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if restart_btn_rect.collidepoint(mouse):
                    return 1
                if next_level_btn_rect.collidepoint(mouse):
                    return 2
                if menu_btn_rect.collidepoint(mouse):
                    return 0
            if event.type == pygame.QUIT:
                return -1

        pygame.display.update()


def main():
    """Главная функция для запуска меню игры."""

    running = True
    next_menu = 0  # Инициализация переменной со значением константы
    global screen
    pygame.init()
    screen = pygame.display.set_mode((512, 512))
    #button_ext_rect, button_record_rect, button_play_rect = draw_main_menu()

    while running:
        current_menu = next_menu
        print(current_menu)
        if current_menu == MAIN_MENU:
            next_menu = main_menu()
        if current_menu == DIFFICULTY_MENU:
            next_menu = difficulty_menu()
        if current_menu == RECORD:
            next_menu = record()
        if current_menu == EASY_LEVEL:
            game_result = game(1)
            if game_result == -1:
                next_menu = -1
                running = False
            if game_result == 0:
                next_menu = MAIN_MENU
        if current_menu == MEAN_LEVEL:
            game_result = game(2)
            if game_result == -1:
                next_menu = -1
                running = False
            if game_result == 0:
                next_menu = MAIN_MENU
        if current_menu == -1:
            running = False
            break
        if running:
            pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()