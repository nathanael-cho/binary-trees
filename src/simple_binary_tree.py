from typing import Optional

from .binary_tree import BinaryTree, BinaryTreeNode


# Implementation of a simple binary tree

class SimpleBinaryTreeNode(BinaryTreeNode):
    """Node for a simple binary tree"""
    pass


# In this implementation we do not allow duplicate values
class SimpleBinaryTree(BinaryTree):
    """Simple binary tree"""

    root: Optional[SimpleBinaryTreeNode]

    def insert(self, value: int) -> bool:
        """
        Insert a value into the tree and return whether it was inserted
        
        Duplicate values are not allowed
        """
        node_to_insert = SimpleBinaryTreeNode(value)

        if not self.root:
            self.root = node_to_insert
            return True
            
        current = self.root
        while True:
            if value == current.value:
                return False
            elif value < current.value:
                if not current.left:
                    current.left = node_to_insert
                    return True
                else:
                    current = current.left
            else:
                if not current.right:
                    current.right = SimpleBinaryTreeNode(value)
                    return True
                else:
                    current = current.right

    def delete(self, value: int) -> bool:
        """Delete a value from the tree and return whether it was found"""
        if not self.root:
            return False

        current = self.root
        parent = None
        while current:
            if value < current.value:
                parent = current
                current = current.left
            elif value > current.value:
                parent = current
                current = current.right
            # Delete the current node
            else:
                replacement = None
                if not current.right:
                    replacement = current.left
                elif not current.right.left:
                    current.right.left = current.left
                    replacement = current.right
                # Replace the current node with the smallest value among current.right and its children
                else:
                    replacement = current.right.left
                    parent_of_replacement = current.right
                    while replacement.left:
                        parent_of_replacement = replacement
                        replacement = replacement.left
                    parent_of_replacement.left = replacement.right
                    replacement.left = current.left
                    replacement.right = current.right

                if not parent:
                    self.root = replacement
                elif parent.value > current.value:
                    parent.left = replacement
                else:
                    parent.right = replacement
                return True

        # Value not found in the tree
        return False
