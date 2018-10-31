from math import *

init_x = 340
init_y = 250
x_end = 775
scale = 4


def Exact(self, root, canv, x0, y0, X, grid):
    # y'=xy^2+3xy
    # y = 3/(1-ce^(3x^2/2)) - 3
    # c=y0/exp((3*x0^2)/2)
    h=grid
    c = y0 / ((y0 + 3) * exp((3 * (x0 ** 2)) / 2))
    yf, xf = y0, x0
    scale = abs((init_x - x_end)) / X
    print("scale=" + str(scale))
    for x in range(ceil(x0 * h), ceil(X * h)):
        xcur = x / h
        y = (3 / (1 - c * exp((3 * (xcur ** 2)) / 2))) - 3
        if abs(yf - y) < h:
            canv.create_line(init_x + scale * xcur, init_y - scale * y/2, init_x + scale * xf, init_y - scale * yf/2,
                             fill="red", width=1.5)
        yf, xf = y, xcur

def Euler(self, root, canv, x0, y0, X, grid):
    # y'=xy^2+3xy
    # y1=y0+(x0y0^2+3x0y0)*(1/grid)
    # x1=y0+1/grid
    h=1/grid
    xf, yf = x0, y0
    print("Hey, pidor")
    scale = abs((init_x - x_end)) / X
    for x in range(ceil(x0*grid), ceil(X*grid)):
        xcur=x*h
        y = yf+(xf*(yf**2)+3*xf*yf)*h
        if abs(yf - y) < grid:
            canv.create_line(init_x + scale * xcur, init_y - scale * y/2, init_x + scale * xf, init_y - scale * yf/2,
                             fill="yellow", width=1.5)
        yf, xf = y, xcur
    print("Ti pidor")

def Euler_i(self, root, canv, x0, y0, X, grid):
    print("Ti pidor")

def RC(self, root, canv, x0, y0, X, grid):
    print("Ti pidor")




class my_grap:
    exact = Exact
    euler = Euler
    euler_i = Euler_i
    rc = RC