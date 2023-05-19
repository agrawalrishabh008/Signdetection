from tkinter import *

def sub():
    # tkinter file for thankyou page
    import sys

    r = Tk()
    r.title('                                                   Thankyou Page')
    r.geometry("500x350")
    r.configure(bg='gray5')

    label = Label(r, text='We are very thankful to you to use our software!', bg='gray5', fg='green2', font=("Arial", 15))
    label.place(x=40, y=20)

    label = Label(r, text='Please visit again!', bg='gray5', fg='green2',
                  font=("Arial", 15))
    label.place(x=170, y=60)

    label2 = Label(r, text='Please click below button for closing the app', bg='gray5', fg='white')
    label2.place(x=130, y=200)

    my_button2 = Button(r, text="close", bg='green2', fg='gray5', command=sys.exit)     # shut down app by this button
    my_button2.place(x=215, y=230)

    r.mainloop()
