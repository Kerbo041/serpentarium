class Material:
    def __init__(
        self, id, name :str, density :Density, temperature=None, color=None
    ):
        self.id = id
        self.name = name
        self.density = density
        self.temperature = temperature
        self.color = color

    def set_name(self, name):
        self.name = name

    def get_set_name(self):
        return self.set_name

    def set_density(self, density):
        self.density = density

    def get_density(self):
        return self.density

    def set_temperature(self, temperature):
        self.temperature = temperature

    def get_temperature(self):
        return self.temperature

    def set_rgb(self, fraction):
        self.fraction = fraction

    def get_rgb(self):
        return self.rgb

    def get_string(self):
        pass
    
    def __str__(self):
        self.get_string(self)