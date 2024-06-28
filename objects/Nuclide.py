from objects.DoplerTemperature import DoplerTemperature
class Nuclide:
    def __init__(
        self, id, nuclide_number :int, atomic_mass :int, temperature :DoplerTemperature, fraction :str
    ):
        self.id = id
        self.nuclide_number = nuclide_number
        self.atomic_mass = atomic_mass
        self.temperature = temperature
        self.fraction = fraction

    def set_nuclide_number(self, nuclide_number):
        self.nuclide_number = nuclide_number

    def get_nuclide_number(self):
        return self.nuclide_number

    def set_atomic_mass(self, atomic_mass):
        self.atomic_mass = atomic_mass

    def get_atomic_mass(self):
        return self.atomic_mass

    def set_temperature(self, temperature):
        self.temperature = temperature

    def get_temperature(self):
        return self.temperature

    def set_fraction(self, fraction):
        self.fraction = fraction

    def get_fraction(self):
        return self.fraction

    def get_string(self):
        return f"{self.nuclide_number}{self.atomic_mass}.{self.temperature} \t {self.fraction}"
    
    def __str__(self):
        self.get_string(self)