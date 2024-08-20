from src.repository.SerpentObjectRepository import SerpentObjectRepository

class SerpentObjectController():
    def __init__(self, id):
        self.id = id
        self.repository_storage = {}

    @property
    def id(self):
        return self.id
    
    def add_repository(self, serpentObjectRepository: SerpentObjectRepository):
        self.repository_storage[serpentObjectRepository.id] = serpentObjectRepository

    def delete_repository(self, serpentObjectRepository: SerpentObjectRepository):
        del self.repository_storage[serpentObjectRepository.id]