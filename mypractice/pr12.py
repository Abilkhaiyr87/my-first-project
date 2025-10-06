# class Dog:
#     def __init__(self,name):
#         self.name=name
#     def bark(self):
#         return f"{self.name}:Гав-гав!"
#
#
# my_dog=Dog("шарик")
# sound=my_dog.bark()
# with open("bark.txt","w",encoding="utf-8") as f:
#     f.write(sound)
# print("Собака погавкала, смтори в bark txt")


import pygame

pygame.init()
dis=pygame.display.set_mode((600,600))


dis_over=False
while not dis_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            print(event)
            pygame.quit()

    r=pygame.Rect(200,370,205,250)     #HOUSE
    color=(255,255,255)
    pygame.draw.rect(dis,color,r,0)

    r = pygame.Rect(295, 500, 80, 120)  #DOOR
    color = (150, 75, 0)
    pygame.draw.rect(dis, color, r, 0)

    r = pygame.Rect(220,440, 50, 60)
    color = (173, 220, 230)                       #WINDOW
    pygame.draw.rect(dis, color, r, 0)

    r = pygame.Rect(60, 60, 60, 60)
    color = (255, 172, 2)                        #SUN
    pygame.draw.rect(dis, color, r, 0)

    r = pygame.Rect(480, 500, 20, 120)
    color = (150, 75, 0)                            #TREE
    pygame.draw.rect(dis, color, r, 0)

    r = pygame.Rect(450, 440, 80, 70)                  #foliage
    color = (81, 200, 120)  # TREE
    pygame.draw.rect(dis, color, r, 0)


    r = pygame.Rect(1, 580, 600, 350)
    color = (81, 200, 120)                         #GRASS
    pygame.draw.rect(dis, color, r, 0)

    # r=pygame.Rect(50,50,50,50)
    # color=(255,172,2)
    # p=pygame.draw.circle(surface, color, pas, radius, with=0)


    pygame.display.update()

quit()
