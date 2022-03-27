from tkinter import *
import threading

# Start`s parameters
ArrayAnswer = [x for x in range(4)]
res = 0

# # Creating form
root = Tk()
root.title("Лабораторна робота № 3 Палагін_Чураков_Васалатій_Паталашко")
root.geometry("650x540")

# # Creating data of each variant
variant = {1: [110, 20, "red"],
           2: [160, 60, "black"],
           3: [170, 50, "blue"],
           4: [180, 40, "purple"]}

# # Creating properties
CanvasShiftX, CanvasShiftY = 30, 150
LocationMainInfoX, LocationMainInfoY = 160, 20
LabelShiftX, LabelShiftY = 30, 80
TotalThreadLabelX, TotalThreadLabelY = 130, 400
TotalInfoX, TotalInfoY = 230, 400
RadioButtonShiftX = 65

# # Creating arrays of elements
# # # Creating array of canvases
Canvas = Canvas()
ArrayCanvas = []
for x in variant.values():
    ArrayCanvas.append(Canvas.create_rectangle(CanvasShiftX + 40,
                                               CanvasShiftY,
                                               CanvasShiftX + 100,
                                               CanvasShiftY + 10,
                                               fill=x[2]))
    CanvasShiftX += 150
CanvasShiftX, CanvasShiftY = 30, 150

# # # Creating array of labels
ArrayLabel = []
for x in range(len(variant)):
    ArrayLabel.append(Label(text=f"1", fg=f"{variant[x + 1][2]}", font="Arial 16 bold"))

# # # Creating array of threads
def calc(a, b, index):
    global ArrayAnswer
    ArrayAnswer[index] = float(a * b)

def fin(list):
    global res
    Sum = 0.0

    for x in range(len(list)):
        if list[x]:
            Sum += float(variant[x + 1][0] * variant[x + 1][1])
    res = Sum

#ArrayThread = [threading.Thread(target = calc, args=(values[0], values[1], keys - 1), name=f"thr-{keys}") for keys, values in variant.items()]
#ArrayThread.append(threading.Thread(target=fin, args=[ArrayAnswer], name="thr-5"))

# # # Creating array of RadioButtons
ArrayRadioButton = []

def act():
    global CanvasShiftX, CanvasShiftY, res

    ArrrayChanges = []

    for x in range(len(ArrayRadioButton)):
        if ArrayRadioButton[x].get():
            ArrrayChanges.append(1)

            thread = threading.Thread(target=calc,
                                      args=(variant[x + 1][0],
                                            variant[x + 1][1], x),
                                      name=f"thr-{x + 1}")
            thread.start()

            ArrayLabel[x]['text'] = ArrayAnswer[x]
            Canvas.coords(ArrayCanvas[x],
                          CanvasShiftX + 40,
                          CanvasShiftY,
                          CanvasShiftX + 40 + variant[x + 1][1],
                          CanvasShiftY + variant[x + 1][0])
        else:
            ArrrayChanges.append(0)

            ArrayLabel[x]['text'] = ""
            Canvas.coords(ArrayCanvas[x],
                          CanvasShiftX + 40,
                          CanvasShiftY,
                          CanvasShiftX + 100,
                          CanvasShiftY + 10,)
        CanvasShiftX += 150

    thread = threading.Thread(target=fin,
                              args=([ArrrayChanges]),
                              name=f"thr-fin")
    thread.start()

    TotalInfo["text"] = f"Загальна площа пікселів {res}"

    CanvasShiftX, CanvasShiftY = 30, 150


for x in range(len(variant)):
    ArrayRadioButton.append(BooleanVar())
    ArrayRadioButton[-1].set(0)

# Start form
# # Creating Main info label
MainInfo = Label(text=f"Площа прямокутників в пікселях", fg="black", font="Arial 16 bold")
MainInfo.place(x=LocationMainInfoX, y=LocationMainInfoY)

# # Creating labels and thread info labels
for x in range(len(variant)):
    ArrayLabel[x].place(x=LabelShiftX + 35, y=LabelShiftY)

    ThreadInfoLabel = Label(text=f"Thread {x + 1}", fg="grey", font="Arial 16")
    ThreadInfoLabel.place(x=LabelShiftX + 30, y=LabelShiftY + 30)

    LabelShiftX += 150

# # Creating Canvases
Canvas.pack(fill=BOTH, expand=1)

# # Creating total thread label
TotalThreadLabel = Label(text=f"Thread 5", fg="grey", font="Arial 16")
TotalThreadLabel.place(x=130, y=400)

# # Creating Total info label
TotalInfo = Label(text=f"Загальна площа пікселів {float(res)}", font="Arial 16")
TotalInfo.place(x=TotalInfoX, y=TotalInfoY)

# # Creating RadioButtons
for x in range(len(ArrayRadioButton)):
    RadioButtonStart = Radiobutton(text='Start', variable=ArrayRadioButton[x], value=1, font="Arial 12", command=act)
    RadioButtonCancel = Radiobutton(text='Cancel', variable=ArrayRadioButton[x], value=0, font="Arial 12", command=act)

    RadioButtonStart.place(x=RadioButtonShiftX, y=450)
    RadioButtonCancel.place(x=RadioButtonShiftX, y=490)

    RadioButtonShiftX += 150

root.mainloop()
