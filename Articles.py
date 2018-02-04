import datetime

class Articles:
    def __init__(self, title, author, body):
        self.__articleid = ''
        self.__title = title
        self.__author = author
        currentdatetime = datetime.datetime.now()
        create_date = str(currentdatetime.day) + "-" + str(currentdatetime.month) + "-" + str(currentdatetime.year) # DD-MM-YYYY format
        self.__created_date = create_date
        self.__body = body

    # Accessor Methods
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_created_date(self):
        return self.__created_date

    def get_body(self):
        return self.__body

    def get_articleid(self):
        return self.__articleid

    # Mutator Methods
    def set_title(self,title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_created_date(self, create_date):
        self.__created_date = create_date

    def set_body(self, body):
        self.__body = body

    def set_articleid(self, articleid):
        self.__articleid = articleid
