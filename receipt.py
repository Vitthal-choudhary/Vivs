from tkinter import *
import random

receipt_window = Tk()
receipt_window.iconbitmap("logo.ico")
receipt_window.title("Vivs")
receipt_window.geometry("900x700")
receipt_window.config(bg="black")
riders_details = [("Nishant", "+91 8420157520"), ("Raghav", "+91 9452136050"),
                  ("Mohan", "+91 9925600350"), ("Sohan", "+91 7015240650"),
                  ("Ravi", "+91 8024510630"), ("Arpit", "+91 7201546020")]
x = random.randrange(0, len(riders_details))
detail = (riders_details[x][0], riders_details[x][1])

receipt = Label(receipt_window, text="Thanks for using Vivs \n Your order will be delivered by :-", bg="white", fg="red", font=("Comic Sans MS", 30))
receipt.place(x=140, y=50)

rider = Label(receipt_window, text=detail, bg="white", fg="red", font=("Comic Sans MS", 30))
rider.place(x=220, y=200)

with open('Bill.txt', 'r') as fil:
    rcpt = fil.read()
    rcpt_label = Label(receipt_window, text=rcpt, bg="white", fg="red", font=('cosmic sans', 15))
    rcpt_label.place(x=260, y=300)
receipt_window.mainloop()
