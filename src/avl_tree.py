from typing import Optional

from .binary_tree import BinaryTree, BinaryTreeNode


class AVLTreeNode(BinaryTreeNode):
    """AVL tree node"""

    def __init__(self, value: int) -> None:
        self.value: int = value
        self.left: AVLTreeNode = None
        self.right: AVLTreeNode = None
        self.height: int = 1


class AVLTree(BinaryTree):
    """AVL tree"""

    root: Optional[AVLTreeNode]

    def __init__(self):
        self.root: AVLTreeNode = None

    @staticmethod
    def get_balance(node: AVLTreeNode) -> int:
        """Get the balance of a node"""
        return (node.left.height if node.left else 0) - (node.right.height if node.right else 0)
    
    def rotate_left(self, node: AVLTreeNode) -> AVLTreeNode:
        """
        Rotate a node's right child up

        Note that we move the nodes themselves around and not just the values
        """
        assert bool(node.right)
        node_right = node.right
        temporary = node_right.left
        node_right.left = node
        node.right = temporary
        node.height = 1 + max(
            node.left.height if node.left else 0,
            node.right.height if node.right else 0
        )
        node_right.height = 1 + max(
            node_right.left.height if node_right.left else 0,
            node_right.right.height if node_right.right else 0
        )
        return node_right

    def rotate_right(self, node: AVLTreeNode) -> AVLTreeNode:
        """
        Rotate a node's left child up

        Note that we move the nodes themselves around and not just the values
        """
        assert bool(node.left)
        node_left = node.left
        temporary = node_left.right
        node_left.right = node
        node.left = temporary
        node.height = 1 + max(
            node.left.height if node.left else 0,
            node.right.height if node.right else 0
        )
        node_left.height = 1 + max(
            node_left.left.height if node_left.left else 0,
            node_left.right.height if node_left.right else 0
        )
        return node_left

    def recursive_insert(self, node: Optional[AVLTreeNode], value: int) -> AVLTreeNode:
        """
        Recursively insert a value into the tree
        
        We only call this method when we know the value is not already in the tree
        """
        if not node:
            return AVLTreeNode(value)

        if value < node.value:
            node.left = self.recursive_insert(node.left, value)
        elif value > node.value:
            node.right = self.recursive_insert(node.right, value)
        else:
            raise ValueError("The value is already in the tree")
        
        node.height = 1 + max(
            node.left.height if node.left else 0,
            node.right.height if node.right else 0
        )

        balance = AVLTree.get_balance(node)

        # Left-left case
        if (balance > 1 and value < node.left.value):
            return self.rotate_right(node)
        # Right-right case
        elif (balance < -1 and value > node.right.value):
            return self.rotate_left(node)
        # Left-right case
        elif (balance > 1 and value > node.left.value):
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        # Right-left case
        elif (balance < -1 and value < node.right.value):
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        else:
            return node

    def insert(self, value: int) -> bool:
        """
        Insert a value into the tree and return whether the insertion is successful
        
        Duplicate values are not inserted
        """
        if not self.root:
            self.root = AVLTreeNode(value)
            return True
        
        if self.lookup(value):
            return False
        
        self.root = self.recursive_insert(self.root, value)
        return True
    
    def delete(self, value: int) -> bool:
        """Delete a value from the tree and return whether it was found"""
        if not self.lookup(value):
            return False
        pass
