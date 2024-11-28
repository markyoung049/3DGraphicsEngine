import math
import numpy as np
import pygame
import pygame.display

##########################################################################################################################################################################
# Triangle Class
##########################################################################################################################################################################
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
    def update2DView(self, player, fov, aspectRatio, renderDistance, screenSize):
        
        """
        playerAngle = player.getAngle()
        playerPosition = player.getPosition()
        horizAngle = -playerAngle[0]  # angle is negative because rotating in the opposite direction as the player
        vertAngle = -playerAngle[1]   # angle is negative because rotating in the opposite direction as the player

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
        
        # Perform the rotations but apply the horizontal one first. prepare for perspective mtrix
        rotatedA = verticalRotationMatrix * (horizontalRotationMatrix * playerA)
        rotatedB = verticalRotationMatrix * (horizontalRotationMatrix * playerB)
        rotatedC = verticalRotationMatrix * (horizontalRotationMatrix * playerC)

        
        w = 1

        # Now, apply the projection matrix to the rotated values
        near = renderDistance[0]
        far = renderDistance[1]

        projectionMatrix = np.array([   [1/(aspectRatio * math.tan(fov/2)), 0, 0, 0],
                                        [0, 1/(math.tan(fov/2)), 0, 0],
                                        [0, 0, (near+far)/(near-far), (2*near*far)/(near-far)],
                                        [0, 0, -1, 0]   ])


        aPrime = projectionMatrix * np.array(rotatedA[0], rotatedA[1], rotatedA[2], 1)
        bPrime = projectionMatrix * np.array(rotatedB[0], rotatedB[1], rotatedB[2], 1) 
        cPrime = projectionMatrix * np.array(rotatedC[0], rotatedC[1], rotatedC[2], 1)

        
        # Now, calculate the distance to each point using a^2 + b^2 + c^2 = d^2
        distanceA = math.sqrt(rotatedA[0]*rotatedA[0] + rotatedA[1]*rotatedA[1] + rotatedA[2]*rotatedA[2])
        distanceB = math.sqrt(rotatedB[0]*rotatedB[0] + rotatedB[1]*rotatedB[1] + rotatedB[2]*rotatedB[2])
        distanceC = math.sqrt(rotatedC[0]*rotatedC[0] + rotatedC[1]*rotatedC[1] + rotatedC[2]*rotatedC[2])
        

        # Save the depth
        self.depthA = rotatedA[2]
        self.depthB = rotatedB[2]
        self.depthC = rotatedC[2]



        # Now, compute the 2d position of a b and c 
        self.positionA = (math.tan(angleA[0]), (math.tan(angleA[1])))
        self.positionB = (math.tan(angleB[0]), (math.tan(angleB[1])))
        self.positionC = (math.tan(angleC[0]), (math.tan(angleC[1])))


        """

        self.screenA = toPlayerView (self.a, player, fov, aspectRatio, renderDistance, screenSize)
        self.screenB = toPlayerView (self.b, player, fov, aspectRatio, renderDistance, screenSize)
        self.screenC = toPlayerView (self.c, player, fov, aspectRatio, renderDistance, screenSize)

        # GEt the screen space coordinates

  


        # Get the bounding box
        # First, get the minimum in the x direction
        xPositions = [self.screenA[0], self.screenB[0], self.screenC[0]]
        yPositions = [self.screenA[1], self.screenB[1], self.screenC[1]]
        xPositions.sort()
        yPositions.sort()
  
        self.boundingBox = [xPositions[0], xPositions[2], yPositions[0], yPositions[2]]
        
        # Compute the area of the triangle using determinant
        self.area = abs(0.5 * (  self.screenA[0] * (self.screenB[1] - self.screenC[1]) 
                           + self.screenB[0] * (self.screenC[1] - self.screenA[1]) 
                           + self.screenC[0] * (self.screenA[1] - self.screenB[1])))
        


            



    # Functions to get 2d position for points a b and c
    def getScreenA(self): 
        return self.screenA
    
    def getScreenB(self): 
        return self.screenB
    
    def getScreenC(self): 
        return self.screenC
    
    

    # Get bounding box
    def getBoundingBox(self):
        return self.boundingBox
    
    # get the triangle area
    def getArea(self):
        return self.area
    
    # Get the color
    def getColor(self):
        return self.color
    

    
        





