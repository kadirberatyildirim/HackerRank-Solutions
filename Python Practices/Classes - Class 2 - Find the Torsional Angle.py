"""
You are given four points A, B, C and D in a 3-dimensional Cartesian coordinate system. 
You are required to print the angle between the plane made by the points A, B, C and D in degrees(not radians). 
Let the angle be PHI. 
"""

import math

class Points(object):
    def __init__(self, x, y, z):
        self.coord = [x, y, z]

    def __sub__(self, no):
        return Points(*[a_i - b_i for a_i, b_i in zip(self.coord, no.coord)])

    def dot(self, no):
        return sum(i * j for i, j in zip(self.coord, no.coord))

    def cross(self, no):
        c = [self.coord[1] * no.coord[2] - self.coord[2] * no.coord[1],
            self.coord[2] * no.coord[0] - self.coord[0] * no.coord[2],
            self.coord[0] * no.coord[1] - self.coord[1] * no.coord[0]]

        return Points(*c)
        
    def absolute(self):
        return pow((self.coord[0] ** 2 + self.coord[1] ** 2 + self.coord[2] ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))