from tkinter import *
from test import sepm
from subsoftware1 import sub


def kill():
    root.destroy()
    sub()

root = Tk()
root.title('                          Software Engineering and Project Management')
root.geometry("500x350")
root.configure(bg='gray5')

label = Label(root, text='Sign Language Detection Software!', bg='gray5', fg='green2', font=("Arial", 20))
label.place(x=40, y=20)

label0 = Label(root, text='Please click below button for starting the video feed', bg='gray5', fg='white')
label0.place(x=115, y=80)

my_button1 = Button(root, text="start app", bg='green2', fg='black', command=sepm) #calls the sepm function thus running the software
my_button1.place(x=215, y=110)

label1 = Label(root, text="Please long press 'X' on keyboard to stop video feed", bg='gray5', fg='white')
label1.place(x=115, y=150)   # gives control to closing app function in test.py file

label2 = Label(root, text='Please click below button for exiting the app', bg='gray5', fg='white')
label2.place(x=130, y=200)

my_button2 = Button(root, text="exit app", bg='green2', fg='gray5', command=kill )
# calls the thankyou function thus calling another tkinter file.
my_button2.place(x=215, y=230)

root.mainloop()