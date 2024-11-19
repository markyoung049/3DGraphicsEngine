import pygame
import time
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([1700, 900])
pxarray = pygame.PixelArray(screen)
screen.fill([0, 0, 0])
list = []
print("HERE")
start_time = time.time()
for i in range(1700*  60):
    for j in range(900):
        pxarray[i//1700, j] = (0, i//255, j//255)

pygame.display.flip()
print("--- %s seconds ---" % (time.time() - start_time))

print("DONE")