import math
import numpy as np

################################################################################
# Triangle Class
################################################################################
"""
This creates the triangle object which will be the basis of all other entities. They will all just be sets of connected triangles
"""
class triangle:

    # Initialize the triangle
    def __init__(self, pointA, pointB, pointC, color, position):

        self.a = pointA
        self.b = pointB
        self.c = pointC
        self.color = color
        self.position = position

        # Calculate the global position of the triangle vertices
        self.globalA = (pointA[0] + position[0], pointA[1] + position[1], pointA[2] + position[2])
        self.globalB = (pointB[0] + position[0], pointB[1] + position[1], pointB[2] + position[2])
        self.globalC = (pointC[0] + position[0], pointC[1] + position[1], pointC[2] + position[2])




    # Transform the coordinates to the player view
    def toPlayerCoord(self, playerPosition, angle):
        horizAngle = -angle[0]  # angle is negative because rotating in the opposite direction as the player
        vertAngle = -angle[1]   # angle is negative because rotating in the opposite direction as the player

        # Grab object coordinates relative to the player (before rotation)
        playerA = np.array(self.globalA[0] - playerPosition[0], self.globalA[1] - playerPosition[1], self.globalA[2] - playerPosition[2])
        playerB = np.array(self.globalB[0] - playerPosition[0], self.globalB[1] - playerPosition[1], self.globalB[2] - playerPosition[2])
        playerC = np.array(self.globalC[0] - playerPosition[0], self.globalC[1] - playerPosition[1], self.globalC[2] - playerPosition[2])

        # This section will apply 2 rotations to the map and rotate them to the player view

        horizontalRotationMatrix = np.array([   [math.cos(horizAngle), -math.sin(horizAngle), 0],
                                                [math.sin(horizAngle), math.cos(vertAngle), 0],
                                                [0, 0, 1]   ])
        
        verticalRotationMatrix = np.array([     [1, 0, 0],
                                                [0, math.cos(vertAngle), -math.sin(vertAngle)],
                                                [0, math.sin(vertAngle), math.cos(vertAngle)]   ])
        
        # Perform the rotations but apply the horizontal one first
        rotatedA = verticalRotationMatrix * (horizontalRotationMatrix * playerA)
        rotatedB = verticalRotationMatrix * (horizontalRotationMatrix * playerB)
        rotatedC = verticalRotationMatrix * (horizontalRotationMatrix * playerC)

        # Now, make it into 2d and store the depth
        angleA = (math.tan(rotatedA[0] /  rotatedA[1]), math.tan(rotatedA[2] /  rotatedA[1]))  # Angle A = (tan(x/y), tan(z/y) (THis is the horizontal angle then the vertical angle)
        angleB = (math.tan(rotatedB[0] /  rotatedB[1]), math.tan(rotatedB[2] /  rotatedB[1]))
        angleC = (math.tan(rotatedC[0] /  rotatedC[1]), math.tan(rotatedC[2] /  rotatedC[1]))

        # Now, calculate the distance to each point
        distanceA = math.sqrt(rotatedA[0]*rotatedA[0] + rotatedA[1]*rotatedA[1] + rotatedA[2]*rotatedA[2])
        distanceB = math.sqrt(rotatedB[0]*rotatedB[0] + rotatedB[1]*rotatedB[1] + rotatedB[2]*rotatedB[2])
        distanceC = math.sqrt(rotatedC[0]*rotatedC[0] + rotatedC[1]*rotatedC[1] + rotatedC[2]*rotatedC[2])

        return ((angleA[0], angleA[1], distanceA), (angleB[0], angleB[1], distanceB), (angleC[0], angleC[1], distanceC))
    



class object:
    def __init__ (self):
        pass
