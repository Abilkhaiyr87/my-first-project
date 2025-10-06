import pygame, random
from pygame.colordict import THECOLORS

pygame.init()
dis=pygame.display.set_mode((600,600))
pygame.display.set_caption("Рисунок")
font = pygame.font.SysFont(None, 36)

dis_over=False
while not dis_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            dis_over=True


    dis.fill('white')

    counter=1

    for row in range(8):
        for col in range(8):
            x = 30 + col * 70
            y = 20 + row * 70
            r = pygame.Rect(x, y, 50, 50)
            color =random.randint(0,255),random.randint(0, 255),random.randint(0, 255),

            pygame.draw.rect(dis, color, r, width=0)
            text = font.render(str(counter),True,random.randint(0,200))
            text_rect=text.get_rect(center=r.center)
            dis.blit(text, text_rect)
            counter += 1


    pygame.display.update()
pygame.quit()