from user_implementation import UserImpl
from tkinter import *
import tkinter.font as tkFont


class UserAccount(UserImpl):

    def __init__(self, name, email, password, balance, withdraw, deposit):
        super(UserAccount, self).__init__(user_name=name, user_email=email, user_password=password)
        self.__balance = balance = 0.0
        self.__withdraw = withdraw = 0.0
        self.__deposit = deposit = 0.0

    def user_balance(self, email, password):
        #print("Account Balance", self.__balance)
        self.__user_email = email
        self.__user_password = password
        print("Personal Details:")
        user_info = UserAccount("", self.__user_email, self.__user_password, "", "", "")
        filename = user_info.get_user_email() + user_info.get_user_password()
        read_file = open(filename + '.txt', "r")
        value = read_file.read()
        words = value.split()
        (a, b, c) = words
        details_balance = "Current Balance: " + str(c) + "      "
        return details_balance


    def user_deposit(self, amount, email, password):

        self.amount = float(amount)
        self.email = email
        self.password = password
        self.__balance = self.__balance + self.amount
        filename = self.email + self.password
        read_file = open(filename + '.txt', "r")
        value = read_file.read()
        text = value
        words = text.split()
        try:
            (a, b) = words
        except ValueError:
            try:
                (a, b, c) = words
            except ValueError:
                print("Less Value Detected")
        if c != "" or c != " ":
            money = float(c)
            self.__balance = self.amount + money

        if self.amount >= 0:
            value = value.rsplit(' ', 1)[0]
            total = str(value) + " " + str(self.__balance)
            file = open(filename + '.txt', "w+")
            file.write(total)
            file.close()
            print("Account balance has been updated : ", self.__balance)
            return self.__balance

    def user_withdraw(self, amount, email, password):
        self.amount = float(amount)
        self.email = email
        self.password = password
        filename = self.email + self.password

        read_file = open(filename + '.txt', "r")
        value = read_file.read()
        text = value
        words = text.split()
        try:
            (a, b) = words
        except ValueError:
            try:
                (a, b, c) = words
            except ValueError:
                print("Less Value Detected")
        if c != "" or c != " ":
            money = float(c)
            self.__balance = money - self.amount

        if self.amount > self.__balance:
            print("Insufficient Funds | Balance Available : ", self.__balance)
        else:
            filename = self.email + self.password
            read_file = open(filename + '.txt', "r")
            value = read_file.read()
            value = value.rsplit(' ', 1)[0]
            total = str(value) + " " + str(self.__balance)
            file = open(filename + '.txt', "w+")
            file.write(total)
            file.close()
            print("Account balance has been updated : ", self.__balance)
            return self.__balance

    def user_login(self, acnt):

        if acnt == 'y':

            def login():
                email = self.set_user_email(email = email_storage.get())
                password = self.set_user_password(password=password_storage.get())
                temp = email + password
                with open("mydata.txt") as f:
                    if temp in f.read():
                        print("Login Success")
                        new_text = Label(text="Login Successful", fg="green", bg="white", font=fontStyle_result)
                        new_text.place(x=120, y=240)
                        obj = UserAccount("", "", "", "", "", "")
                        root.destroy()
                        obj.main_control(email, password)


                        # obj = UserAccount("", "", "", "", "", "")
                        # obj.user_deposit(input("Enter Deposit Amount"), email, password)
                        # obj.user_withdraw(input("Enter Withdraw Amount"), email, password)
                        # obj.show_details(email, password)

                        # return email, password
                    else:
                        new_text = Label(text="Wrong Email or Password", fg="green", bg="white", font=fontStyle_result)
                        new_text.place(x=120, y=240)
            # print("Login into your account ")
            root = Tk()
            root.title("BANKING SYSTEM-LOGIN")
            root.geometry("500x300")
            bg1 = PhotoImage(file="files/login.jpg")
            label = Label(root, image=bg1)
            label.place(x=-5, y=0)
            fontStyle = tkFont.Font(family="Lucida Grande", size=20)
            fontStyle_result = tkFont.Font(family="Lucida Grande", size=20)
            text_area_font = tkFont.Font(family="Courier", size=12, weight="bold")
            text_input_font = tkFont.Font(family="Courier", size=13, weight="bold")
            welcome_text = Label(text="LOGIN WINDOW", fg="blue", bg="violet", font=fontStyle)
            welcome_text.place(x=140, y=2)

            email_text = Label(text="Enter Your Email: ", bg='darkslateblue', fg='white', font=text_area_font)
            email_text.place(x=50, y=80)

            email_storage = StringVar()
            email = Entry(textvariable=email_storage, bg='aquamarine', fg='black', font=text_input_font)
            email.place(x=250, y=80)

            password_text = Label(text="Enter Your Password: ", bg='darkslateblue', fg='white', font=text_area_font)
            password_text.place(x=50, y=140)

            password_storage = StringVar()
            password = Entry(textvariable=password_storage, bg='aquamarine', fg='black', font=text_input_font)
            password.place(x=250, y=140)

            pre_button_font = tkFont.Font(family="Helvetica", size=15, weight="bold")
            click = Button(text="Login", fg="red", bg="aqua", relief="raised", font=pre_button_font, command=login)
            click.place(x=220, y=180)
            root.mainloop()
        else:

            def open_func():
                print("This is Account Opening")
                name = self.set_user_name(name=name_storage.get())
                email = self.set_user_email(email=email_storage.get())
                password = self.set_user_password(password=password_storage.get())

                acc = UserImpl("", "", "")
                value = acc.open_user_account(name, email, password)
                (email, password, message) = value
                new_text = Label(text=message, fg="green", bg="white", font=fontStyle_result)
                new_text.place(x=10, y=310)
                obj = UserAccount("", "", "", "", "", "")
                screen.destroy()
                obj.main_control(email, password)

                # return email, password, message

            screen = Tk()
            screen.title("BANKING SYSTEM-OPEN ACCOUNT")
            screen.geometry("500x400")

            bg = PhotoImage(file="files/open.jpg")
            label1 = Label(screen, image=bg)
            label1.place(x=-5, y=0)

            fontStyle = tkFont.Font(family="Lucida Grande", size=20)
            fontStyle_result = tkFont.Font(family="Lucida Grande", size=20)
            text_area_font = tkFont.Font(family="Courier", size=12, weight="bold")
            text_input_font = tkFont.Font(family="Courier", size=13, weight="bold")
            welcome_text = Label(text="OPEN ACCOUNT", fg="blue", bg="violet", font=fontStyle)
            welcome_text.place(x=140, y=2)

            name_text = Label(text="Enter Your Name: ", bg='darkslateblue', fg='white', font=text_area_font)
            name_text.place(x=50, y=80)

            name_storage = StringVar()
            name = Entry(textvariable=name_storage, bg='aquamarine', fg='black', font=text_input_font)
            name.place(x=250, y=80)

            email_text = Label(text="Enter Your Email: ", bg='darkslateblue', fg='white', font=text_area_font)
            email_text.place(x=50, y=140)

            email_storage = StringVar()
            email = Entry(textvariable=email_storage, bg='aquamarine', fg='black', font=text_input_font)
            email.place(x=250, y=140)

            password_text = Label(text="Enter Your Password: ", bg='darkslateblue', fg='white', font=text_area_font)
            password_text.place(x=50, y=200)

            password_storage = StringVar()
            password = Entry(textvariable=password_storage, bg='aquamarine', fg='black', font=text_input_font)
            password.place(x=250, y=200)

            pre_button_font = tkFont.Font(family="Helvetica", size=15, weight="bold")
            click = Button(text="Register", fg="red", bg="aqua", relief="raised", font=pre_button_font, command=open_func)
            click.place(x=220, y=250)

            screen.mainloop()

    def main_control(self, email, password):

        self.__user_email = email
        self.__user_password = password

        def open_withdraw():
            amount = withdraw_storage.get()
            obj = UserAccount("", "", "", "", "", "")
            value = obj.user_withdraw(amount, email, password)
            new_text = Label(text=str(value)+"      ", fg="green", bg="white", font=fontStyle_result)
            new_text.place(x=300, y=250)

        def open_deposit():
            amount = deposit_storage.get()
            obj = UserAccount("", "", "", "", "", "")
            value = obj.user_deposit(amount, email, password)
            new_text = Label(text=str(value)+"      ", fg="green", bg="white", font=fontStyle_result)
            new_text.place(x=300, y=250)

        def open_show():
            obj = UserAccount("", "", "", "", "", "")
            value = obj.show_details(email, password)
            (value1, value2) = value
            new_text = Label(text=value1+" ", fg="green", bg="white", font=fontStyle_open)
            new_text.place(x=50, y=350)

            new_text = Label(text=value2+" ", fg="green", bg="white", font=fontStyle_open)
            new_text.place(x=50, y=400)

        def open_balance():
            obj = UserAccount("", "", "", "", "", "")
            value = obj.user_balance(email, password)
            new_text = Label(text=str(value)+"      ", fg="green", bg="white", font=fontStyle_result)
            new_text.place(x=400, y=400)

        screen = Tk()
        screen.title("MAIN BANKING SYSTEM")
        screen.geometry("800x500")

        bg = PhotoImage(file="files/final_view.jpg")
        label1 = Label( screen, image=bg)
        label1.place(x=-5, y=0)

        fontStyle = tkFont.Font(family="Lucida Grande", size=20)
        fontStyle_result = tkFont.Font(family="Lucida Grande", size=20)
        fontStyle_open = tkFont.Font(family="Lucida Grande", size=15)
        text_area_font = tkFont.Font(family="Courier", size=12, weight="bold")
        text_input_font = tkFont.Font(family="Courier", size=13, weight="bold")
        welcome_text = Label(text="MAIN BANKING SYSTEM", fg="blue", bg="violet", font=fontStyle)
        welcome_text.place(x=230, y=2)

        withdraw_text = Label(text="Enter Withdraw Amount: ", bg='darkslateblue', fg='white', font=text_area_font)
        withdraw_text.place(x=50, y=80)

        withdraw_storage = DoubleVar()
        withdraw = Entry(textvariable=withdraw_storage, bg='aquamarine', fg='black', font=text_input_font)
        withdraw.place(x=50, y=140)

        pre_button_font = tkFont.Font(family="Helvetica", size=15, weight="bold")
        click = Button(text="Withdraw Balance", fg="red", bg="aqua", relief="raised", font=pre_button_font,command=open_withdraw)
        click.place(x=50, y=200)

        deposit_text = Label(text="Enter Deposit Amount: ", bg='darkslateblue', fg='white', font=text_area_font)
        deposit_text.place(x=500, y=80)

        deposit_storage = DoubleVar()
        deposit = Entry(textvariable=deposit_storage, bg='aquamarine', fg='black', font=text_input_font)
        deposit.place(x=520, y=140)

        click = Button(text="Deposit Balance", fg="red", bg="aqua", relief="raised", font=pre_button_font, command=open_deposit)
        click.place(x=550, y=200)

        click = Button(text="Show Details: ", fg="white", bg="steelblue", relief="ridge", font=pre_button_font, command=open_show)
        click.place(x=50, y=300)

        click = Button(text="Show Current Balance: ", fg="white", bg="steelblue", relief="ridge", font=pre_button_font, command=open_balance)
        click.place(x=480, y=300)

        screen.mainloop()

        # print("New Account Needs Deposit")
            # obj1 = UserAccount("", "", "", "", "", "")
            # obj1.user_deposit(input("Enter Deposit Amount"), email, password)
            # obj1.user_withdraw(input("Enter Withdraw Amount"), email, password)
            # obj1.show_details(email, password)

# user = UserAccount("", "", "", "", "", "")
# user.user_login()


# user.open_user_account()
# user.user_deposit(input("Enter Deposit Amount"))
# user.user_deposit(input("Enter Deposit Amount"))
# user.user_withdraw(input("Enter Withdraw Amount"))
# user.show_details()
# user.user_balance()
