import random
import math
import pygame
from pygame import gfxdraw



pygame.init()

screen = pygame.display.set_mode((200,200))

screen.fill((0,0,0))

running = True

pygame.draw.rect(screen,(255,255,255),(0,0,200,200),2)
pygame.draw.circle(screen,(255,255,255),(200/2,200/2),100,2)

inside_circle = 0
total = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(10):
    
        posx = random.uniform(0,200)
        posy = random.uniform(0,200)

        total+=1
        if (((posx-100)**2 + (posy-100)**2) < (100**2)):
            # print("inside the circle")
            inside_circle+=1
            pygame.draw.line(screen, (255,0,0), (posx,posy), (posx,posy), 2)
        elif ((posx-100)**2 + (posy-100)**2) > (100**2):
            # print("out of the circle in the square")
            pygame.draw.line(screen, (0,0,255), (posx,posy), (posx,posy), 2)
        else:
            print("OK")
            # pass
            # print("IDK why its breaking")

    print(f"{4*float(inside_circle)/float(total)} value of π")



    pygame.display.flip()
