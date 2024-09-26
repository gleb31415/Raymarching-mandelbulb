import tkinter as tk
from Objects import Circle, Rectangle, Triangle
import time

root = tk.Tk()
root.title("2D Ray Marching")

width, height = 800, 800
lb, ub = 0.1, 800
camx, camy = None, None
rx, ry = 0, 0


def set_camera(event):
    global camx, camy
    canvas.delete("camera")
    canvas.delete("anim")
    x, y = event.x, event.y
    rad = 3
    canvas.create_oval(x - rad, y - rad, x + rad, y + rad, fill='white', tags="camera")
    camx, camy = x, y
    canvas.unbind("<Button-1>")
    canvas.bind("<Button-1>", set_ray)
    canvas.tag_raise("camera")


def set_ray(event):
    global camx, camy, rx, ry
    if camx is None or camy is None:
        return

    x, y = event.x, event.y
    k = (y - camy) / (x - camx)
    b = camy - k * camx
    canvas.delete("base_ray")
    if x > camx:
        canvas.create_line(camx, camy, width, width * k + b, fill='yellow', tags="base_ray")
    else:
        canvas.create_line(camx, camy, 0, b, fill='yellow', tags="base_ray")
    rx, ry = x, y
    start_animation(k, b)
    canvas.tag_raise("base_ray")


def start_animation(k, b):
    for obj in objects:
        obj.plot(canvas)
    canvas.tag_raise("camera")
    canvas.tag_raise("base_ray")
    x, y = camx, camy
    r = calc_min_dist(objects, x, y)
    canvas.delete("anim")
    while lb < r < ub:
        canvas.create_oval(x - r, y - r, x + r, y + r, outline='red', tags="anim")

        dx = r / ((1 + k ** 2) ** 0.5)
        dy = k * dx

        if rx >= camx:
            x += dx
            y += dy
        else:
            x -= dx
            y -= dy

        r = calc_min_dist(objects, x, y)
        canvas.update()
        time.sleep(0.2)


def calc_min_dist(objects, x, y):
    min_dist = float('inf')
    for obj in objects:
        min_dist = min(min_dist, obj.dist(x, y))
    return min_dist


def activate_camera():
    for obj in objects:
        obj.plot(canvas)
    canvas.delete("cam")
    canvas.delete("base_ray")
    canvas.delete("anim")
    canvas.bind("<Button-1>", set_camera)


objects = [
    Circle(150, 150, 50),
    Circle(650, 150, 50),
    Circle(150, 650, 50),
    Circle(650, 650, 50),

    Rectangle(400, 150, 100, 200, 0),
    Rectangle(150, 400, 200, 100, 45),
    Rectangle(650, 400, 200, 100, 45),
    Rectangle(400, 650, 100, 200, 0),

    Triangle(400, 130, 350, 400, 450, 400),
    Triangle(200, 550, 150, 650, 250, 650),
    Triangle(60, 50, 190, 140, 210, 300),
    Triangle(400, 750, 350, 850, 450, 850)
]

canvas = tk.Canvas(root, width=width, height=height, background='black')
camera_button = tk.Button(root, text="Set Camera", command=activate_camera)
camera_button.pack()
canvas.pack()

root.mainloop()
