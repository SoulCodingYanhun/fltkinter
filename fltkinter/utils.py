import tkinter as tk

def create_round_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]

    return canvas.create_polygon(points, **kwargs, smooth=True)

def animate(widget, attribute, start, end, duration, steps=10, update_func=None):
    step_size = (end - start) / steps
    step_time = int(duration / steps)

    def step(i):
        if i < steps:
            value = start + (step_size * i)
            if update_func:
                update_func(value)
            else:
                widget[attribute] = value
            widget.after(step_time, step, i + 1)

    step(0)