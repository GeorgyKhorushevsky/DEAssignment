from math import *
from tkinter import *
from Error import Error
from my_grap import my_grap

root = Tk()
root1 = Tk()
root1.title("DE Error table")
root1.geometry("400x400")


root.title("DE graphical representation")
root.geometry("850x500")



default_color = "blue"
canv = Canvas(root, width=850, heigh=500)

canv.pack()

scrollbar = Scrollbar(root1, orient=VERTICAL)
scrollbar.pack(fill=Y, side=RIGHT)
listbox = Listbox(root1)
listbox.pack(fill=BOTH, expand=1)



listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


label_x0 = Label(root, text="x0:", font="60")
entry_x0 = Entry(root, text="default=0", foreground="black", font="60")
label_y0 = Label(root, text="y0:", font="60")
entry_y0 = Entry(root, text="default=3", font="60")
label_X = Label(root, text=" X:", font="60")
entry_X = Entry(root, text="default=5.5", font="60")
label_grid = Label(root, text="GRID", font="60")
entry_grid = Entry(root, text="default=0.1", font="60")

entry_x0.insert(0, "0")
entry_y0.insert(0, "3")
entry_X.insert(0, "5.5")
entry_grid.insert(0, "1000")

exact_g, euler, euler_i, rc = BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(),
exact_check = Checkbutton(root, text="Exact solution", font="50", variable=exact_g)
euler_check = Checkbutton(root, text="Euler's method", font="50", variable=euler)
euler_i_check = Checkbutton(root, text="Euler's improved", font="50", variable=euler_i)
rc_check = Checkbutton(root, text="Runge-Kutta method", font="50", variable=rc)




def clean(canv):
    x0, y0, xm, ym = 340, 250, 780, 20
    for y in range(-1000, 500):

        canv.create_line(x0 - 30, y, xm + 70, y, fill="white", arrow=LAST, width=0.1)

    canv.create_line(x0 - 10, y0, xm + 10, y0, fill=default_color, arrow=LAST, width=0.1)
    canv.create_line(x0, ym - 10, x0, 2 * y0 - ym + 10, fill=default_color, arrow=FIRST, width=0.1)
    canv.create_line(x0 - 30, 0, x0 - 30, 500, fill="black", width=2)


clean(canv)


def clean_but():
    clean(canv)
    entry_x0.delete(0, END)
    entry_y0.delete(0, END)
    entry_X.delete(0, END)
    entry_grid.delete(0, END)


def apply():
    grap = my_grap()
    clean(canv)
    print(exact_g.get())
    print(euler.get())
    if exact_g.get():
        grap.exact(root, canv, float(entry_x0.get()), float(entry_y0.get()), float(entry_X.get()),
                   float(entry_grid.get()))
    if euler.get():
        grap.euler(root, canv, float(entry_x0.get()), float(entry_y0.get()), float(entry_X.get()),
                   float(entry_grid.get()))
    if euler_i.get():
        grap.euler_i(root, canv, float(entry_x0.get()), float(entry_y0.get()), float(entry_X.get()),
                     float(entry_grid.get()))
    if rc.get():
        grap.rc(root, canv, float(entry_x0.get()), float(entry_y0.get()), float(entry_X.get()), float(entry_grid.get()))





def error():
    error = Error()
    error.all( listbox, float(entry_x0.get()), float(entry_y0.get()), float(entry_X.get()), float(entry_grid.get()))


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
buttom_frame = Frame(root)
buttom_frame.pack(side=BOTTOM)


apply_but = Button(text="APPLY", background="#148", foreground="#ccc", padx="14", pady="7", font="13", command=apply)
apply_but.place(x=50, y=350)
clean_but = Button(text="CLEAN", background="#aaa", foreground="#000", padx="14", pady="7", font="13",
                   command=clean_but)
clean_but.place(x=180, y=350)
error_but = Button(text="SHOW ERRORS", background="#000", foreground="#ccc", padx="14", pady="7", font="13",
                   command=error)
error_but.place(x=50, y=430)


root.mainloop()
root1.mainloop()
