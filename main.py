# Code by Sadman Sakib
# Libraries
from tkinter import *
from tkinter.ttk import *
from time import strftime

# Creating UI
root = Tk()
root.title('Sakib\'s Clock')


# Main Function
def time():
    string = strftime('%H:%M:%S  %p')
    label.config(text=string)
    label.after(1000, time)


# Font, Background, Foreground
label = Label(root, font=('ds-digital', 80), background='#0d0d0d', foreground='pink')
label.pack(anchor='center')


# Calling functions

time()
mainloop()
