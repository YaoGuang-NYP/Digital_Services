from forms import Forms

class RegisterForm(Forms) :
    def __init__(self, username, password, email, firstname, lastname, age, country, highestqualification, workexperiences, skillsets, awards, bio):
        Forms.__init__(self, username, password)
        self.__email = email
        self.__firstname = firstname
        self.__lastname = lastname
        self.__age = age
        self.__country = country
        self.__highestqualification = highestqualification
        self.__workexperiences = workexperiences
        self.__skillsets = skillsets
        self.__awards = awards
        self.__bio = bio
    def get_email(self):
        return self.__email
    def get_firstname(self):
        return self.__firstname
    def get_lastname(self):
        return self.__lastname
    def get_age(self):
        return self.__age
    def get_country(self):
        return self.__country
    def get_highestqualification(self):
        return self.__highestqualification
    def get_workexperiences(self):
        return self.__workexperiences
    def get_skillsets(self):
        return self.__skillsets
    def get_awards(self):
        return self.__awards
    def get_bio(self) :
        return self.__bio
    def set_email(self, email):
        self.__email = email
    def set_firstname(self, firstname):
        self.__firstname = firstname
    def set_lastname(self, lastname):
        self.__lastname = lastname
    def set_age(self, age):
        self.__age = age
    def set_country(self, country):
        self.__country = country
    def set_highestqualification(self, highestqualification):
        self.__highestqualification = highestqualification
    def set_workexperiences(self, workexperiences):
        self.__workexperiences = workexperiences
    def set_skillsets(self, skillsets):
        self.__skillsets = skillsets
    def set_awards(self, awards):
        self.__awards = awards
    def set_bio(self, bio) :
        self.__bio = bio
