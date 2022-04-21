from tkinter import *
import threading
import socket

variant = {1: [110, 20, "red"],
           2: [160, 60, "black"],
           3: [170, 50, "blue"],
           4: [180, 40, "purple"]}

ip = '127.0.0.1'
port = 8000
res = 0
ArrayAnswer = [x for x in range(4)]

LocationMainInfoX, LocationMainInfoY = 160, 20
TotalThreadLabelX, TotalThreadLabelY = 130, 400
TotalInfoX, TotalInfoY = 230, 400
RadioButtonShiftX = 65
ArrayLabel,ArrayCanvas = [],[]
CanvasShiftX, CanvasShiftY = 30, 150
canvas, TotalInfo = 0, 0

def interface():
    global T, ArrayLabel,ArrayCanvas, CanvasShiftX, CanvasShiftY, canvas, TotalInfo
    LabelShiftX, LabelShiftY = 30, 80

    root = Tk()
    root.title("Лабораторна робота № 6 Палагін_Чураков")
    root.geometry("950x540")

    # # Creating Total info label
    TotalInfo = Label(text=f"Загальна площа пікселів {float(res)}", font="Arial 16")
    TotalInfo.place(x=TotalInfoX, y=TotalInfoY)

    # Start form
    # # Creating Main info label
    MainInfo = Label(root, text=f"Площа прямокутників в пікселях", fg="black", font="Arial 16 bold")
    MainInfo.place(x=LocationMainInfoX, y=LocationMainInfoY)

    # # Creating arrays of elements
    # # # Creating array of canvases
    canvas = Canvas()
    ArrayCanvas = []
    for x in variant.values():
        ArrayCanvas.append(canvas.create_rectangle(CanvasShiftX + 40,
                                                   CanvasShiftY,
                                                   CanvasShiftX + 100,
                                                   CanvasShiftY + 10,
                                                   fill=x[2]))
        CanvasShiftX += 150
    CanvasShiftX, CanvasShiftY = 30, 150

    # # # Creating array of labels
    for x in range(len(variant)):
        ArrayLabel.append(Label(text=f"1", fg=f"{variant[x + 1][2]}", font="Arial 16 bold"))

    # # Creating labels and thread info labels
    for x in range(len(variant)):
        ArrayLabel[x].place(x=LabelShiftX + 35, y=LabelShiftY)

        ThreadInfoLabel = Label(text=f"Thread {x + 1}", fg="grey", font="Arial 16")
        ThreadInfoLabel.place(x=LabelShiftX + 30, y=LabelShiftY + 30)

        LabelShiftX += 150

    # # Creating Canvases
    canvas.pack(fill=BOTH, expand=1)

    # # Creating total thread label
    TotalThreadLabel = Label(text=f"Thread 5", fg="grey", font="Arial 16")
    TotalThreadLabel.place(x=130, y=400)

    # # Creating Total info label
    TotalInfo = Label(text=f"Загальна площа пікселів {float(res)}", font="Arial 16")
    TotalInfo.place(x=TotalInfoX, y=TotalInfoY)

    Label(root,text=f"Server:Port:{port}", fg="blue", font="Arial 16 bold").place(x=630, y=20)

    T = Text(root, height=8, width=20, font="Arial 16 bold")
    T.place(x=630, y=60)

    root.mainloop()

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

def act(answer):
    global CanvasShiftX, CanvasShiftY, res, ArrayLabel, ArrayCanvas, TotalInfo, ArrayAnswer, variant, canvas

    ArrrayChanges = []

    for x in range(len(answer)):
        if answer[x] == 'True':
            print(answer[x])
            ArrrayChanges.append(1)

            thread = threading.Thread(target=calc,
                                      args=(variant[x + 1][0],
                                            variant[x + 1][1], x),
                                      name=f"thr-{x + 1}")
            thread.start()

            ArrayLabel[x]['text'] = ArrayAnswer[x]
            canvas.coords(ArrayCanvas[x],
                          CanvasShiftX + 40,
                          CanvasShiftY,
                          CanvasShiftX + 40 + variant[x + 1][1],
                          CanvasShiftY + variant[x + 1][0])
        else:
            ArrrayChanges.append(0)

            ArrayLabel[x]['text'] = ""
            canvas.coords(ArrayCanvas[x],
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

    return str(res)

def server():
    global T

    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    listener.bind((ip, port))
    listener.listen(1)

    connection, address = listener.accept()
    T.delete(1.0, END)
    T.insert(1.0, f'>>>Connected\n {str(address)}\n')

    data = connection.recv(1024)

    answer = data.decode("utf-8").split()

    print(answer)

    ans = act(answer)

    for x in range(len(variant)):
        ans += ' '
        if answer[x] == 'True':
            ans += str(variant[x + 1][0]*variant[x + 1][1])
        else:
            ans += '0'

    T.insert(3.0, ans)
    connection.send(str(ans).encode("utf-8"))
    connection.close()

if __name__ == "__main__":
    threading.Thread(target=interface, daemon=True).start()
    while True:
        server()
