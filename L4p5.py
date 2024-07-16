#Add a method to_polar that will convert the given point X, Y
#into its equivalent polar co-ordinates form. 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def find_midpoint(point1, point2):
    midpoint_x = (point1.x + point2.x) / 2
    midpoint_y = (point1.y + point2.y) / 2
    return Point(midpoint_x, midpoint_y)

# Creating two Point objects
point_A = Point(3, 5)
point_B = Point(7, 9)

# Finding the midpoint
midpoint = find_midpoint(point_A, point_B)
print(f"The midpoint is at ({midpoint.x}, {midpoint.y})")
