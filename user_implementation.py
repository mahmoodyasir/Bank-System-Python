from main_class import User


class UserImpl(User):
    __user_name = ""
    __user_email = ""
    __user_password = ""

    def __init__(self, user_name, user_email, user_password):
        self.__user_name = user_name
        self.__user_email = user_email
        self.__user_password = user_password
        self.var = 0

    def get_user_name(self):
        return self.__user_name

    def set_user_name(self, name):
        var = self.__user_name = name
        return var

    def get_user_email(self):
        return self.__user_email

    def set_user_email(self, email):
        var = self.__user_email = email
        return var

    def get_user_password(self):
        return self.__user_password

    def set_user_password(self, password):
        var = self.__user_password = password
        return var

    def open_user_account(self, name, email, password):

        try:
            self.__user_name = name
            self.__user_email = email
            self.__user_password = password
            user_info = UserImpl(self.__user_name, self.__user_email, self.__user_password)
            user_info.get_user_name()
            user_info.get_user_email()
            user_info.get_user_password()
            mydata = open("mydata.txt", "a+")
            tb = (user_info.get_user_email() + user_info.get_user_password(),)
            mydata.write(str(tb))
            mydata.close()
            filename = user_info.get_user_email() + user_info.get_user_password()
            user_data = (user_info.get_user_email() + " " + user_info.get_user_name() + " " + "0.0")
            yourfile = open(filename + '.txt', "w+")
            yourfile.write(user_data)
            yourfile.close()
            print("Your Account was successfully created")
            message = "Your Account was successfully created"
            return user_info.get_user_email(), user_info.get_user_password(), message

        except ValueError:
            print('Invalid input!')

    def show_details(self, email, password):
        self.__user_email = email
        self.__user_password = password
        print("Personal Details:")
        user_info = UserImpl(self.__user_name, self.__user_email, self.__user_password)
        filename = user_info.get_user_email() + user_info.get_user_password()
        read_file = open(filename + '.txt', "r")
        value = read_file.read()
        words = value.split()
        (a, b, c) = words
        # print("Name: ", b)
        details_name = "Name: " + str(b)
        #print("Email: ", a)
        details_email = "Email: " + str(a)
        return details_name, details_email

        # print("Name: ", self.__user_name)
        # print("Email: ", self.__user_email)


# user = UserImpl("", "", "")
# user.open_user_account()
# user.show_details()
