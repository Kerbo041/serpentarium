from src.model.SerpentObjects.SerpentObject import SerpentObject

class SerpentObjectRepository():
    def __init__(self, id: int, type) -> None:
        self.id = id
        self.type = type
        self.storage = {}

    @property
    def __id(self) -> int:
        return self.id
    
    def add_object(self, serpentObject: SerpentObject) -> None:
        serpentObject_id = serpentObject.get_id()
        self.__storage[serpentObject_id] = serpentObject