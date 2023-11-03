import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Clock")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = tk.Label(root, font=("calibri", 40, "bold"), background="white", foreground="black")
label.pack(anchor='center')

time()
root.mainloop()