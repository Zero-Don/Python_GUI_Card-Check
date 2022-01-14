from tkinter import *
from tkinter import messagebox
from os import path

win = Tk()

user_name = StringVar()
password = StringVar()
number = StringVar()
credit_card = StringVar()
address = StringVar()

def doLogin():
    global loginWindow

    if not path.exists("account.txt"):
        messagebox.showerror("Login", "No account exists")
        return

    file = open("account.txt","r")

    lines = []
    for line in file:
        lines.append(line)
    file.close()

    if (user_name.get().strip() == lines[0].rstrip() and password.get().strip() == lines[1].rstrip()):
        messagebox.showinfo("Login", "Login Successful!")
        win.wm_state('iconic')
        showMainWindow()
    else:
        messagebox.showerror("Login", "Username or password incorrect!")


def doRegister():
    global regWindow

    # write text to file
    file = open("account.txt","w")
    file.write(user_name.get()+"\n")
    file.write(password.get()+"\n")
    file.write(number.get()+"\n")
    file.write(address.get()+"\n")

    file.close()

    messagebox.showinfo(title="Registration successful", message="Registration Complete! Please login to continue.")

    # close register window
    regWindow.destroy()

def doubleNumber(num):
    result = num * 2

    if (result >= 10):
        firstPart = 1
        secondPart = result - 10
        result = firstPart + secondPart

    return result

def isCardValid(digits:str):
    if len(digits) == 0:
        return False

    digits = digits[::-1]
    evenTotal = 0
    oddTotal = 0

    # sum the double of even digits (right to left)
    even = False
    for d in digits:
        if even:
            evenTotal += doubleNumber(int(d))

        even = not even

    # sum odd digits (right to left)
    odd = True
    for d in digits:
        if odd:
            oddTotal += int(d)

        odd = not odd

    # step 4
    total = oddTotal + evenTotal

    # step 5
    if total % 10 == 0:
        return True
    return False
    
def checkCreditCard():
    if isCardValid(credit_card.get().strip()):
        messagebox.showinfo("Card Result", "Card Valid!")
    else:
        messagebox.showerror("Card Result", "Card numbers is INVALID! Please enter a valid number")
    pass


def showLoginWindow():
    win.geometry("300x400")

    Label(win, text="Username", font=("Consolas", 16)).place(x=95, y=110)
    Entry(win, width=20, textvariable=user_name, font=("Consolas", 16)).place(x=60, y=145, width=165)

    Label(win, text="Password", font=("Consolas", 16)).place(x=95, y=185)
    Entry(win, width=20, textvariable=password, font=("Consolas", 16)).place(x=60, y=220, width=165)

    Button(win, text="Register", command=showRegisterWindow, font=("Consolas", 16)).place(x=40, y=280)
    Button(win, text="Login", command=doLogin, font=("Consolas", 16)).place(x=170, y=280)


def showRegisterWindow():
    global regWindow
    win = Toplevel()
    regWindow = win

    win.geometry("300x400")

    Label(win, text="Username", font=("Consolas", 16)).place(x=95, y=35)
    Entry(win, width=20, textvariable=user_name, font=("Consolas", 12)).place(x=60, y=65, width=165)

    Label(win, text="Password", font=("Consolas", 16)).place(x=95, y=95)
    Entry(win, width=20, textvariable=password, font=("Consolas", 12)).place(x=60, y=125, width=165)

    Label(win, text="Phone Number", font=("Consolas", 16)).place(x=75, y=155)
    Entry(win, width=20, textvariable=number, font=("Consolas", 12)).place(x=60, y=185, width=165)

    Label(win, text="Address", font=("Consolas", 16)).place(x=95, y=215)
    Entry(win, width=20, textvariable=address, font=("Consolas", 12)).place(x=20, y=245, width=255)

    Button(win, text="Register", command=doRegister, font=("Consolas", 16)).place(x=80, y=295)


def showMainWindow():
    global img
    win = Toplevel()
    win.geometry("300x400")

    # menu
    menubar = Menu(win)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Help", command=showHelpWindow)
    filemenu.add_command(label="Exit", command=win.destroy)
    menubar.add_cascade(label="File", menu=filemenu)
    
    win.config(menu=menubar)

    Label(win, text="Welcome," + user_name.get(), font=("Consolas", 16)).place(x=40, y=20)

    img = PhotoImage(file="account.png")
    Label(win, bg='#FCF7E7', image=img).place(x=63, y=60, width=175, height=175)

    Label(win, text="Credit Card Checker", font=("Consolas", 16)).place(x=35, y=255)
    Entry(win, width=20, textvariable=credit_card, font=("Consolas", 12)).place(x=30, y=290, width=240)
    Button(win, text="Check", command=checkCreditCard, font=("Consolas", 14)).place(x=120, y=320)

def showHelpWindow():
    global img
    win = Toplevel()
    win.geometry("300x400")

    Label(win, text="Welcome To My Credit Card App").place(x=40, y=20)
    Message(win, text="1. Enter username and password. 2. To register, enter phone number, address then click register. 3. Enter your credit card number.").place(x = 30, y = 40, width=260, height=300)

    Button(win, text="Close", command=win.destroy, font=("Consolas", 14)).place(x=120, y=320)

win.title("Credit Card Checker")


showLoginWindow()

win.mainloop()
