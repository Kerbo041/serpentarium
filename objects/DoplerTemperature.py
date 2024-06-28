class DoplerTemperature:
    
    values_dict = {
        300 : "03",
        600 : "06",
        900 : "09"
    }
    
    def __init__(self, value) -> None:
        
        self.value = value
        self.set_text_value(self.value)
    
    def set_value(self, value):
        self.value = value
        
    def get_value(self):
        return self.value
    
    def set_text_value(self):
        self.text_value = self.values_dict[self.value]
    
    def get_text_value(self):
        return self.text_value
    
    def __str__(self) -> str:
        return f"{self.text_value}c"