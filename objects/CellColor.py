class CellColor:
    def __init(self, id, name, ColorsList):
        self.id = id
        self.name = name
        pass
    
    def __str__(self):
        return f"rgb {self.red} {self.green} {self.blue}"