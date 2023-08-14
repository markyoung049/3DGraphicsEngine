############################################
# 3D GRAPHICS TEST
############################################
import pygame
import math
import rectangle_class as r
#######################################################################################################################################
# Initialization
#######################################################################################################################################




########################                                                     <===============================================
# EDIT DIMENSIONS HERE
aspect_ratio = 16/9
screen_width = 400
screen_height = (int(aspect_ratio * 600) // 2) * 2 # round up to a integer that's divisible by 2
distance_from_monitor = 0.9 # in m
monitor_width = 0.53
monitor_height = .3
pixel_size = 0.00027604166
middle_point = [int(screen_width / 2), int(screen_height / 2)]

# NOTES: ADD SUPPORT FOR CURVED MONITOR

########################                                                     <===============================================          

 


# pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([screen_height, screen_width])
white = [255, 255, 255]
red = [255, 0, 0]
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
player_height = 2
player_horizontal_angle = 0 # in degrees
player_vertical_angle = 0
player_location = [-10, player_height, -10]

# initialize environment
x = r.rectangle([2, 2, 5], [3, 2, 5], [2, 0, 5], [3, 0, 5], [0, 0, 0])
print(x.in_bounds(player_location, [player_horizontal_angle, player_vertical_angle], [0, 0], distance_from_monitor, pixel_size, middle_point))


######### NOTES: Make classes for each object, and store a list of all objects to make initialization easier





#######################################################################################################################################
# Main Game Loop
#######################################################################################################################################
left = False
right = False
up = False
down = False
while running:
    #screen.fill(black)
    # Check user input
    for event in pygame.event.get():
        # if user exits
        if event.type == pygame.QUIT:
            running = False

        # if user holds q, turn left;. if e, turn right, etc.
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_q:
                left = True

            if event.key == pygame.K_e:
                right = True

            if event.key == pygame.K_w:
                up = True

            if event.key == pygame.K_s:
                down = True

        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_q:
                left = False

            if event.key == pygame.K_e:
                right = False

            if event.key == pygame.K_w:
                up = False

            if event.key == pygame.K_s:
                down = False


    # adjust layer angle for turn
    if left:
        player_horizontal_angle = (player_horizontal_angle - 2) % 360
    if right:
        player_horizontal_angle = (player_horizontal_angle + 2) % 360
    if down:
        player_vertical_angle = (player_vertical_angle - 2) % 360
    if up:
        player_vertical_angle = (player_vertical_angle + 2) % 360




    for i in range(screen_height):
        for j in range(screen_width):


            distance = x.in_bounds(player_location, [player_horizontal_angle, player_vertical_angle], (j, i), distance_from_monitor, pixel_size, middle_point)
            
            if distance > 2:
                screen.set_at((i, j), white)

    # iterate through pixels
    

    # set fps
    pygame.display.flip()



# NOTES: CONVEX HULL