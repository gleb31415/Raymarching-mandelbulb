import tkinter as tk
import math
from objects import Mandelbulb

root = tk.Tk()

width, height = 800, 800
cams = (-3, 0, 0)
light = (-5, 5, -10)
ang = math.radians(30)
close = 0.001
far = 10


canvas = tk.Canvas(root, width=width, height=height, background='white')
canvas.pack()


def get_to_norm(vec):
    length = math.sqrt(vec[0]**2 + vec[1]**2 + vec[2] ** 2)
    return vec[0] / length, vec[1] / length, vec[2] / length


def scal(p, q):
    return p[0] * q[0] + p[1] * q[1] + p[2] * q[2]


def normal(point, eps=1e-4):
    x, y, z = point
    dx = (object.sdf((x + eps, y, z)) - object.sdf((x - eps, y, z))) / (2 * eps)
    dy = (object.sdf((x, y + eps, z)) - object.sdf((x, y - eps, z))) / (2 * eps)
    dz = (object.sdf((x, y, z + eps)) - object.sdf((x, y, z - eps))) / (2 * eps)
    return dx, dy, dz


def toreal(point, r, al, be):
    x0, y0, z0 = point
    x = x0 + r * math.cos(al) * math.cos(be)
    y = y0 + r * math.sin(al) * math.cos(be)
    z = z0 + r * math.sin(be)
    return x, y, z


def get_light_intensity(point):
    l_v = get_to_norm((light[0] - point[0], light[1] - point[1], light[2] - point[2]))
    p_v = get_to_norm(normal(point))
    intensity = max(0, scal(l_v, p_v))
    return int(intensity * 255)


object = Mandelbulb()


def get_col(point, al, be):
    x, y, z = point
    dist = object.sdf(point)
    while close < dist < far:
        x, y, z = toreal((x, y, z), dist, al, be)
        dist = object.sdf((x, y, z))
        if dist >= far:
            return 0, 0, 30
        if dist <= close:
            intensity = get_light_intensity((x, y, z))
            blue_intensity = int(intensity * 0.8)
            return 0, int(intensity * 0.9), blue_intensity


for i in range(width):
    for j in range(height):
        dx, dy = i - width / 2, j - height / 2
        a = math.atan2(dx, width / 2) * ang
        b = math.atan2(dy, height / 2) * ang

        color = get_col(cams, a, b)
        col = f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}'
        canvas.create_line(i, j, i + 1, j, fill=col)

root.mainloop()