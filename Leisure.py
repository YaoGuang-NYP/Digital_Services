from Blog import Blog

class Leisure(Blog):
    def __init__(self, title, publisher, status, created_by, category, type, frequency):
        Blog.__init__(self, title, publisher, status, created_by, category, type)
        self.__frequency = frequency

    # Getters

    def get_frequency(self):
        return self.__frequency

    # Setters

    def set_frequency(self, frequency):
        self.__frequency = frequency