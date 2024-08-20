class SerpentObject:

    def __init__(self, id, name=None, type=None):
        self.id = id
        self.name = name
        self.type = type

    # Setters
    @id.setter
    def id(self, id):
        pass

    @name.setter
    def name(self, name):
        self.name = name

    @type.setter
    def type(self, type):
        self.type = type

    # Getters
    @property
    def id(self):
        return self.id

    @property
    def name(self):
        return self.__name

    @property
    def type(self):
        return self.__type
