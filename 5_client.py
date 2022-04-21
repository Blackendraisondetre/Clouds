from tkinter import *
import socket

root = Tk()
root.title("Лабораторна робота № 5 Палагін_Чураков_Паталашко")
root.geometry("720x280")

Label(root,text="Client", fg="blue", font="Arial 16 bold").place(x=40, y=20)

T = Text(root, height=8, width=20, font="Arial 16 bold")
T.place(x=40, y=60)

Label(root,text="Port", fg="black", font="Arial 14").place(x=300, y=70)
Label(root,text="Host", fg="black", font="Arial 14").place(x=300, y=100)
Label(root,text="Operand 1", fg="black", font="Arial 14").place(x=300, y=130)
Label(root,text="Operand 2", fg="black", font="Arial 14").place(x=300, y=160)

port = Entry(root)
port.place(x=410, y=75)
ip = Entry(root)
ip.place(x=410, y=105)
op1 = Entry(root)
op1.place(x=410, y=135)
op2 = Entry(root)
op2.place(x=410, y=165)

r_var = IntVar()
r_var.set(-1)

Radiobutton(root, text='Sum', font="Arial 10 bold", variable=r_var, value=0).place(x=300, y=200)
Radiobutton(root, text='Div', font="Arial 10 bold", variable=r_var, value=1).place(x=360, y=200)
Radiobutton(root, text='Cos', font="Arial 10 bold", variable=r_var, value=2).place(x=420, y=200)
Radiobutton(root, text='Ctng', font="Arial 10 bold", variable=r_var, value=3).place(x=480, y=200)

def connection():
    Server_PORT = int(port.get())
    Server_IP = ip.get()

    data = f'{op1.get()} {op2.get()} {r_var.get()}'

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
        connection.connect((Server_IP, Server_PORT))

        connection.send(data.encode('utf8'))
        data = connection.recv(1024)

        T.delete(1.0, END)
        T.insert(1.0, f'>>>Connected\nPort: {int(port.get())}\nHost: {ip.get()}\n{data.decode("utf-8")}')

Button(text="Connect", font="Arial 16 bold", command=connection).place(x=575, y=70)
Button(text="Disconnect", font="Arial 16 bold", command=connection).place(x=575, y=120)
Button(text="Submit", font="Arial 16 bold", command=connection).place(x=575, y=170)

root.mainloop()
