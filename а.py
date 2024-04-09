import pygame
import time
import random

pygame.init()

# Установка размеров экрана
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Размер блока и скорость
block_size = 20
speed = 20

# Шрифт
font = pygame.font.SysFont(None, 25)

# Функция отрисовки змейки
def snake(block_size, snakeList):
    for XnY in snakeList:
        pygame.draw.rect(screen, white, [XnY[0], XnY[1], block_size, block_size])

# Основная функция игры
def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = width / 2
    lead_y = height / 2

    change_x = 0
    change_y = 0

    snakeList = []
    snakeLength = 1

    randAppleX = round(random.randrange(0, width - block_size) / block_size) * block_size
    randAppleY = round(random.randrange(0, height - block_size) / block_size) * block_size

    while not gameExit:
        while gameOver == True:
            screen.fill(black)
            message("Игра окончена, Нажмите C чтобы сыграть снова или Q чтобы выйти", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    change_x = -block_size
                    change_y = 0
                elif event.key == pygame.K_RIGHT:
                    change_x = block_size
                    change_y = 0
                elif event.key == pygame.K_UP:
                    change_y = -block_size
                    change_x = 0
                elif event.key == pygame.K_DOWN:
                    change_y = block_size
                    change_x = 0

        if lead_x >= width or lead_x < 0 or lead_y >= height or lead_y < 0:
            gameOver = True

        lead_x += change_x
        lead_y += change_y

        screen.fill(black)
        pygame.draw.rect(screen, red, [randAppleX, randAppleY, block_size, block_size])

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snake(block_size, snakeList)

        pygame.display.update()

        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(0, width - block_size) / block_size) * block_size
            randAppleY = round(random.randrange(0, height - block_size) / block_size) * block_size
            snakeLength += 1

        clock.tick(speed)

    pygame.quit()
    quit()

# Функция отображения текста на экране
def message(msg, color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [width / 2 - screen_text.get_width() / 2, height / 2 - screen_text.get_height() / 2])

clock = pygame.time.Clock()
gameLoop()