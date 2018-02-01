import datetime

class Blog:
    def __init__(self, title, publisher, status, created_by, category, type):
        self.__blogid = ''
        self.__title = title
        self.__publisher = publisher
        self.__status = status
        self.__created_by = created_by
        currentdatetime = datetime.datetime.now()
        create_date = str(currentdatetime.day) + "-" + str(currentdatetime.month) + "-" + str(currentdatetime.year)
        self.__created_date = create_date
        self.__category = category
        self.__type = type

    # Accessor Method
    def get_blogid(self):
        return self.__blogid

    def get_title(self):
        return self.__title

    def get_publisher(self):
        return self.__publisher

    def get_status(self):
        return self.__status

    def get_created_by(self):
        return self.__created_by

    def get_created_date(self):
        return self.__created_date

    def get_category(self):
        return self.__category

    def get_type(self):
        return self.__type

    # Mutator Method
    def set_blogid(self, blogid):
        self.__blogid = blogid

    def set_title(self, title):
        self.__title = title

    def set_publisher(self, publisher):
        self.__publisher = publisher

    def set_status(self, status):
        self.__status = status

    def set_created_by(self, created_by):
        self.__created_by = created_by

    def set_created_date(self, created_date):
        self.__created_date = created_date

    def set_category(self, category):
        self.__category = category

    def set_type(self, type):
        self.__type = type