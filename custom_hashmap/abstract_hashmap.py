from abc import ABC, abstractmethod


class AbstractHashMap(ABC):
    @abstractmethod
    def insert(self, key, value):
        pass

    @abstractmethod
    def remove(self, key):
        pass

    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def __len__(self):
        pass
