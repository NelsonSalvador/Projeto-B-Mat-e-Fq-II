import pygame
import math
import numpy


pygame.init()

WIDTH = 720
HEIGHT = 600

#Parametros da simulação
gravidade = 7.8
massa = 1.0
angulo = 60.0
velocidade = 155.0
lastvel = velocidade
viscosidade = 0.005
t = 0.5

posX = 0.0
posY = 0.0
lastPosX = posX
lastPosY = posY

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('My Game')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 25)
YELLOW = (255, 255, 0)

SCREEN.fill(BLUE)
pygame.display.flip()

print("Firing at " + str(angulo) + " degrees, at " + str(velocidade) + "m/s./n")
print("Viscosity is " + str(viscosidade) + ", gravity is " + str(gravidade))

drag = viscosidade * velocidade ** 2

VX = float(velocidade * math.cos(math.radians(angulo)))
VY = float(velocidade * math.sin(math.radians(angulo)))
ax = float(-(drag * math.cos(math.radians(angulo)) / massa))
ay = float(-gravidade - (drag *  math.sin(math.radians(angulo))))

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        pygame.draw.line(SCREEN, WHITE, (50, 560), (700, 560), 1)
        pygame.draw.line(SCREEN, WHITE, (50, 50), (50, 560), 1)

        pygame.event.get()
        ms = pygame.mouse.get_pressed()
        if ms[0]:
            SCREEN.fill(BLUE)
            seet = input("->")
            words = seet.split()

            if words[1] == 'speed':
                velocidade = float(words[2])
            elif words[1] == 'angle':
                angulo = float(words[2])
                velocidade = lastvel
            elif words[1] == 'gravity':
                gravidade = float(words[2])
                velocidade = lastvel
            else:
                print("Invalid Input")
                velocidade = lastvel

            print("Firing at " + str(angulo) + " degrees, at " + str(velocidade) + "m/s./n")
            print("Viscosity is " + str(viscosidade) + ", gravity is " + str(gravidade))


            drag = viscosidade * velocidade ** 2
            VX = float(velocidade * math.cos(math.radians(angulo)))
            VY = float(velocidade * math.sin(math.radians(angulo)))
            ax = float(-(drag * math.cos(math.radians(angulo)) / massa))
            ay = float(-gravidade - (drag *  math.sin(math.radians(angulo))))
            posX = 0.0
            posY = 0.0
            lastPosX = posX
            lastPosY = posY
            pygame.display.flip()
        while (posY >= 0):
            
            VX = VX + t * ax
            VY = VY + t * ay

            posX = float(posX + t * VX)
            posY = float(posY + t * VY)
            
            velocidade = numpy.sqrt(VX ** 2 + VY ** 2)
            drag = viscosidade * velocidade ** 2
            ax = float(-(drag * math.cos(math.radians(angulo)) / massa))
            ay = float(-gravidade - (drag *  math.sin(math.radians(angulo))))
            

             

            if posY >= 0.0:
                pygame.draw.circle(SCREEN, YELLOW, (round(posX + 50.0), round(560.0 - posY)), 3)
                pygame.draw.line(SCREEN, WHITE, (round(posX + 50.0), round(560.0 - posY)), (round(lastPosX + 50.0), round(560.0 - lastPosY)), 1)
            else:
                #posX = -(velocidade * velocidade * math.sin(math.radians(2 * angulo))) / -gravidade
                pygame.draw.circle(SCREEN, GREEN, (round(posX + 50.0), 560), 6)
                pygame.draw.line(SCREEN, WHITE, (round(posX + 50.0), round(560.0)), (round(lastPosX + 50.0), round(560.0 - lastPosY)), 1)

            lastPosX = posX
            lastPosY = posY

            pygame.draw.rect(SCREEN, RED, (600, 10, 100, 50), 1)
        
        pygame.display.flip()

pygame.quit()