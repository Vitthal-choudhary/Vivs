from tkinter import *
from tkinter import ttk
import os

main_screen = Tk()
main_screen.iconbitmap("logo.ico")
main_screen.title("Vivs")
main_screen.geometry("900x700")
main_screen.config(bg="black")

Label = Label(main_screen, text="Dominoes", bg="Blue", fg="white", font=("Comic Sans MS", 50))
Label.pack()


class spinboxes_on_screen:
    def __init__(self, a, b, c):
        box = Spinbox(main_screen, textvariable=c, from_=0, to=50, width=10, font="calibri")
        box.place(x=a, y=b)


a = IntVar()
b = IntVar()
c = IntVar()
d = IntVar()
e = IntVar()
f = IntVar()
g = IntVar()
h = IntVar()
i = IntVar()
j = IntVar()

# spinboxes for number of item customer wants to order.

box1 = spinboxes_on_screen(680, 180, a)
box2 = spinboxes_on_screen(680, 220, b)
box3 = spinboxes_on_screen(680, 260, c)
box4 = spinboxes_on_screen(680, 300, d)
box5 = spinboxes_on_screen(680, 340, e)
box6 = spinboxes_on_screen(680, 380, f)
box7 = spinboxes_on_screen(680, 420, g)
box8 = spinboxes_on_screen(680, 460, h)
box9 = spinboxes_on_screen(680, 500, i)
box10 = spinboxes_on_screen(680, 540, j)

treeview_for_menu = ttk.Treeview(main_screen, columns=("c1", "c2", "c3"), show='headings', height=10)
treeview_for_menu.column("# 1", anchor=CENTER, width=200)
treeview_for_menu.heading("# 1", text="Serial Number")
treeview_for_menu.column("# 2", anchor=CENTER, width=200)
treeview_for_menu.heading("# 2", text="Items")
treeview_for_menu.column("# 3", anchor=CENTER, width=200)
treeview_for_menu.heading("# 3", text="Price")

treeview_for_menu.insert('', 'end', text="1", values=('1', 'Margherita Pizza', '109'))
treeview_for_menu.insert('', 'end', text="2", values=('2', 'Farmhouse', '269'))
treeview_for_menu.insert('', 'end', text="3", values=('3', 'Peppy Paneer', '269'))
treeview_for_menu.insert('', 'end', text="4", values=('4', 'Garlic Bread Sticks', '109'))
treeview_for_menu.insert('', 'end', text="5", values=('5', 'Taco Mexican Veg', '79'))
treeview_for_menu.insert('', 'end', text="6", values=('6', 'Moroccan Spice Pasta Pizza', '189'))
treeview_for_menu.insert('', 'end', text="7", values=('7', 'Party Combo', '2558'))
treeview_for_menu.insert('', 'end', text="8", values=('8', 'Choco Lava Cake', '109'))
treeview_for_menu.insert('', 'end', text="9", values=('9', 'Butterscotch Mousse Cake', '103'))
treeview_for_menu.insert('', 'end', text="10", values=('10', 'Brownie Fantasy', '79'))

style = ttk.Style().configure("Treeview", rowheight=40)
treeview_for_menu.place(x=40, y=150)

generate_bill = open("Bill.txt", "w+")
generate_bill.write("You have ordered: \n")


def place_order():
    global a, b, c, d, e, f, g, h, i, j
    a = a.get()
    b = b.get()
    c = c.get()
    d = d.get()
    e = e.get()
    f = f.get()
    g = g.get()
    h = h.get()
    i = i.get()
    j = j.get()
    list = [a, b, c, d, e, f, g, h, i, j]
    bill = 0
    for i in range(len(list)):
        if i == 0:
            item = "Margherita Pizza"
            price = 109
        elif i == 1:
            item = "Farmhouse"
            price = 269
        elif i == 2:
            item = "Peppy Paneer"
            price = 269
        elif i == 3:
            item = "Garlic Bread sticks"
            price = 109
        elif i == 4:
            item = "Taco Mexican Veg"
            price = 79
        elif i == 5:
            item = "Moroccan Spice Pasta Pizza"
            price = 189
        elif i == 6:
            item = "Party Combo"
            price = 2588
        elif i == 7:
            item = "Choco Lava Cake"
            price = 109
        elif i == 8:
            item = "Butterscotch Mousse Cake"
            price = 103
        elif i == 9:
            item = "Brownie Fantasy"
            price = 79
        if list[i] > 0:
            bill = bill + price * list[i]
            r = str(list[i]) + " " + item + " "
            generate_bill.write(r)
            generate_bill.write("\n")
    generate_bill.write(("Amount to pay " + str(bill)) + '\n')
    generate_bill.close()
    path=r"D:\python\project\address.py"
    os.system(f"python {path}")


proceed = Button(main_screen, text="Proceed", font=("georgia", 20), command=place_order)
proceed.place(x=670, y=600)

main_screen.mainloop()
