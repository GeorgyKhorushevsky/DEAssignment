from math import *
from tkinter import END

init_x = 340
init_y = 1000
x_end = 775
scale = 4

scale1 = 120
scale2 = 25


def f(x, y):
    return x * y * y + 3 * x * y


def exact_point(x0, y0, xcur):
    c = y0 / ((y0 + 3) * exp((3 * (x0 ** 2)) / 2))
    return (3 / (1 - c * exp((3 * (xcur ** 2)) / 2))) - 3


def Exact(x0, y0, X, grid):
    # y'=xy^2+3xy
    # y = 3/(1-ce^(3x^2/2)) - 3
    # c=y0/exp((3*x0^2)/2)
    init_x = 340
    init_y = 250
    x_end = 775
    xf, yf = x0, y0
    scale = abs((init_x - x_end)) / X
    init_x -= x0 * scale
    h = grid
    c = y0 / ((y0 + 3) * exp((3 * (x0 ** 2)) / 2))
    yf, xf = y0, x0
    scale = abs((init_x - x_end)) / X
    for x in range(ceil(x0 * h), ceil(X * h)):
        xcur = x / h
        y = (3 / (1 - c * exp((3 * (xcur ** 2)) / 2))) - 3
        yf, xf = y, xcur


def y_Euler(x0, y0, x, yf, xf, h):
    my_y = yf + (xf * (yf ** 2) + 3 * xf * yf) * h
    if my_y != inf and not isnan(my_y) and abs(my_y - exact_point(x0, y0, x * h)) < 10 ** 5:
        return my_y
    else:
        return exact_point(x0, y0, (x + 1) * h)


def Euler(x0, y0, X, grid):
    # y'=xy^2+3xy
    # y1=y0+(x0y0^2+3x0y0)*(1/grid)
    # x1=x0+1/grid
    init_x = 340
    init_y = 250
    x_end = 775
    h = 1 / grid
    xf, yf = x0, y0
    scale = abs((init_x - x_end)) / X
    init_x -= x0 * scale
    print(init_x)
    x = ceil(x0 * grid)
    while x < ceil(X * grid):
        x, y = y_Euler(x0, y0, x, yf, xf, h)
        xcur = x * h
        yf, xf = y, xcur
        x += 1


def y_Euler_i(x0, y0, x, yf, xf, h):
    my_y_sh = yf + f(xf, yf) * h
    my_y = yf + h * (f(xf, yf) + f(xf + abs(x * h), my_y_sh) / 2)
    my_x = x
    if my_y != inf and not isnan(my_y) and abs(my_y - exact_point(x0, y0, x * h)) < 10 ** 5:
        return my_y
    else:
        return exact_point(x0, y0, (x + 1) * h)


def Euler_i(x0, y0, X, grid):
    # y'=xy^2+3xy
    # my_y1=y0+(x0y0^2+3x0y0)*(1/grid)
    # x1 = x0+1/grid
    # y1 = y0+(1/grid)*(f(x0, y0)+f(x1, my_y1))/2
    init_x = 340
    init_y = 250
    x_end = 775
    scale = abs((init_x - x_end)) / X
    init_x -= x0 * scale
    h = 1 / grid
    xf, yf = x0, y0
    x = ceil(x0 * grid)
    while x < ceil(X * grid):
        x, y = y_Euler_i(x0, y0, x, yf, xf, h)
        xcur = x * h
        yf, xf = y, xcur
        x += 1


def y_RC(x0, y0, x, yf, xf, h):
    # y'=xy^2+3xy=f(x,y)
    # h = 1 / grid
    # k1 = f(x0, y0)
    # k2 = f(x0+h/2, y0+h*k1/2)
    # k3 = f(x0+h/2, y0+h*k2/2)
    # k4 = f(x0+h, y0+h*k3)
    # y1 = y0 + (h/6)*(k1+2k2+2k3+k4)

    k1 = f(xf, yf)
    k2 = f(xf + h / 2, yf + h * k1 / 2)
    k3 = f(xf + h / 2, yf + h * k2 / 2)
    k4 = f(xf + h, yf + h * k3)
    my_y = yf + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    my_x = x
    if x == x0:
        return y0
    if my_y != inf and not isnan(my_y) and abs(my_y - exact_point(x0, y0, x * h)) < 10 ** 5:
        return my_y
    else:
        return exact_point(x0, y0, (x + 1) * h)


def graph(canv, x0, y0, X, grid):
    h = 1 / grid
    yf1, yf2, yf3, xf = y0, y0, y0, x0
    scale = X - x0

    y = [0, 0, 0]
    for x in range(0, int(scale * grid)):
        x_cur = x0 + x / grid
        exact = exact_point(x0, y0, x_cur)

        yf1, yf2, yf3, xf = y_Euler(x0, y0, x_cur, yf1, xf, h), y_Euler_i(x0, y0, x_cur, yf2, xf, h), y_RC(x0, y0,
                                                                                                           x_cur, yf3,
                                                                                                           xf, h), x_cur
        y[0] += abs(yf1 - exact) * h
        y[1] += abs(yf2 - exact) * h
        y[2] += abs(yf3 - exact) * h
    return y


def All(self, canv, x0, y0, X, grid):
    init_x = 10
    init_y = 640
    x_end = 775
    yf = graph(canv, x0, y0, X, 1)
    # 0 - euler
    # 1 - euler_i
    # 2 - rc
    scale = (1 / 20)
    for i in range(2, grid):
        y = graph(canv, x0, y0, X, i)
        canv.create_line(init_x + (i - 1)*(1000/grid), init_y - scale * yf[0], init_x + (i)*(1000/grid), init_y - scale * y[0], fill="yellow")
        canv.create_line(init_x + (i - 1)*(1000/grid), init_y - scale * yf[1], init_x + (i)*(1000/grid), init_y - scale * y[1], fill="red")
        canv.create_line(init_x + (i - 1)*(1000/grid), init_y - scale * yf[2], init_x + (i)*(1000/grid), init_y - scale * y[2], fill="blue")
        yf = y


class error_plot():
    all = All
