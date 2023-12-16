from tkinter import *
# звезда обозначает весь код библиотеки

def Anykey():
    print("ПУНКТ 5 ЗАМИНИРОВАТЬ КНОПКУ")
    Label.configure(text="text")
Anykey()

root = Tk("Моя программа")
#вместо root можно написать любое название для переменной



frame=Frame(root, padx=10,pady=10)
frame.grid()
Label(frame,text="Римская пять").grid(column=0,row=0)

Label(frame,text="Я манипулятор").grid(column=1,row=2)
button=Button(frame,text="создать half life 3",width=15,height=15,command=Anykey)


button.grid(column=1,row=2)

button2 = Button(frame,text="в",background="#566bba",
foreground="#8a2bc4",width=10,height=3,wraplength=100)
button2.grid(column=0,row=2)      













root.mainloop()