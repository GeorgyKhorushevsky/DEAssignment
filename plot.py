from math import *
from tkinter import *
root = Tk()
default_color = "blue"
canv = Canvas(root, width=850, heigh=500)
canv.pack()
label_x0 = Label(root, text="x0:", font="60")
entry_x0 = Entry(root, text="default=0", foreground="black", font="60")
label_y0 = Label(root, text="y0:", font="60")
entry_y0 = Entry(root, text="default=3", font="60")
label_X = Label(root, text=" X:", font="60")
entry_X = Entry(root, text="default=5.5", font="60")
label_grid = Label(root, text="GRID", font="60")
entry_grid = Entry(root, text="default=0.1", font="60")
exact_check = Checkbutton(root, text="Exact solution", font="50")
euler_check = Checkbutton(root, text="Euler's method", font="50")
euler_i_check = Checkbutton(root, text="Euler's improved", font="50")
rc_check = Checkbutton(root, text = "Runge-Kutta method", font="50")

def apply():
    print("I'm alive!")
def error():
    print(entry_grid)



title = Label(root, text="y'=xy^2+3xy", background="#148", foreground="#ccc", padx="25", pady="10", font="100")
title.place(x=0, y=0)

label_x0.place(x=20, y=50)
entry_x0.place(x=60, y=50)
label_y0.place(x=20, y=90)
entry_y0.place(x=60, y=90)
label_X.place(x=20, y=130)
entry_X.place(x=60, y=130)
label_grid.place(x=1, y=170)
entry_grid.place(x=60, y=170)
exact_check.place(x=20, y=200)
euler_check.place(x=20, y=230)
euler_i_check.place(x=20, y=260)
rc_check.place(x=20, y=290)
x0, y0, xm, ym = 340, 250, 780, 20
buttom_frame = Frame(root)
buttom_frame.pack(side=BOTTOM)
canv.create_line(x0 - 10, y0, xm + 10, y0, fill=default_color, arrow=LAST, width=0.1)
canv.create_line(x0, ym - 10, x0, 2 * y0 - ym + 10, fill=default_color, arrow=FIRST, width=0.1)
apply_but = Button(text="APPLY", background="#148", foreground="#ccc", padx="14", pady="7", font="13", command=apply)
apply_but.place(x=50, y=350)
error_but = Button(text="SHOW ERRORS", background="#000", foreground="#ccc", padx="14", pady="7", font="13", command=error)
error_but.place(x=50, y=430)
root.mainloop()
