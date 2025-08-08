import time

import tkinter as tk

def my_clock():
    # local_time = time.localtime()
    day = time.strftime("%a")
    d_label.config(text=day)
    current_time = time.strftime("%H : %M : %S")
    time_label.config(text=current_time)
    root.after(1000,my_clock)

def what_to_say():
    current_hr = int(time.strftime("%H"))

    if 6 < current_hr < 12:
        wts_label.config(text="Good Morning")
    elif 12 <= current_hr < 18:
        wts_label.config(text="Good Afternoon")
    elif 18 <= current_hr < 20:
        wts_label.config(text="Good Evening")
    else:
        wts_label.config(text="Good Night")


root = tk.Tk()
root.title("Clock")
root.geometry("600x400") 
root.configure(bg="black") 
root.resizable(False, False)   

d_label = tk.Label(root,text="sdsd", font=("Arial",20,"bold"), fg="lightgreen", bg="black")
d_label.place(x=30,y=55)

time_label = tk.Label(root,text="", font=("Arial",65,"bold"), fg="lightgreen", bg="black", relief="ridge")
time_label.pack(pady= 100)

wts_label = tk.Label(root,text="", font=("Arial",25,"bold"), fg="lightgreen", bg="black")
wts_label.place(x=175,y=250)

what_to_say()
my_clock()
root.mainloop()
