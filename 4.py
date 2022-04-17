import multiprocessing
from tkinter import *
import threading
import random
from statistics import mean
import time
from multiprocessing import Array

# Start`s parameters
CP_count = multiprocessing.cpu_count()
array_chel = []
radio_x, radio_y = 50,100
processes = []

def sus(sus_array, key,ans):
     ans[key] = (int(mean(sus_array)))
     #print(sus_array)
     print(ans)

def action():
    start = time.perf_counter()
    random_array = [random.randint(0,100) for _ in range (int(text_array.get()))]
    diff = 0
    homies = [x.get() for x in array_chel]
    ans = Array('i', range(sum(homies)))
    for x in range(sum(homies)):
        p = multiprocessing.Process(target = sus, args=(random_array[diff:diff+int(len(random_array)/sum(homies))],x,ans))
        p.start()
        processes.append(p)
        diff += int(len(random_array)/sum(homies))

    for procces in processes:
        procces.join()

    print(ans[:])
    print(mean(ans[:]))

    finish = time.perf_counter()

    print(f"Finished in {round(finish-start, 5)}")

    T.insert(END, f"Chosen processes {sum(homies)}\nAvg: {mean(ans[:])}\nTime elapsed {round(finish-start, 5)}\n")

if __name__ == '__main__':
    # # Creating form
    root = Tk()
    root.title("Лабораторна робота № 4 Палагін_Чураков_Паталашко")
    root.geometry("700x520")

    labela_0 = Label(text="Available processes", fg="blue", font="Arial 16 bold")
    labela_0.place(x=50, y=50)

    for _ in range(CP_count):
        array_chel.append(IntVar())
        array_chel[-1].set(0)
        tmp = Checkbutton(text=f"{len(array_chel)}", variable=array_chel[-1], onvalue=1, offvalue=0,
                          font="Arial 16 bold")
        tmp.place(x=radio_x, y=radio_y)
        radio_y += 50
        if radio_y == 200:
            radio_x += 50
            radio_y = 100

    labela_1 = Label(text="Size of array", fg="black", font="Arial 14 bold")
    labela_1.place(x=50, y=250)
    labela_2 = Label(text="Amount of threads", fg="black", font="Arial 14 bold")
    labela_2.place(x=50, y=300)

    text_array = Entry(root)
    text_array.place(x=240, y=255)
    text_threads = Entry(root)
    text_threads.place(x=240, y=305)

    Activator = Button(text="Calculate", font="Arial 16 bold", command=action)
    Activator.place(x=240, y=355)

    T = Text(root, height=7, width=30, font="Arial 16 bold")
    T.place(x=300, y=50)

    root.mainloop()
