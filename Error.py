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
    print("mem&")
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
    if my_y != inf and not isnan(my_y) and abs(my_y - exact_point(x0, y0, x * h)) < 10 ** 9:
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
    if my_y != inf and not isnan(my_y) and abs(my_y - exact_point(x0, y0, x * h)) < 10 ** 9:
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
    if my_y != inf and not isnan(my_y) and abs(my_y - exact_point(x0, y0, x * h)) < 10 ** 9:
        return my_y
    else:
        return exact_point(x0, y0, (x + 1) * h)


def graph(listbox, x0, y0, X, grid):
    h = 1 / grid
    yf1, yf2, yf3, xf = y0, y0, y0, x0
    scale = X - x0
    y1 = y2 = y3 = [x0, y0, 0]
    listbox.insert(END, "%6s %7s %15s %15s %15s" % ("x", "y", "Euler", "Euler_i", "Runge-Kutta" ))
    for x in range(0, int(scale * grid)):
        x_cur = x0 + x / grid
        exact = exact_point(x0, y0, x_cur)
        listbox.insert(END, "%6s %7s %15s %15s %15s" % (str(x_cur), str(round(exact, 3)), str(
            round(exact - y_Euler(x0, y0, x_cur, yf1, xf, h), 3)), str(
            round(exact - y_Euler_i(x0, y0, x_cur, yf2, xf, h), 3))
                                                        , str(
            round(exact - y_RC(x0, y0, x_cur, yf3, xf, h), 3))))

        yf1, yf2, yf3, xf = y_Euler(x0, y0, x_cur, yf1, xf, h), y_Euler_i(x0, y0, x_cur, yf2, xf, h), y_RC(x0, y0,
                                                                                                           x_cur, yf3,
                                                                                                           xf, h), x_cur
        if abs(round(exact - y_Euler(x0, y0, x_cur, yf1, xf, h), 3))>abs(y1[2]):
            y1 = [x_cur, round(exact, 3), round(exact - y_Euler(x0, y0, x_cur, yf1, xf, h), 3)]
        if abs(round(exact - y_Euler_i(x0, y0, x_cur, yf2, xf, h), 3))>abs(y2[2]):
            y2 = [x_cur, round(exact, 3), round(exact - y_Euler_i(x0, y0, x_cur, yf2, xf, h), 3)]
        if abs(round(exact - y_RC(x0, y0, x_cur, yf3, xf, h), 3))>abs(y3[2]):
            y3 = [x_cur, round(exact, 3), round(exact - y_RC(x0, y0, x_cur, yf3, xf, h), 3)]
    listbox.insert(END, "------------global-----------")
    listbox.insert(END,"%6s %7s %15s" % (str(y1[0]), str(y1[1]), str(y1[2])))
    listbox.insert(END,"%6s %7s %40s" % (str(y2[0]), str(y2[1]), str(y2[2])))
    listbox.insert(END, "%6s %7s %65s" % (str(y3[0]), str(y3[1]), str(y3[2])))
    print("Ti pidor")


def All(self, listbox, x0, y0, X, grid):
    graph(listbox, x0, y0, X, grid)


class Error():
    all = All
