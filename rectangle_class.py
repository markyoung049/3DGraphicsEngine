import math
class rectangle:

    def __init__(self, top_left_coords, top_right_coords, bottom_left_coords, bottom_right_coords, color):
        self.top_left = top_left_coords
        self.top_right = top_right_coords
        self.bottom_left = bottom_left_coords
        self.bottom_right = bottom_right_coords
        self.color = color

    # function to check if part of the object is in that direction, and if it is, the distance that the point is from the player. If not, return -1.
    def in_bounds(self, player_coords, player_angle, pixel, distance_from_monitor, pixel_size, middle_point):

        # initialize
        pixel_t = [pixel[0] - middle_point[0], middle_point[1] - pixel[1]] # transform pygame coords so that (0, 0) is in the middle, and y is increasiong as it goes up
        x_dimension = pixel_t[0] * pixel_size
        y_dimension = pixel_t[1] * pixel_size
        pixel_angle = [math.atan(x_dimension / distance_from_monitor), math.atan(y_dimension / distance_from_monitor)]

        # first, check if the distance where the angle intersects the plane is positive
        edge_one = [[self.top_left[0] - player_coords[0], self.top_left[1] - player_coords[1], self.top_left[2] - player_coords[2]],
                    [self.top_right[0] - player_coords[0], self.top_right[1] - player_coords[1], self.top_right[2] - player_coords[2]]]
        
        edge_two = [[self.top_left[0] - player_coords[0], self.top_left[1] - player_coords[1], self.top_left[2] - player_coords[2]],
                    [self.bottom_left[0] - player_coords[0], self.bottom_left[1] - player_coords[1], self.bottom_left[2] - player_coords[2]]]

        # Compute the vectors
        vector_one = [edge_one[1][0] - edge_one[0][0], edge_one[1][1] - edge_one[0][1], edge_one[1][2] - edge_one[0][2]]
        vector_two = [edge_two[1][0] - edge_two[0][0], edge_two[1][1] - edge_two[0][1], edge_two[1][2] - edge_two[0][2]]

        normal = [vector_one[1]*vector_two[2]-vector_one[2]*vector_two[1], vector_one[2]*vector_two[0]-vector_one[0]*vector_two[2], vector_one[0]*vector_two[1]-vector_one[1]*vector_two[2]]   # cross product
        # compute d in plane equation (Ax + By + Cz = d)

        p = edge_one[0]
        d = (normal[0] * p[0]) + (normal[1] * p[1]) + (normal[2] * p[2])

        # find where t in vector f(t) = (Lt, Mt, Nt) intersects the plane by substituting Lt = x, Mt = y, Nt = z
        # First, compute AL + BM + CN
        vector = [x_dimension, y_dimension, distance_from_monitor]
        denominator =  (vector[0]*normal[0]) + (vector[1]*normal[1]) + (vector[2]*normal[2])

        # check if the line is parallel to the plane. If it is, then return -1. Since the line is restricted to hgaving a point through (0, 0), if d is zero, and if denominator is zero, then any t would work
        # which means that the line is on the plane. In this case, you return -1.
        if denominator == 0:
            return -1

        t = d / denominator
        location = [vector[0] * t, vector[1] * t, vector[2] * t]



        # Now that the location has been found, find the distance form the player , and make sure it is positive.
        location_angle = [math.atan(vector[0] / vector[2]), math.atan(vector[1] / vector[2])]
        angle_from_player = [(location_angle[0] - player_angle[0]) % 360, (location_angle[1] - player_angle[1]) % 360]
        # check if behind player
        if (angle_from_player[0] > 90) and (angle_from_player[0] < 270):
            return -1
            
        if (angle_from_player[0] > 90) and (angle_from_player[0] < 270):
            return -1 
        

                 

        # Check if the point is in the rectangle
        '''
        # first, transform 3d space s.t. location is the origin, and its basis vectors are 2 vertices of the polygon, and the k basis is the normal
        basis_i = [edge_one[0][0] - location[0], edge_one[0][1] - location[1], edge_one[0][2] - location[2]]
        basis_j = [edge_one[1][0] - location[0], edge_one[1][1] - location[1], edge_one[1][2] - location[2]]
        basis_k = normal'''
        top_left = [self.top_left[0] - player_coords[0], self.top_left[1] - player_coords[1], self.top_left[2] - player_coords[2]]
        top_right = [self.top_right[0] - player_coords[0], self.top_right[1] - player_coords[1], self.top_right[2] - player_coords[2]]
        bottom_left = [self.bottom_left[0] - player_coords[0], self.bottom_left[1] - player_coords[1], self.bottom_left[2] - player_coords[2]]
        bottom_right = [self.bottom_right[0] - player_coords[0], self.bottom_right[1] - player_coords[1], self.bottom_right[2] - player_coords[2]]

        # now, make each vector of equal depth to make checking easy
        top_left = [top_left[0]/top_left[2], top_left[1]/top_left[2], 1]
        top_right = [top_right[0]/top_right[2], top_right[1]/top_right[2], 1]
        bottom_left = [bottom_left[0]/bottom_left[2], bottom_left[1]/bottom_left[2], 1]
        bottom_right = [bottom_right[0]/bottom_right[2], bottom_right[1]/bottom_right[2], 1]

        locationt = [location[0]/location[2], location[1]/location[2], 1]

        points = [top_left, top_right, bottom_left, bottom_right, location]

        # create the convex hull, and check if the location is outside
        convex_hull = []
        # initialize with thw lowest point
        #for i in range(len(points)) :


        # if the object is there, and is not behind, find and return its euclidean distance
        distance = math.sqrt(     location[0]*location[0]     +     (location[1])*(location[1])     +    
                                  (location[2])*(location[2])           )
                        
        return distance
    
        