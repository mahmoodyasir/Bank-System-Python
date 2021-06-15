from abc import ABC


class User(ABC):

    def get_user_name(self):
        pass

    def set_user_name(self,  name):
        pass

    def show_details(self, email, password):
        pass

    def get_user_email(self):
        pass

    def set_user_email(self, email):
        pass

    def open_user_account(self, name, email, password):
        pass

    def get_user_password(self):
        pass

    def set_user_password(self, password):
        pass
