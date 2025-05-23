#1 osa
import pygame
import sys
pygame.init()
lGreen=[153,255,153]
lBlue=[153,204,255]

ekraani_pind=pygame.display.set_mode((640, 480))
ekraani_pind.fill( lGreen )
pygame.display.set_caption("Esimine mäng")

gameover= False

while not gameover:
    youWin=pygame.image.load("bee_image.png")
    youWin=pygame.transform.scale(youWin,[300,200])
    ekraani_pind.blit(youWin, [180,100])

    pygame.display.flip()
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            sys.exit()
pygame.quit()

#2 osa
import pygame
import random
import sys

pygame.init()

r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
varv = [r, g, b]
lGreen = [153, 255, 153]

pind = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Juhuslikud kujundid")
pind.fill(lGreen)

for i in range(1, 10):
    x = random.randint(0, 620)
    y = random.randint(0, 460)
    pygame.draw.rect(pind, varv, [x, y, 20, 20])

pygame.display.flip()

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

pygame.quit()

#3 osa

import pygame
import sys
import random

pygame.init()

red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]

pind = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Majake")
pind.fill(lGreen)

def drawHouse(x, y, width, height, screen, color):
    points = [
        (x, y - (3/4.0) * height),      # katuse tipp
        (x, y),                         # vasak alumine nurk
        (x + width, y),                 # parem alumine nurk
        (x + width, y - (3/4.0) * height),  # parem katuse äär
        (x + width / 2.0, y - height),  # katuse harja punkt
        (x, y - (3/4.0) * height)       # vasak katuse äär uuesti
    ]
    lineThickness = 3
    pygame.draw.lines(screen, color, False, points, lineThickness)

drawHouse(100, 400, 300, 400, pind, red)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()