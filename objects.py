import math

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.r = radius

    def sdf(self, point):
        x, y, z = point
        cx, cy, cz = self.center
        return ((x - cx) ** 2 + (y - cy) ** 2 + (z - cz) ** 2) ** 0.5 - self.r


class Mandelbulb:
    def __init__(self, pow = 8, mxit = 100):
        self.pow = pow
        self.mxit = mxit

    def sdf(self, point):
        x, y, z = point
        mxit = self.mxit
        pow = self.pow
        
        z_x, z_y, z_z = x, y, z
        dr = 1.0
        r = 0.0

        for i in range(mxit):
            r = math.sqrt(z_x * z_x + z_y * z_y + z_z * z_z)
            if r > 2.0:
                break

            theta = math.acos(z_z / r)
            phi = math.atan2(z_y, z_x)
            zr = r ** pow

            dr = zr * pow * dr + 1.0

            z_x = zr * math.sin(theta * pow) * math.cos(phi * pow) + x
            z_y = zr * math.sin(theta * pow) * math.sin(phi * pow) + y
            z_z = zr * math.cos(theta * pow) + z

        distance = 0.5 * math.log(r) * r / dr
        return distance