############################################
# 3D GRAPHICS TEST
############################################

import pygame
import math
import rectangle_class as r
import entity
import numpy as np

import time



# Code to be timed



#######################################################################################################################################
# Initialization
#######################################################################################################################################

# Teack average fps
startTime = time.time()
frames = 0


########################                                                     <===============================================
# EDIT DIMENSIONS HERE
aspect_ratio = 16/9
screen_height = 100
screen_width = (int(aspect_ratio * screen_height) // 2) * 2 # round up to a integer that's divisible by 2
distance_from_monitor = 0.9 # in mw
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
pygame.display.set_caption("3D Simulation")
font = pygame.font.Font(None, 20)

blue = (0, 0, 255)
red = (255, 0, 0)
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
player_location = [-3, 1, -15]

# initialize environment
xTriangles = [ entity.triangle((0, 0, 0), (0, 5, 0), (10, 5, 0), red, (0, 0, 5)), entity.triangle((0, 0, 0), (10, 0, 0), (10, 5, 0), red, (0, 0, 5))]
x = entity.entity(xTriangles)

yTriangles = [entity.triangle((0, 0, 0), (0, 0, -10), (0, 5, -10), blue, (0, 0, 5)), entity.triangle((0, 0, 0), (0, 5, -10), (0, 5, 0), blue, (0, 0, 5))]
y = entity.entity(yTriangles)

scene = [x, y]


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

fps = 0

player = entity.player(player_location, [player_horizontal_angle, player_vertical_angle])

render = True
while running:
    pxarray = pygame.PixelArray(screen)
    horizAngle = player.getAngle()[0]
    playerPosition = player.getPosition()
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

    # Rotate space, apply movements, then rotate back
    #print( -.1 * (math.cos(player.getAngle()[0])))
    horizontalRotationMatrix = np.array([   [math.cos(horizAngle), 0, math.sin(horizAngle)],
                                                [0, 1, 0],
                                                [-math.sin(horizAngle), 0, math.cos(horizAngle)]   ])

    playerPosVector = np.array(playerPosition)
    rotatedPosVector = np.dot(horizontalRotationMatrix, playerPosVector)
    rotatedPos = [rotatedPosVector[0], rotatedPosVector[1], rotatedPosVector[2]]


    # In the roptated space, apply the motion
    if left:
        rotatedPos[0] = rotatedPosVector[0] - .1 
    if right:
        rotatedPos[0] = rotatedPosVector[0] + .1  
    if down:
        rotatedPos[2] = rotatedPosVector[2] - .1 
    if up:
        rotatedPos[2]= rotatedPosVector[2] + .1  

    # Rotate the vector back to global space
    rotatedPos = np.array(rotatedPos)
    position = np.dot(horizontalRotationMatrix.T, rotatedPos)
    player.setPosition(position)



    # Rotate space if user does so
    if counterClockwise:
        player.setAngle([player.getAngle()[0] + 0.0261799, player.getAngle()[1]])
    if clockwise:
        player.setAngle([player.getAngle()[0] - 0.0261799, player.getAngle()[1]])

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
    screen.flip()d
    """
    # Render the scene
    screen.lock()
    entity.render(scene, player, fov, aspect_ratio, renderDistance, screen, (screen_width, screen_height))
    del pxarray
    screen.unlock()

    
     # FPS TEST
    if frames == 5:
        # Calcuate the fps
        
        elapsedTime = time.time() - startTime
        fps = 5 / elapsedTime

        frames = 0
        startTime = time.time()

    # Draw the fps counter
    text = font.render(f"{fps:.2f} FPS", True, (0, 255, 0))
    textBox = text.get_rect(center=(35, 20))

    screen.blit(text, textBox)

    frames += 1
    clock.tick(144)


    pygame.display.flip() # update the screen

# NOTES: CONVEX HULL