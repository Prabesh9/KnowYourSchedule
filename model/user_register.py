class UserRegister(object):
    def __init__(self):
        self.__user = None
        self.__password = None
        self.__cpassword = None

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user):
        self.__user = user

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def cpassword(self):
        return self.__cpassword

    @cpassword.setter
    def cpassword(self, cpassword):
        self.__cpassword = cpassword