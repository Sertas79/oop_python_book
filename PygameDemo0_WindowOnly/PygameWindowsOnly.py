# pygame демо 0 - только окно

#1 - Импортируем пакеты
import pygame
from pygame.locals import *
import sys
import random

#2 - Определяем константы
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT

#3 - Инициализируем окружение pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

#4 - Загружаем элементы: изображения, звуки и т.д.
ballimage = pygame.image.load('images/ball.png')

#5 - Инициализируем переменные
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

#6 - Бесконечный цикл
while True:
    #7 - Проверяем наличие событий и обрабатываем их
    for event in pygame.event.get():
        # Нажата кнопка "закрыть"? Выходим из pygame и завершаем
        # программу
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # определяем, щелкну ли пользователь
        if event.type == pygame.MOUSEBUTTONUP:
            # mouseX, mouseY = event.pos
            # Могли бы это сделать при необходимости

            # проверяем, был ли щелчок в пределах прямоугольника мяча
            # Если это так, выбираем случайны образом новое
            # местоположение
            if ballRect.collidepoint(event.pos):
                ballX = random.randrange(MAX_WIDTH)
                ballY = random.randrange(MAX_HEIGHT)
                ballRect = pygame.Rect(ballX, ballY,
                                       BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)


    #8 - Выполняем действия "в рамках фрейма"

    #9 - Рисуем все элементы окна
    window.fill(BLACK)

    #10 - Рисуем все элементы окна
    # рисуем мяч на позиции 100 вдоль (x) и 200 вниз по (y)
    window.blit(ballimage, (ballX, ballY))

    #11 - Обновляем окно
    pygame.display.update()

    #12 - Делаем паузу
    clock.tick(FRAMES_PER_SECOND)