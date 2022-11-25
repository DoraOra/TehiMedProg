from tkinter import *
def saveToFile():
    S=text1.get(1.0,"end")
    with open(file="Stydents.txt",mode='w',encoding="utf-8") as F:
        F.write(S)

form1= Tk ()
form1.geometry("500x500+400+200")
text1=Text()
text1.place(x=5,y=5,width=290,height=250)
for i in range(10):
    S=str(i)+"-Студент"
    text1.insert("end",S+'\n')

Button(text="Сохранить список",command=saveToFile).place(x=5,y=260)
form1.mainloop()