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
N_PIXELS_PER_FRAME = 3

#3 - Инициализируем окружение pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

#4 - Загружаем элементы: изображения, звуки и т.д.
ballImage = pygame.image.load('images/ball.png')

#5 - Инициализируем переменные
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME

#6 - Бесконечный цикл
while True:
    #7 - Проверяем наличие событий и обрабатываем их
    for event in pygame.event.get():
        # Нажата кнопка "закрыть"? Выходим из pygame и завершаем
        # программу
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #8 - Выполняем действия "в рамках фрейма"
    if (ballX < 0) or (ballX >= MAX_WIDTH):
        xSpeed = -xSpeed

    if (ballY < 0) or (ballY >= MAX_HEIGHT):
        ySpeed =-ySpeed

    # обновляем местоположение мяча, используя скорость в двух
    # направлениях
    ballX = ballX + xSpeed
    ballY = ballY + ySpeed

    #9 - Рисуем все элементы окна
    window.fill(BLACK)

    #10 - Рисуем все элементы окна
    # рисуем мяч на позиции 100 вдоль (x) и 200 вниз по (y)
    window.blit(ballImage, (ballX, ballY))

    #11 - Обновляем окно
    pygame.display.update()

    #12 - Делаем паузу
    clock.tick(FRAMES_PER_SECOND)