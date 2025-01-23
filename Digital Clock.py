import tkinter as tk
from time import strftime

#Create the root window
root=tk.Tk()
root.title("Digital Clock")

#Define the clock update function
def time():
    #get the current time format
    string=strftime('%H:%M:%S %p')
    
    #Update the label with the current time
    label.config(text=string)

    #Call the time function every 1000 mileseconds(1 sec)
    label.after(1000,time)

#Set the label for displaying time with custom font and colors
label=tk.Label(root,font=('calibri',50,'bold'),background='pink',foreground='black')
label.pack(anchor='center')

#Start the clock function
time()

#Start the tkinter event loop
root.mainloop()