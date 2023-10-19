from abc import ABC, abstractmethod


# Abstract base class for binary trees

class BinaryTree(ABC):
    @abstractmethod
    def insert(self, value):
        pass

    @abstractmethod
    def lookup(self, value):
        pass

    @abstractmethod
    def delete(self, value):
        pass

    @abstractmethod
    def list(self):
        pass