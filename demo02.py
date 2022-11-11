from tkinter import *
def click1():
    if label1["text"]== "0":
        label1["text"] = "1"
    else:
        label1["text"] += "1"

    #label1["text"]+=" 1"

form1= Tk ()
W,H = 700, 700
L,T=(form1.winfo_screenwidth()-W)//2,(form1.winfo_screenheight()-H)//2
form1.geometry (f"{W}x{H}+{L}+{T}")
form1.title ("Calc")
label1= Label(text="0")
label1.place (x=5,y=5)
Button (text="Tap me, bro, do it", command= click1).place(x=30,y=30)
form1.mainloop()