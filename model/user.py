class User(object):
    def __init__(self):
        self.__user_id = None
        self.__full_name = None
        self.__email = None
        self.__created_at = None

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self, created_at):
        self.__created_at = created_at

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, full_name):
        self.__full_name = full_name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email