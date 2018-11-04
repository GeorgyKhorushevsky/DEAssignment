from math import *

init_x = 340
init_y = 250
x_end = 775
scale = 4


def f(x, y):
    return x * y * y + 3 * x * y


def exact_point(x0, y0, xcur):
    c = y0 / ((y0 + 3) * exp((3 * (x0 ** 2)) / 2))
    return (3 / (1 - c * exp((3 * (xcur ** 2)) / 2))) - 3


def Exact(self, root, canv, x0, y0, X, grid):
    # y'=xy^2+3xy
    # y = 3/(1-ce^(3x^2/2)) - 3
    # c=y0/exp((3*x0^2)/2)
    print("mem&")
    init_x = 340
    init_y = 250
    x_end = 775
    xf, yf = x0, y0
    print("Hey, pidor")
    scale = abs((init_x - x_end)) / X
    init_x -= x0 * scale
    h = grid
    c = y0 / ((y0 + 3) * exp((3 * (x0 ** 2)) / 2))
    yf, xf = y0, x0
    scale = abs((init_x - x_end)) / X
    print("scale=" + str(scale))
    for x in range(ceil(x0 * h), ceil(X * h)):
        xcur = x / h
        y = (3 / (1 - c * exp((3 * (xcur ** 2)) / 2))) - 3
        if abs(yf - y) < h:
            canv.create_line(init_x + scale * xcur, init_y - scale * y / 2, init_x + scale * xf,
                             init_y - scale * yf / 2,
                             fill="red", width=1.5)
        yf, xf = y, xcur


def y_Euler(x0, y0, x, yf, xf, h):
    try:
        my_x, my_y = x, yf + (xf * (yf ** 2) + 3 * xf * yf) * h
    except:
        print("DA-DA??")
        my_x, my_y = x + 1, exact_point(x0, y0, (x + 1) * h)
    return my_x, my_y


def Euler(self, root, canv, x0, y0, X, grid):
    # y'=xy^2+3xy
    # y1=y0+(x0y0^2+3x0y0)*(1/grid)
    # x1=x0+1/grid
    print("mem&")
    init_x = 340
    init_y = 250
    x_end = 775
    h = 1 / grid
    xf, yf = x0, y0
    print("Hey, pidor")
    scale = abs((init_x - x_end)) / X
    init_x -= x0 * scale
    print(init_x)
    x = ceil(x0 * grid)
    while x < ceil(X * grid):

        x, y = y_Euler(x0, y0, x, yf, xf, h)
        xcur = x * h
        if abs(yf - y) < grid:
            canv.create_line(init_x + scale * xcur, init_y - scale * y / 2, init_x + scale * xf,
                             init_y - scale * yf / 2,
                             fill="yellow", width=1.5)
        yf, xf = y, xcur
        x += 1
    print("Ti pidor")


def y_Euler_i(x0, y0, x, yf, xf, h):
    my_y_sh = yf + f(xf, yf) * h
    my_y = yf + h * (f(xf, yf) + f(xf + abs(x * h), my_y_sh) / 2)
    my_x = x
    if my_y != inf and not isnan(my_y):
        print(my_y)
        return my_x, my_y
    else:
        print("DA-DA??")
        return x + 1, exact_point(x0, y0, (x + 1) * h)


def Euler_i(self, root, canv, x0, y0, X, grid):
    # y'=xy^2+3xy
    # my_y1=y0+(x0y0^2+3x0y0)*(1/grid)
    # x1 = x0+1/grid
    # y1 = y0+(1/grid)*(f(x0, y0)+f(x1, my_y1))/2
    init_x = 340
    init_y = 250
    x_end = 775
    print("Hey, pidor")
    scale = abs((init_x - x_end)) / X
    init_x -= x0 * scale
    h = 1 / grid
    xf, yf = x0, y0
    print("Hey, pidor")
    x = ceil(x0 * grid)
    while x < ceil(X * grid):

        x, y = y_Euler_i(x0, y0, x, yf, xf, h)
        xcur = x * h
        if abs(yf - y) < grid:
            canv.create_line(init_x + scale * xcur, init_y - scale * y / 2, init_x + scale * xf,
                             init_y - scale * yf / 2,
                             fill="green", width=1.5)
        yf, xf = y, xcur
        x += 1
    print("Ti pidor")


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
    if my_y != inf and not isnan(my_y):
        return my_x, my_y
    else:
        print("DA-DA??")
        return x + 1, exact_point(x0, y0, (x + 1) * h)


def RC(self, root, canv, x0, y0, X, grid):
    # y'=xy^2+3xy=f(x,y)
    # h = 1 / grid
    # k1 = f(x0, y0)
    # k2 = f(x0+h/2, y0+h*k1/2)
    # k3 = f(x0+h/2, y0+h*k2/2)
    # k4 = f(x0+h, y0+h*k3)
    # y1 = y0 + (h/6)*(k1+2k2+2k3+k4)
    init_x = 340
    init_y = 250
    x_end = 775
    print("Hey, pidor")
    scale = abs((init_x - x_end)) / X
    init_x -= x0 * scale
    h = 1 / grid
    xf, yf = x0, y0
    x = ceil(x0 * grid)
    while x < ceil(X * grid):

        x, y = y_RC(x0, y0, x, yf, xf, h)
        xcur = x * h
        if abs(yf - y) < grid:
            canv.create_line(init_x + scale * xcur, init_y - scale * y / 2, init_x + scale * xf,
                             init_y - scale * yf / 2,
                             fill="#654", width=1.5)
        print(xcur, y)
        yf, xf = y, xcur
        x += 1
    print("Ti pidor")


class my_grap:
    exact = Exact
    euler = Euler
    euler_i = Euler_i
    rc = RC
