'''import pygame
from pygame.colordict import THECOLORS

pygame.init()
dis=pygame.display.set_mode((800,600))


dis_over=False
while not dis_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            print(event)
            pygame.quit()

    dis.fill(THECOLORS["blue"])
    font=pygame.font.SysFont('couriernew',40)
    text=font.render(('Дикий огурец'),True,THECOLORS['green'])
    x=20
    while x < 500:
        text = font.render(('Дикий огурец'), True, THECOLORS['green'])
        dis.blit(text,(20,x))
        text = font.render(('Дикий огурец'), True, THECOLORS['blue'])
        dis.blit(text, (20, x-10))
        x=x+10
        pygame.time.wait(60)
    pygame.draw.circle(dis,(225,255,255),(357,150),50) #круг1
    pygame.draw.circle(dis,(225,255,255),(357,220),60) #круг2
    pygame.draw.circle(dis,(225,255,255),(357,300),70) #круг3
    pygame.draw.circle(dis,(0,0,0),(357,300),5) # пуговица1
    pygame.draw.circle(dis,(0,0,0),(357,220),5) #пуговица2
    pygame.draw.circle(dis,(0,0,0),(357,260),5) #пуговица3
    pygame.draw.circle(dis, (0, 0, 0), (357, 170), 5) # рот 1
    pygame.draw.circle(dis, (0, 0, 0), (345, 170), 5) # рот 2
    pygame.draw.circle(dis, (0, 0, 0), (370, 170), 5) # рот 3
    pygame.draw.circle(dis, (0, 0, 0), (365, 140), 5) # глаз 1
    pygame.draw.circle(dis, (0, 0, 0), (350, 140), 5) # глаз 2
    pygame.display.update()

quit()
'''



# import pygame
# from pygame.color import THECOLORS
#
# pygame.init()
# dis = pygame.display.set_mode((800, 600))
# pygame.display.set_caption("Олимпийский флаг")
#
# dis_over = False
# clock = pygame.time.Clock()
#
# while not dis_over:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             dis_over = True
#
#     dis.fill(THECOLORS['white'])
#
#
#     pygame.draw.circle(dis, THECOLORS['blue'], (191, 250), 60, 12)
#     pygame.draw.circle(dis, THECOLORS['black'], (322, 255), 60, 12)
#     pygame.draw.circle(dis, THECOLORS['red'], (453, 245), 60, 12)
#
#     pygame.draw.circle(dis, THECOLORS['yellow'], (262, 300), 60, 12)
#     pygame.draw.circle(dis, THECOLORS['green'], (394, 305), 60, 12)
#
#     pygame.display.update()
#
# pygame.quit()
