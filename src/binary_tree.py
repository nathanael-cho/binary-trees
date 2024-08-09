from abc import ABC, abstractmethod
from typing import Optional


# Abstract base classes for binary trees

class BinaryTreeNode():
    """Binary tree node"""

    def __init__(self, value: int) -> None:
        self.value: int = value
        self.left: Optional[BinaryTreeNode] = None
        self.right: Optional[BinaryTreeNode] = None


class BinaryTree(ABC):
    """Binary tree abstract base class"""

    def __init__(self):
        self.root: BinaryTreeNode = None

    @abstractmethod
    def insert(self, value: int) -> bool:
        pass

    def lookup(self, value: int) -> bool:
        """Look up a value in the tree and return whether it exists"""
        if not self.root:
            return False
        else:
            current = self.root
            while current:
                if value == current.value:
                    return True
                elif value < current.value:
                    current = current.left
                else:
                    current = current.right
            return False

    @abstractmethod
    def delete(self, value: int) -> bool:
        pass

    def list(self) -> list[int]:
        """Return a list of the values in the tree in ascending order"""
        to_return = []
        node_stack = [self.root]
        visited = set()
        while node_stack:
            node = node_stack.pop()
            if not node:
                continue
            if node.value not in visited:
                visited.add(node.value)
                node_stack.append(node.right)
                node_stack.append(node)
                node_stack.append(node.left)
            else:
                to_return.append(node.value)
        return to_return