##########################################################################################################################################################################
# Entity Class
##########################################################################################################################################################################
class entity:

    # Initialize the object
    def __init__ (self, triangles):
        self.triangles = triangles

    # This will return a list of where each pixel hits the triangle if it hists it. It will give the distance
    def getRenderData(self, screenSize, pixArray, pxArray):

        screenWidth = screenSize[0]
        screenHeight = screenSize[1]


        # For every triangle, get the depth of where each pixel hits if if it hits it
        for triangle in self.triangles:
            a = triangle.getScreenA()
            b = triangle.getScreenB()
            c = triangle.getScreenC()


            # Make sure the triangle isnt out of render distance
            if (0 <= a[2] <= 1) or (0 <= b[2] <= 1) or (0 <= c[2] <= 1):

                boundingBox = triangle.getBoundingBox()
                minX, maxX, minY, maxY = math.floor(boundingBox[0]), math.ceil(boundingBox[1]), math.floor(boundingBox[2]), math.ceil(boundingBox[3])


                # make sure the bounding box is in thw window and if not then clip it
                if minX <= 0:
                    minX = 0
                if maxX >= screenWidth:
                    maxX = screenWidth-1

                if minY <= 0:
                    minY = 0
                if maxY >= screenHeight:
                    maxY = screenHeight-1


                # for every pixel in the bounding box, check where they land in the triangle
                for x in range(minX, maxX):
                    for y in range(minY, maxY):
                        p  = (x, y)

                        # Now do edge functions: Baically its a cross product between the vector of side AB and AP, BC and BP, CA anc CP. if all cross products have same sign
                        # then the pont must be inside the triangle.

                        eAB = (p[0] - a[0]) * (b[1] - a[1]) - ((p[1] - a[1]) * (b[0] - a[0]))
                        eBC = (p[0] - b[0]) * (c[1] - b[1]) - ((p[1] - b[1]) * (c[0] - b[0]))
                        eCA = (p[0] - c[0]) * (a[1] - c[1]) - ((p[1] - c[1]) * (a[0] - c[0]))

                        # If they have the same sign then the point is in the triangle
                        if (eAB>= 0 and eBC>=0 and eCA>=0) or (eAB<= 0 and eBC<=0 and eCA<=0):
                            
                            eAB = abs(eAB)
                            eBC = abs(eBC)
                            eCA = abs(eCA)

                            # Compute the depth using barycentric coordinates
                            area = triangle.getArea()

                            # Use barycentric coordinates to compute the depth
                            alpha = eBC / area
                            beta = eCA / area
                            gamma = eAB / area   
                            
                            z = alpha * a[2] + beta * b[2] + gamma * c[2]

                            # if the depth is minimum so far update
                            if 0 <= z <= pixArray[x][y]:
                                pixArray[x][y] = z
                                # Since pygame flips y you need to transform it
                                yPrime = -y + screenHeight-1
                                pxArray[x, yPrime] = triangle.getColor()

                                
                        # If the point is not in the triangle
                        else:
                            pass

        return pixArray, pxArray


                    

    # Update the object
    def update(self, player, fov, aspectRatio, renderDistance, screenSize): 
        for triangle in self.triangles:
            triangle.update2DView(player, fov, aspectRatio, renderDistance, screenSize)

        




