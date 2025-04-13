import pygame
pygame.init()  # обязательная каманда people
window_size = (500, 500)
screen = pygame.display.set_mode(window_size)  # создание экрана(окна) с размера 300x300
pygame.display.set_caption("БАСУХА В ДЕЛЕ РОДНЫЕ")  # название окна
backgound_color = (255, 255, 255)  # цвет
clock = pygame.time.Clock()  # создание игровово таймера
while True:  # игрововй таймер
    clock.tick(40)  # частота обновления таймераааааа
    screen.fill(backgound_color)
    pygame.draw.line(screen,(0,0,0),[10,30],[290,15],3)
    for event in pygame.event.get():  # проходимся по событиям
        if event.type == pygame.QUIT:  # если нажали на крестик
            pygame.QUIT()  # выйти из ГОЙДА
    pygame.display.update() #ОБНОВЛЕНИЕ ДИСПЛЕЯ