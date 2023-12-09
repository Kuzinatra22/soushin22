from tkinter import *
# звезда обозначает весь код библиотеки

#создаём окошко программы
root = Tk("Моя программа")
#вместо root можно написать любое название для переменной
#работаем с окошком
root.geometry("500x300")
#Можно ли изменять размер окна
root.resizable(width=True,height=False)
#Цвет окошка
root["bg"] = "#3ed8fa"



frame=Frame(root, padx=10,pady=10,width=200,height=200)
#Настраиваем местополоэение фрейма
frame.place(anchor="w", relx=0.5,rely=0.5)
frame["bg"] = "#d95fd5"

frame1=Frame(root, padx=10,pady=10,width=200,height=200)
frame.place(anchor="s", relx=0.5,rely=0.5)
frame1["bg"] = "#0af7c0"

frame2=Frame(root, padx=10,pady=10,width=200,height=200)
frame.place(anchor="e", relx=0.5,rely=0.5)
frame2["bg"] = "#f3f70a"










root.mainloop()