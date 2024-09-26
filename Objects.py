import numpy as np


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def dist(self, x0, y0):
        return ((self.x - x0) ** 2 + (self.y - y0) ** 2) ** 0.5 - self.r

    def plot(self, canvas):
        x, y, r = self.x, self.y, self.r
        canvas.create_oval(x - r, y - r, x + r, y + r, fill='green', tags='objects')


class Rectangle:
    def __init__(self, x0, y0, w, h, angle):
        self.x = x0
        self.y = y0
        self.w = w
        self.h = h
        self.angle = np.radians(angle)

    def dist(self, x0, y0):
        cos_a, sin_a = np.cos(-self.angle), np.sin(-self.angle)
        x, y = x0 - self.x, y0 - self.y
        x_rot = cos_a * x - sin_a * y
        y_rot = sin_a * x + cos_a * y

        dx = max(abs(x_rot) - self.w / 2, 0)
        dy = max(abs(y_rot) - self.h / 2, 0)

        return (dx ** 2 + dy ** 2) ** 0.5

    def plot(self, canvas):
        x, y, w, h, angle = self.x, self.y, self.w, self.h, self.angle

        cos_a, sin_a = np.cos(angle), np.sin(angle)

        x1 = x + (-w / 2 * cos_a - -h / 2 * sin_a)
        y1 = y + (-w / 2 * sin_a + -h / 2 * cos_a)

        x2 = x + (w / 2 * cos_a - -h / 2 * sin_a)
        y2 = y + (w / 2 * sin_a + -h / 2 * cos_a)

        x3 = x + (w / 2 * cos_a - h / 2 * sin_a)
        y3 = y + (w / 2 * sin_a + h / 2 * cos_a)

        x4 = x + (-w / 2 * cos_a - h / 2 * sin_a)
        y4 = y + (-w / 2 * sin_a + h / 2 * cos_a)

        points = [x1, y1, x2, y2, x3, y3, x4, y4]
        canvas.create_polygon(points, fill='green', tags='objects')


class Triangle:
    def __init__(self, x0, y0, x1, y1, x2, y2):
        self.x0, self.y0 = x0, y0
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2

    def dist(self, x0, y0):
        def point_line_dist(px, py, ax, ay, bx, by):
            abx, aby = bx - ax, by - ay
            apx, apy = px - ax, py - ay
            ab_ap = abx * apx + aby * apy
            ab_ab = abx * abx + aby * aby
            t = max(0, min(1, ab_ap / ab_ab))
            closest_x = ax + t * abx
            closest_y = ay + t * aby
            return ((px - closest_x) ** 2 + (py - closest_y) ** 2) ** 0.5

        d1 = point_line_dist(x0, y0, self.x0, self.y0, self.x1, self.y1)
        d2 = point_line_dist(x0, y0, self.x1, self.y1, self.x2, self.y2)
        d3 = point_line_dist(x0, y0, self.x2, self.y2, self.x0, self.y0)

        return min(d1, d2, d3)

    def plot(self, canvas):
        points = [self.x0, self.y0, self.x1, self.y1, self.x2, self.y2]
        canvas.create_polygon(points, outline='white', fill='white', tags='objects')
