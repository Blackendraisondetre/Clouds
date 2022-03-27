from tkinter import *
import threading

ans = [x for x in range(4)]
res = 0

root = Tk()
root.title("Лабораторна робота № 3 Палагін_Чураков_Васалатій_Паталашко")
root.geometry("650x600")

variant = {1:[110,20, "red"], 2:[160,60, "black"], 3:[170,50, "blue"], 4:[180,40, "purple"]}

canvas = Canvas()

pos_1, pos_2 = 30, 150
for x in variant.values():
    canvas.create_rectangle(pos_1+40, pos_2, pos_1+100, pos_2+10, fill=x[2])
    pos_1 += 150

Counter = Label(text=f"Площа прямокутників в пікселях", fg = "black", font = "Arial 16 bold")
Counter.place(x=160,y=20)

def calc(a,b,index):
    global ans
    ans[index] = a*b

def fin(ans):
    global res
    res = sum(ans)

Threading = [threading.Thread(target = calc, args=(values[0],values[1], keys-1), name=f"thr-{keys}") for keys,values in variant.items()]
Threading.append(threading.Thread(target = fin, args=[ans], name="thr-5"))

pos_1, pos_2 = 30, 80

for x in range(len(variant)):
    #Threading[x].start()
    lab_1 = Label(text=f"", fg=f"{variant[x+1][2]}", font="Arial 16 bold")
    lab_1.place(x=pos_1+35, y=pos_2)
    lab_0 = Label(text=f"Thread {x+1}", fg="grey", font="Arial 16")
    lab_0.place(x=pos_1 + 30, y=pos_2+30)
    pos_1 +=150

#Threading[4].start()

lab_2 = Label(text=f"Thread 5", fg="grey", font="Arial 16")
lab_2.place(x=130, y=400)

lab_3 = Label(text=f"Загальна площа пікселів {float(res)}", font="Arial 16")
lab_3.place(x=230, y=400)

canvas.pack(fill=BOTH, expand=1)

r_var = []
pos_1 = 65

def act():
    for x in range(len(r_var)):
        if r_var[x]:
            pass

for x in range(len(variant)):
    r_var.append(BooleanVar())
    r_var[-1].set(0)

    radio_1 = Radiobutton(text='Start', variable=r_var[-1], value=1, font="Arial 12", command=act)
    radio_2 = Radiobutton(text='Cancel', variable=r_var[-1], value=0, font="Arial 12", command=act)

    radio_1.place(x=pos_1, y=500)
    radio_2.place(x=pos_1, y=540)

    pos_1 += 150











root.mainloop()
