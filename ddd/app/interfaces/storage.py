import abc


class StorageABC(abc.ABC):
    abc.abstractmethod

    def session(self):
        pass
