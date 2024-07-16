#Add a method to_polar that will convert the given point X, Y
#into its equivalent polar co-ordinates form.
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_polar(self):
        r = math.sqrt(self.x ** 2 + self.y ** 2)
        theta = math.atan2(self.y, self.x)
        theta_deg = math.degrees(theta)
        return r, theta_deg

# Example usage
point = Point(3, 4)
r, theta = point.to_polar()
print(f"Polar coordinates: r = {r}, θ = {theta} degrees")
