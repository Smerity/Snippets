# From https://twitter.com/FogleBird/status/1087152894909075463

import cairocffi as cairo
from math import hypot, pi
from random import random

W, H, N, I = 1600, 1600, 24, 2000

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
cr = cairo.Context(surface)
cr.set_source_rgb(0, 0, 0)
cr.paint()
cr.set_line_width(1)
cr.set_source_rgba(1, 1, 1, 0.05)

points = [(random() * W, random() * H) for _ in range(N)]
for i in range(I):
    p = list(points)
    for i, (x0, y0) in enumerate(p):
        x1, y1 = p[(i + 1) % N]
        dx, dy = x1 - x0, y1 - y0
        d = hypot(dx, dy)
        points[i] = (x0 + dx / d, y0 + dy / d)
        cr.arc(x0, y0, d, 0, 2 * pi)
        cr.stroke()

surface.write_to_png('out.png')
