from abc import abstractmethod, ABC

class DaoInterface(ABC):
    @abstractmethod
    def select(self):
        pass

    @abstractmethod
    def update(self, obId):
        pass

    @abstractmethod
    def insert(self, ent:object):
        pass

    @abstractmethod
    def delete(self, ent:object):
        pass


class TaskDao(DaoInterface):
    pass