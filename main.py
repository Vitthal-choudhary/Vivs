from tkinter import *
from PIL import Image, ImageTk
import os

main_screen = Tk()
main_screen.iconbitmap("logo.ico")
main_screen.title("Vivs")
main_screen.geometry("900x700")
main_screen.config(bg="black")

label_on_main = Label(main_screen, text='Welcome to Vivs', bg="black", fg="cyan", font=("ALGERIAN", 50))
label_on_main.place(x=170, y=50)

logo_img = ImageTk.PhotoImage(Image.open("logo.png"))
logo_on_screen = Label(main_screen, image=logo_img)
logo_on_screen.place(x=270, y=180)

# photos for restaurant screen buttons
madras_cafe = ImageTk.PhotoImage(Image.open("MADRAS cafe.jpg"))
dominos = ImageTk.PhotoImage(Image.open("dominos.jpg"))
sukhdev = ImageTk.PhotoImage(Image.open("AS.jpg"))
barista = ImageTk.PhotoImage(Image.open("barista.jpg"))


def press_button():
    global main_screen
    global madras_cafe, dominos, sukhdev, barista
    for widget in main_screen.winfo_children():
        widget.destroy()
    main_screen.title("Vivs")
    main_screen.geometry("900x700")

    main_screen.config(bg="black")

    def third_screen(value):
        if value == 1:
            path=r"D:\python\project\madras.py"
            os.system(f"python {path}")
        if value == 2:
            path=r"D:\python\project\dominos.py"
            os.system(f"python {path}")
        if value == 3:
            path=r"D:\python\project\sukhdev.py"
            os.system(f"python {path}")
        if value == 4:
            path=r"D:\python\project\barista.py"
            os.system(f"python {path}")

    madras_button = Button(main_screen, image=madras_cafe, command=lambda: third_screen(1))
    madras_button.place(x=20, y=20)
    domino_button = Button(main_screen, image=dominos, command=lambda: third_screen(2))
    domino_button.place(x=20, y=370)
    sukhdev_button = Button(main_screen, image=sukhdev, command=lambda: third_screen(3))
    sukhdev_button.place(x=570, y=20)
    barista_button = Button(main_screen, image=barista, command=lambda: third_screen(4))
    barista_button.place(x=570, y=370)


button1 = Button(main_screen, text="start ordering", bg='black', fg='cyan', font=("georgia", 40), command=press_button)
button1.place(x=270, y=480)

main_screen.mainloop()
