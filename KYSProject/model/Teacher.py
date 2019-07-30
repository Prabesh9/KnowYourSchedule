class Teacher(object):
    def __init__(self):
        self.__teacher_id = None
        self.__first_name = None
        self.__last_name = None
        self.__email = None
        self.__password = None

    @property
    def teacher_id(self):
        return self.__teacher_id

    @teacher_id.setter
    def first_name(self, teacher_id):
        self.__teacher_id = teacher_id

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def password(self):
        return self.__password

    @email.setter
    def password(self, password):
        self.__password = password
