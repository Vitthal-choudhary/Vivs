from tkinter import *
from tkinter import messagebox
import os

main_screen = Tk()
main_screen.iconbitmap("logo.ico")
main_screen.title("Vivs")
main_screen.geometry("900x700")
main_screen.config(bg="black")

Label(main_screen, text="Vivs", font="arial 60 bold", bg="cyan", fg="black").pack(fill='both')
Label(main_screen, text="NAME", font="arial 20 bold", fg="blue", bd=8).place(x=150, y=200)  # LABEL 1
Label(main_screen, text="ADDRESS", font="arial 20 bold", fg="blue", bd=8).place(x=150, y=280)  # LABEL 2
Label(main_screen, text="PHONE NO", font="arial 20 bold", fg="blue", bd=8).place(x=150, y=360)  # LABEL 3

# entry boxes
NAME_value = StringVar()
ADDRESS_value = StringVar()
PHONE_NO_value = StringVar()
ent1 = Entry(main_screen, textvariable=NAME_value, font="arial 20 bold", bd=4)
ent1.place(x=400, y=200)
ent2 = Entry(main_screen, textvariable=ADDRESS_value, font="arial 20 bold", bd=4)
ent2.place(x=400, y=280)
ent3 = Entry(main_screen, textvariable=PHONE_NO_value, font="arial 20 bold", bd=4)
ent3.place(x=400, y=360)


def print_():
    if NAME_value.get() == "" or ADDRESS_value.get() == "" or PHONE_NO_value.get() == "":
        messagebox.showerror("Vivs", "Enter details correctly")
    else:
        fil = open('Bill.txt', 'a+')
        fil.write('\nOrder To be delivered at\n')
        fil.writelines(["NAME :", NAME_value.get(), '\n', "ADDRESS :", ADDRESS_value.get(), '\n', "PHONE NUMBER :",
                        PHONE_NO_value.get(), '\n'])
        fil.write('************************************************\n')
        fil.close()
        btn3['state'] = 'disable'
        path=r"D:\python\project\receipt.py"
        os.system(f"python {path}")


# buttons
btn3 = Button(main_screen, text="CONTINUE TO ORDER", font=("georgia", 20), bd=4, command=print_)
btn3.place(x=280, y=500)

main_screen.mainloop()
