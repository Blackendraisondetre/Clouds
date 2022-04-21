from tkinter import *
import threading
import socket
from math import tan,sin

ip = '127.0.0.1'
port = 8000

def interface():
    global T

    root = Tk()
    root.title("Лабораторна робота № 5 Палагін_Чураков_Паталашко")
    root.geometry("320x280")

    Label(root,text=f"Server:Port:{port}", fg="blue", font="Arial 16 bold").place(x=40, y=20)

    T = Text(root, height=8, width=20, font="Arial 16 bold")
    T.place(x=40, y=60)

    root.mainloop()

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

    answer = [int(x) for x in answer]

    ans = 0

    if answer[2] == 0:
        ans = answer[0] + answer[1]
    elif answer[2] == 1:
        ans = answer[0]/answer[1]
    elif answer[2] == 2:
        ans = sin(answer[0]/answer[1])
    elif answer[2] == 3:
        ans = 1 / tan(answer[0]/answer[1])

    T.insert(3.0, ans)
    connection.send(str(ans).encode("utf-8"))
    connection.close()

if __name__ == "__main__":
    threading.Thread(target=interface, daemon=True).start()
    while True:
        server()
