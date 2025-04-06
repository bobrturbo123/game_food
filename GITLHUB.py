import pygame
import random
class Sprites:
    def __init__(self,name_image, x, y, width, height):#конструктор.Создание свойств
        self.image = pygame.image.load(name_image)# создание картинки
        self.image=pygame.transform.scale(self.image,(width,height))
        self.rect=self.image.get_rect()# создание прям по границам картинки

        self.rect.x=x
        self.rect.y = x

    def draw_image(self): #МЕТОД!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        screen.blit(self.image, (self.rect.x,self.rect.y)) #это отрисовка картинок на координатах x и y


    def colide_food(self,f):
      if self.rect.colliderect(f.rect) == True:
          print("ggg")

    def move_food(self): #ПОСТОЯННОЕ ДВИЖЕНИЕ ВНИЗ
        self.rect.y += 3
        if self.rect.y > 650:
            self.rect.y = 0


    def move_plate(self):#метод!!!!!!!!!!!!!!!!!!!!
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 10
        elif keys[pygame.K_RIGHT]:
            self.rect.x += 10


pygame.init()  # обязательная каманда people
window_size = (1280, 720)
life = 3
screen = pygame.display.set_mode(window_size)  # создание экрана(окна) с размера 300x300
pygame.display.set_caption("БАСУХА В ДЕЛЕ РОДНЫЕ")  # название окна
backgound_color = (255, 255, 255)  # цвет
clock = pygame.time.Clock()  # создание игровово таймера
zov1 = random.randint(-300,0)
zov2 = random.randint(-300,0)
zov3 = random.randint(-300,0)
zov4 = random.randint(-300,0)
zov5 = random.randint(-300,0)
plate=Sprites('plate.png', 490,620, 330, 98)
fon=Sprites("kitchen.jpg",0,0,1280,720)
food1=Sprites("food1.png",100,zov1,64,64)
food2=Sprites("food2.png",500,zov2,64,64)
food3=Sprites("food3.png",700,zov3,64,64)
food4=Sprites("food4.png",800,zov4,64,64)
food5=Sprites("food5.png",1200,zov5,64,64)
food_list = [food1,food2,food3,food4,food5]
while True:  # игрововй таймер
    clock.tick(40)  # частота обновления таймераааааа
    fon.draw_image()
    for i in food_list:
        i.draw_image()
        i.move_food()
        i.colide_food(plate)
    plate.draw_image()
    plate.move_plate()
    for event in pygame.event.get():  # проходимся по событиям
        if event.type == pygame.QUIT:  # если нажали на крестик
            pygame.QUIT()  # выйти из ГОЙДА
    pygame.display.update() #ОБНОВЛЕНИЕ ДИСПЛЕЯ

