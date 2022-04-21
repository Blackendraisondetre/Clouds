from tkinter import *
import socket

root = Tk()
root.title("Лабораторна робота № 6 Палагін_Чураков")
root.geometry("720x320")
ans = 0
ArrayRadioButton = []


for x in range(4):
    ArrayRadioButton.append(BooleanVar())
    ArrayRadioButton[-1].set(0)

Label(root,text="Client", fg="blue", font="Arial 16 bold").place(x=40, y=20)

T = Text(root, height=4, width=20, font="Arial 16 bold")
T.place(x=40, y=60)

Label(root,text="Port", fg="black", font="Arial 10").place(x=300, y=70)
Label(root,text="Host", fg="black", font="Arial 10").place(x=300, y=100)
Label(root,text="Thread 1", fg="black", font="Arial 10").place(x=300, y=180)
Label(root,text="Thread 2", fg="black", font="Arial 10").place(x=380, y=180)
Label(root,text="Thread 3", fg="black", font="Arial 10").place(x=460, y=180)
Label(root,text="Thread 4", fg="black", font="Arial 10").place(x=540, y=180)
Label(root,text="Загальна площа пікселів", fg="black", font="Arial 10").place(x=40, y=200)
Label(root,text=f"{ans}", fg="black", font="Arial 10").place(x=115, y=230)
Label(root,text="Площа прямокутників ", fg="black", font="Arial 10").place(x=40, y=270)



port = Entry(root)
port.place(x=410, y=75)
ip = Entry(root)
ip.place(x=410, y=105)



RadioButtonShiftX = 300
# # Creating RadioButtons
for x in range(len(ArrayRadioButton)):
    RadioButtonStart = Radiobutton(text='Yes', variable=ArrayRadioButton[x], value=1, font="Arial 12")
    RadioButtonCancel = Radiobutton(text='No', variable=ArrayRadioButton[x], value=0, font="Arial 12")

    RadioButtonStart.place(x=RadioButtonShiftX, y=200)
    RadioButtonCancel.place(x=RadioButtonShiftX, y=220)

    RadioButtonShiftX += 80


def connection():
    Server_PORT = int(port.get())
    Server_IP = ip.get()

    data = f'{ArrayRadioButton[0].get()} {ArrayRadioButton[1].get()} {ArrayRadioButton[2].get()} {ArrayRadioButton[3].get()}'

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
        connection.connect((Server_IP, Server_PORT))

        connection.send(data.encode('utf8'))
        data = connection.recv(1024)

        ans = data.decode("utf-8")
        ans = ans.split(' ')

        print(ans)

        T.delete(1.0, END)
        T.insert(1.0, f'>>>Connected\nPort: {int(port.get())}\nHost: {ip.get()}\n{ans[0]}')

        Label(root, text=f"{ans[0]}", fg="black", font="Arial 10 bold").place(x=115, y=230)
        Label(root, text=f"{ans[1]}", fg="red", font="Arial 10 bold").place(x=300, y=250)
        Label(root, text=f"{ans[2]}", fg="black", font="Arial 10 bold").place(x=380, y=250)
        Label(root, text=f"{ans[3]}", fg="blue", font="Arial 10 bold").place(x=460, y=250)
        Label(root, text=f"{ans[4]}", fg="purple", font="Arial 10 bold").place(x=540, y=250)

Button(text="Connect", font="Arial 16 bold", command=connection).place(x=575, y=70)
Button(text="Disconnect", font="Arial 16 bold", command=connection).place(x=575, y=120)

root.mainloop()
