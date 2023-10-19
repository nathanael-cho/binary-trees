from binary_tree import BinaryTree

# Implementation of a simple binary tree

class SimpleBinaryTreeNode():
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

# In this implementation we do not allow duplicate values
class SimpleBinaryTree(BinaryTree):
    def __init__(self):
        self.root = None

    # Inserts the value if it does not already exist and returns whether the insertion is successful
    def insert(self, value):
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

    def lookup(self, value):
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
        
    # Deletes the value in the tree if it exists and returns whether the element is found
    def delete(self, value):
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
    
    # This implementation assumes no duplicates in the binary tree
    def list(self):
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