##########################################################################################################################################################################
# Player Class
##########################################################################################################################################################################
class player:
    def __init__(self, position, angle):
        self.position = position
        self.angle = angle


    # Get player position
    def getPosition(self):
        return self.position
    
    # Get player angle
    def getAngle(self):
        return self.angle
    
    """
    # Get player height
    def getHeight(self):
        return self.height

    """

    # Set player position
    def setPosition(self, position):
        self.position = position
    
    # Set player angle
    def setAngle(self, angle):
        self.angle = angle
    
    """
    # Set player height
    def setHeight(self, height):
        self.height = height

    """



##########################################################################################################################################################################
# Render Function
##########################################################################################################################################################################
def render(entities, player, fov, aspectRatio, renderDistance, screen, screenSize):
    # Fill the sreen black
    screen.fill([0, 0, 0])

    pxArray = pygame.PixelArray(screen)
    # Initialize an empty pixelarray with -1
    pixArray = []
    
    for i in range(screenSize[0]):
        pixList = []

        for j in range(screenSize[1]):
            pixList.append(renderDistance[1] + 1)
        
        pixArray.append(pixList)

    # iterate through all objects and compute the depth of each pixel
    for entity in entities:

        # Update all objects and create an empty pixelarray
        entity.update(player, fov, aspectRatio, renderDistance, screenSize)
        
        # Get the render data
        pixArray, colorArray = entity.getRenderData(screenSize, pixArray, pxArray)
        
    

    pygame.display.flip() # update the screen



##########################################################################################################################################################################
# Convert 3D Coord to Player View Function
##########################################################################################################################################################################
def toPlayerView(point, player, fov, aspectRatio, renderDistance, screenSize):
        
        playerAngle = player.getAngle()
        playerPosition = player.getPosition()
        horizAngle = playerAngle[0]  # angle is negative because rotating in the opposite direction as the player
        vertAngle = playerAngle[1]   # angle is negative because rotating in the opposite direction as the player
        x = point[0]
        y = point[1]
        z = point[2]

        # Get the points coordinates relative to the player
        pointPlayerPosition = np.array([x - playerPosition[0], y - playerPosition[1], z - playerPosition[2]])
        

        # This section will apply 2 rotations to the map and rotate them to the player view

        verticalRotationMatrix = np.array([     [1, 0, 0],
                                                [0, math.cos(vertAngle), -math.sin(vertAngle)],
                                                [0, math.sin(vertAngle), math.cos(vertAngle)]   ])
        
        horizontalRotationMatrix = np.array([   [math.cos(horizAngle), 0, math.sin(horizAngle)],
                                                [0, 1, 0],
                                                [-math.sin(horizAngle), 0, math.cos(horizAngle)]   ])
        
        # Perform the rotations but apply the horizontal one first. prepare for perspective matrix
        rotatedPoint = np.dot(verticalRotationMatrix, np.dot(horizontalRotationMatrix, pointPlayerPosition))

        # Now, apply the projection matrix to the rotated values
        near = renderDistance[0]
        far = renderDistance[1]

        projectionMatrix = np.array([   [1/(aspectRatio * math.tan(fov/2)), 0, 0, 0],
                                        [0, 1/(math.tan(fov/2)), 0, 0],
                                        [0, 0, (near+far)/(far-near), (2*near*far)/(far-near)],
                                        [0, 0, 1, 0]   ])
        
        ndcPoint = np.dot(projectionMatrix, np.array([rotatedPoint[0], rotatedPoint[1], rotatedPoint[2], 1]))
        w = ndcPoint[3]
        

        if w != 0:
            ndcPoint = ndcPoint / abs(w) # Absolute value si ot preserves the direction 
        else:
            print('Value Error')
        # Apply the viewpoint matrix to but the coords in terms of screen coordinates
        width = screenSize[0]
        height = screenSize[1]
        viewpointMatrix = np.array( [[width/2, 0, 0, width/2 ],
                                    [0, height/2, 0, height/2 ], 
                                    [0, 0, 1, -1],
                                    [0, 0, 0, 1]] )

        # Get screen coordinates
        coords = np.dot(viewpointMatrix, ndcPoint)
        return coords
