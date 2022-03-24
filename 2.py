from tkinter import *
import threading

ans = [x for x in range(4)]
res = 0

root = Tk()
root.title("Лабораторна робота № 2 Палагін_Чураков_Васалатій_Паталашко")
root.geometry("500x500")

variant = {1:[110,20, "red"], 2:[160,60, "black"], 3:[170,50, "blue"], 4:[180,40, "purple"]}

canvas = Canvas()

pos_1, pos_2 = 30, 150
for x in variant.values():
    canvas.create_rectangle(pos_1+40, pos_2, pos_1+x[1]+40, pos_2+x[0], fill=x[2])
    pos_1 += 100

Counter = Label(text=f"Площа прямокутників в пікселях", fg = "black", font = "Arial 16 bold")
Counter.place(x=100,y=20)

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
    Threading[x].start()
    lab_1 = Label(text=f"{float(ans[x])}", fg=f"{variant[x+1][2]}", font="Arial 16 bold")
    lab_1.place(x=pos_1+35, y=pos_2)
    lab_0 = Label(text=f"Thread {x+1}", fg="grey", font="Arial 16")
    lab_0.place(x=pos_1 + 30, y=pos_2+30)
    pos_1 +=100

Threading[4].start()

lab_2 = Label(text=f"Thread 5", fg="grey", font="Arial 16")
lab_2.place(x=50, y=400)

lab_3 = Label(text=f"Загальна площа пікселів {float(res)}", font="Arial 16")
lab_3.place(x=150, y=400)

canvas.pack(fill=BOTH, expand=1)

root.mainloop()
