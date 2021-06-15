from tkinter import *
import tkinter.font as tkFont


def open_withdraw():
    value = 40
    new_text = Label(text=value, fg="green", bg="white", font=fontStyle_result)
    new_text.place(x=300, y=250)


def open_deposit():
    value = 20
    new_text = Label(text=value, fg="green", bg="white", font=fontStyle_result)
    new_text.place(x=300, y=250)


def open_show():
    value1 = "Name: mamun"
    new_text = Label(text=value1, fg="green", bg="white", font=fontStyle_result)
    new_text.place(x=50, y=350)

    value2 = "Email: mamun@gmail.com"
    new_text = Label(text=value2, fg="green", bg="white", font=fontStyle_result)
    new_text.place(x=50, y=400)


def open_balance():
    value = "Current Balance: 2000      "
    new_text = Label(text=value, fg="green", bg="white", font=fontStyle_result)
    new_text.place(x=400, y=400)


screen = Tk()
screen.title("MAIN BANKING SYSTEM")
screen.geometry("800x500")

# bg = PhotoImage(file="files/main.jpg")
# label1 = Label( screen, image=bg)
# label1.place(x=-5, y=0)

fontStyle = tkFont.Font(family="Lucida Grande", size=20)
fontStyle_result = tkFont.Font(family="Lucida Grande", size=20)
text_area_font = tkFont.Font(family="Courier", size=12, weight="bold")
text_input_font = tkFont.Font(family="Courier", size=13, weight="bold")
welcome_text = Label(text = "MAIN BANKING SYSTEM", fg = "blue", bg = "violet", font=fontStyle)
welcome_text.place(x=230, y=2)

withdraw_text = Label(text = "Enter Withdraw Amount: ", bg= 'darkslateblue', fg='white', font=text_area_font)
withdraw_text.place(x=50, y=80)

withdraw_storage = DoubleVar()
withdraw = Entry(textvariable=withdraw_storage, bg='aquamarine', fg='black',font=text_input_font)
withdraw.place(x=50, y=140)

pre_button_font = tkFont.Font(family="Helvetica", size=15, weight="bold")
click = Button(text = "Withdraw Balance", fg="red", bg="aqua", relief="raised", font=pre_button_font, command=open_withdraw)
click.place(x=50, y=200)


deposit_text = Label(text = "Enter Deposit Amount: ", bg= 'darkslateblue', fg='white', font=text_area_font)
deposit_text.place(x=500, y=80)

deposit_storage = DoubleVar()
deposit = Entry(textvariable=deposit_storage, bg='aquamarine', fg='black',font=text_input_font)
deposit.place(x=520, y=140)

click = Button(text="Deposit Balance", fg="red", bg="aqua", relief="raised", font=pre_button_font, command=open_deposit)
click.place(x=550, y=200)

click = Button(text="Show Details: ", fg="white", bg="steelblue", relief="ridge", font=pre_button_font, command=open_show)
click.place(x=50, y=300)

click = Button(text="Show Current Balance: ", fg="white", bg="steelblue", relief="ridge", font=pre_button_font, command=open_balance)
click.place(x=480, y=300)


screen.mainloop()



