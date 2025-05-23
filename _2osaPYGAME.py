#1 osa
# import pygame
# import sys
# pygame.init()
# lGreen=[153,255,153]
# lBlue=[153,204,255]

# ekraani_pind=pygame.display.set_mode((640, 480))
# ekraani_pind.fill( lGreen )
# pygame.display.set_caption("Esimine mäng")

# gameover= False

# while not gameover:
#     youWin=pygame.image.load("bee_image.png")
#     youWin=pygame.transform.scale(youWin,[300,200])
#     ekraani_pind.blit(youWin, [180,100])

#     pygame.display.flip()
#     for i in pygame.event.get():
#         if i.type==pygame.QUIT:
#             sys.exit()
# pygame.quit()



#2 osa
import pygame
import sys
pygame.init()

green = (0, 255, 0)
brown = (139, 69, 19)
pink = (255, 153, 255)
red = (255, 0, 0)
sky_blue = (135, 206, 235)
light_green = (153, 255, 153)

# AKen
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Дом с небом и травой")

screen.fill(sky_blue)
pygame.draw.rect(screen, light_green, (0, 350, 640, 130))

# Maja
def drawMaja(x, y, width, height, screen):
    pygame.draw.rect(screen, green, (x, y - height * 0.75, width, height * 0.75))
    roof_points = [
        (x, y - height * 0.75),
        (x + width / 2, y - height),
        (x + width, y - height * 0.75)
    ]
    pygame.draw.polygon(screen, red, roof_points)

# Uks
def drawUks(x, y, width, height, screen):
    door_rect = pygame.Rect(
        x + width * 0.375,
        y - height * 0.5,
        width * 0.25,
        height * 0.5
    )
    pygame.draw.rect(screen, brown, door_rect)

# Aken
def drawAken(x, y, width, height, screen):
    wx = x + width * 0.15
    wy = y - height * 0.35
    size = width * 0.2

    pygame.draw.rect(screen, pink, (wx, wy - size, size, size))
    pygame.draw.rect(screen, (0, 0, 0), (wx, wy - size, size, size), 2)

    pygame.draw.line(screen, (0, 0, 0), (wx + size / 2, wy - size), (wx + size / 2, wy), 2)
    pygame.draw.line(screen, (0, 0, 0), (wx, wy - size / 2), (wx + size, wy - size / 2), 2)

# Chimney
def drawChimney(x, y, width, height, screen):
    chimney_rect = pygame.Rect(
        x + width * 0.65,
        y - height,
        width * 0.08,
        height * 0.25
    )
    pygame.draw.rect(screen, red, chimney_rect)

house_x = 150
house_y = 400
house_width = 300
house_height = 400

drawMaja(house_x, house_y, house_width, house_height, screen)
drawUks(house_x, house_y, house_width, house_height, screen)
drawAken(house_x, house_y, house_width, house_height, screen)
drawChimney(house_x, house_y, house_width, house_height, screen)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# #3 osa
# import pygame
# import sys

# pygame.init()

# ekraanilaius = 640
# ekraanikorgus = 480
# ekraan = pygame.display.set_mode((ekraanilaius, ekraanikorgus))
# pygame.display.set_caption("Ruudustik")

# def joonista_ruudustik(ekraan, ruudu_laius, ruudu_korgus, read, veerud, joone_varv):
#     taust_varv = (200, 255, 200)
#     for rida in range(read):
#         for veerg in range(veerud):
#             x = veerg * ruudu_laius
#             y = rida * ruudu_korgus
#             ruut = pygame.Rect(x, y, ruudu_laius, ruudu_korgus)
#             pygame.draw.rect(ekraan, taust_varv, ruut)  
#             pygame.draw.rect(ekraan, joone_varv, ruut, 1)  

# joonista_ruudustik(ekraan, 20, 20, 24, 32, (255, 0, 0))  

# pygame.display.flip()

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
