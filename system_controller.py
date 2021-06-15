from user_account import UserAccount
from tkinter import *
import tkinter.font as tkFont


class Controller(UserAccount):

    def __init__(self, name, email, password, balance, withdraw, deposit):
        super().__init__(name, email, password, balance, withdraw, deposit)
        self.__email = email
        self.__password = password

    def choose(self, email, password):
        self.__email = email
        self.__password = password


def run_login():
    screen.destroy()
    obj = Controller("", "", "", "", "", "")
    obj.user_login('y')


def run_open():
    screen.destroy()
    obj = Controller("", "", "", "", "", "")
    obj.user_login('n')


screen = Tk()
screen.title("BANKING SYSTEM")
screen.geometry("500x300")

bg = PhotoImage(file="files/bg_image.jpg")
label1 = Label( screen, image=bg)
label1.place(x=-5, y=0)

fontStyle = tkFont.Font(family="Lucida Grande", size=20)
fontStyle_result = tkFont.Font(family="Lucida Grande", size=20)
welcome_text = Label(text = "BANKING SYSTEM", fg = "blue", bg = "violet", font=fontStyle)
welcome_text.place(x=140, y=2)


pre_button_font = tkFont.Font(family="Helvetica", size=15, weight="bold")
click = Button(text = "Login", fg = "red", bg = "aqua", relief="raised", font=pre_button_font, command=run_login)
click.place(x=220, y=100)

click = Button(text = "Open Account", fg = "red", bg = "aquamarine", relief="raised", font=pre_button_font, command=run_open)
click.place(x=180, y=150)

screen.mainloop()
