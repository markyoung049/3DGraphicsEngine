############################################
# 3D GRAPHICS TEST
############################################

import pygame
import math
import rectangle_class as r
import entity

#######################################################################################################################################
# Initialization
#######################################################################################################################################




########################                                                     <===============================================
# EDIT DIMENSIONS HERE
aspect_ratio = 16/9
screen_height = 100
screen_width = (int(aspect_ratio * screen_height) // 2) * 2 # round up to a integer that's divisible by 2
distance_from_monitor = 0.9 # in m
monitor_width = 0.53
monitor_height = .3
pixel_size = 0.00027604166
middle_point = [int(screen_width / 2), int(screen_height / 2)]
renderDistance = [.1, 1000]
fov = .785

# NOTES: ADD SUPPORT FOR CURVED MONITOR

########################                                                     <===============================================          

 


# pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([screen_width, screen_height])
white = [255, 255, 255]
red = [255, 0, 0]
redPxarray = (255, 0, 0)
black = [0, 0, 0]
screen.fill(black)
running = True

# Create room (in meters)
width = 100
height = 50
length = 200
pillar_width = 10
pillar_length = 20
pillar_location = [100, 200, 50]

# player defaults
player_height = 1.5
player_horizontal_angle = 0 # in degrees
player_vertical_angle = 0
player_location = [0, 1, -5]

# initialize environment
xTriangles = [entity.triangle((0, 0, 0), (5, 0, 0), (0, 5, 0), redPxarray, (0, 0, 5)), entity.triangle((0, 0, 0), (0, 5, 0), (5, 0, 0), redPxarray, (0, 0, 5))]
x = entity.entity(xTriangles)
#y = r.rectangle([0, 3, 5], [0, 3, -3], [0, 0, 5], [0, 0, -3], red)
#z = r.rectangle([3, 3, 5], [3, 3, -3], [3, 0, 5], [3, 0, -3], [0, 0, 255])
entities = [x]


######### NOTES: Make classes for each object, and store a list of all objects to make initialization easier





#######################################################################################################################################
# Main Game Loop
#######################################################################################################################################
left = False
right = False
up = False
down = False
clockwise = False
counterClockwise = False

pxarray = pygame.PixelArray(screen)

player = entity.player(player_location, [player_horizontal_angle, player_vertical_angle])

render = True
while running:

    screen.fill(black)
    # Check user input
    for event in pygame.event.get():
        # if user exits

        if event.type == pygame.QUIT:
            running = False

        # if user holds q, turn left;. if e, turn right, etc.
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_a:
                left = True

            if event.key == pygame.K_d:
                right = True

            if event.key == pygame.K_w:
                up = True

            if event.key == pygame.K_s:
                down = True

            if event.key == pygame.K_q:
                counterClockwise = True

            if event.key == pygame.K_e:
                clockwise = True

        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_a:
                left = False

            if event.key == pygame.K_d:
                right = False

            if event.key == pygame.K_w:
                up = False

            if event.key == pygame.K_s:
                down = False

            if event.key == pygame.K_q:
                counterClockwise = False

            if event.key == pygame.K_e:
                clockwise = False



    # adjust layer angle for turn
    if left:
        player_location[0]= player_location[0] - .1
    if right:
        player_location[0]= player_location[0] + .1
    if down:
        player_location[2]= player_location[2] - .1
    if up:
        player_location[2]= player_location[2] + .1
    if counterClockwise:
        player.setAngle([player.getAngle()[0] + 0.261799, player.getAngle()[1]])
    if clockwise:
        player.setAngle([player.getAngle()[0] - 0.261799, player.getAngle()[1]])

    """

    for i in range(screen_width):
        for j in range(screen_height):
            # Iterate through all objects, and grab the one with lowest distance
            min = "None"
            for k in range(0, len(objects)):
                distance = objects[k].in_bounds(player_location, [player_horizontal_angle, player_vertical_angle], (i, j), distance_from_monitor, pixel_size, middle_point)

                if min == "None":
                    if 0 < distance:
                        pxarray[i, j] = objects[k].get_color()
                        min = distance
                elif 0 < distance < min:
                    pxarray[i, j] = objects[k].get_color()
                    min = distance
                

            
 
    # iterate through pixels

    # set fps
    screen.flip()
    """

    if render: 
        entity.render(entities, player, fov, aspect_ratio, renderDistance, screen, (screen_width, screen_height))

    clock.tick(144)

# NOTES: CONVEX HULL