from tkinter import *

counter = 1
min,max = 0,50

def increase():
    global counter
    if counter < max:
        counter += 1
        refresh()

def decrease():
    global counter
    if counter > min:
        counter -= 1
        refresh()

root = Tk()
root.title("Лабораторна робота № 1 Палагін_Чураков_Васалатій_Паталашко")
root.geometry("900x500")

r_var = IntVar()
r_var.set(-1)

radio_1 = Radiobutton(text='RadioButton 1',variable=r_var, value=0, font = "Arial 16 bold")
radio_2 = Radiobutton(text='RadioButton 2',variable=r_var, value=1, font = "Arial 16 bold")
radio_3 = Radiobutton(text='RadioButton 3',variable=r_var, value=2, font = "Arial 16 bold")

chel_1 = BooleanVar()
chel_2 = BooleanVar()
chel_3 = BooleanVar()

chel_1.set(0)
chel_2.set(0)
chel_3.set(0)

check_1 = Checkbutton(text="CheckBox 1", variable=chel_1, onvalue = 1, offvalue = 0, font = "Arial 16 bold")
check_2 = Checkbutton(text="CheckBox 2", variable=chel_2, onvalue = 1, offvalue = 0, font = "Arial 16 bold")
check_3 = Checkbutton(text="CheckBox 3", variable=chel_3, onvalue = 1, offvalue = 0, font = "Arial 16 bold")

T = Text(root, height = 4, width = 35, font = "Arial 16 bold")
T.insert(1.0,f"Лабороторна робота № 1\nЛічильник: {counter}")

Counter = Label(text=f"Лічильник: {counter}", fg = "blue", font = "Arial 16 bold")

btn_1 = Button(text="Збільшити", font = "Arial 16 bold", command=increase)
btn_2 = Button(text="Зменшити", font = "Arial 16 bold", command=decrease)

scaler = IntVar()
scaler.set(counter)

def onScale(self, val):
    v = int(float(val))
    self.var.set(v)

radio_1.place(x=25,y=10)
radio_2.place(x=25,y=50)
radio_3.place(x=25,y=90)

check_1.place(x=250,y=10)
check_2.place(x=250,y=50)
check_3.place(x=250,y=90)

T.place(x=450,y=10)

Counter.place(x=25,y=150)

btn_1.place(x=25,y=200)
btn_2.place(x=175,y=200)

def refresh():
    T.delete(1.0,END)
    T.insert(1.0, f"Лабороторна робота № 1\nЛічильник: {counter}")
    Counter["text"]= f"Лічильник: {counter}"
    scaler.set(counter)

def onscale(var):
    global counter
    counter = int(var)
    refresh()

scale = Scale(from_=0, to=50, font = "Arial 16 bold", orient = HORIZONTAL, length = 300, variable = scaler, command = onscale)
scale.place(x = 500, y = 150)

root.mainloop()
