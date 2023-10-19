from simple_binary_tree import SimpleBinaryTree

# Implementation of a red-black binary tree

# Invariants of a red black tree:
#  1. Every node is either red or black
#  2. The root of the tree is always black
#  3. All leaves are null and they are black
#  4. If a node is red, then its parent is black
#  5. Any path from a node to any of its descendant null nodes contains the same number of black nodes

class RedBlackBinaryTreeNode():
    def __init__(self, value) -> None:
        self.value = value
        self.red = True
        self.parent = None
        self.left = None
        self.right = None

# In this implementation we do not allow duplicate values
class RedBlackBinaryTree(SimpleBinaryTree):
    # Remove node's parent and plug the node into its grandparent
    def remove_intermediate_generation(self, node):
        parent = node.parent
        grandparent = parent.parent
        node.parent = grandparent
        if grandparent:
            if grandparent.left == parent:
                grandparent.left = node
            else:
                grandparent.right = node
        else:
            # Parent was the root -> node is the new root
            self.root = node


    # Rotate a node up and to the left
    # Note that we move the nodes themselves around and not just the values, and we don't change the colors
    def rotate_left(self, node):
        assert node.parent.right == node
        parent = node.parent
        self.remove_intermediate_generation(node)
        node_left = node.left
        node.left = parent
        parent.parent = node
        parent.right = node_left
        if node_left:
            node_left.parent = parent

    # Rotate a node up and to the right
    # Note that we move the nodes themselves around and not just the values
    def rotate_right(self, node):
        assert node.parent.left == node
        parent = node.parent
        self.remove_intermediate_generation(node)
        node_right = node.right
        node.right = parent
        parent.parent = node
        parent.left = node_right
        if node_right:
            node_right.parent = parent


    def fix_tree_after_insert(self, node):
        # If node is not red, no action is needed
        if not node.red:
            return
        # Node is the root and is set to black
        if not node.parent:
            node.red = False
            return
        parent = node.parent
        # If parent is black, no action is needed
        if not parent.red:
            return
        # If the parent is red, then parent is not the root -> the grandparent must exist and be black 
        grandparent = parent.parent
        uncle = grandparent.right if grandparent.left == parent else grandparent.left
        if uncle and uncle.red:
            parent.red = False
            uncle.red = False
            grandparent.red = True
            self.fix_tree_after_insert(grandparent)
        else:
            grandparent.red = True
            # Left-left case
            if grandparent.left == parent and parent.left == node:
                self.rotate_right(parent)
                parent.red = False
            # Left-right case
            elif grandparent.left == parent and parent.right == node:
                self.rotate_left(node)
                self.rotate_right(node)
                node.red = False
            # Right-left case
            elif grandparent.right == parent and parent.left == node:
                self.rotate_right(node)
                self.rotate_left(node)
                node.red = False
            # Right-right case
            else:
                self.rotate_left(parent)
                parent.red = False

    def insert(self, value):
        node_to_insert = RedBlackBinaryTreeNode(value)
        if not self.root:
            self.root = node_to_insert
            self.fix_tree_after_insert(node_to_insert)
            return True
        current = self.root
        while True:
            if value == current.value:
                return False
            elif value < current.value:
                if not current.left:
                    node_to_insert.parent = current
                    current.left = node_to_insert
                    self.fix_tree_after_insert(node_to_insert)
                    return True
                else:
                    current = current.left
            else:
                if not current.right:
                    node_to_insert.parent = current
                    current.right = node_to_insert
                    self.fix_tree_after_insert(node_to_insert)
                    return True
                else:
                    current = current.right

    def handle_double_black(self, node):
        if not node.parent:
            # We are at the root, and double black is equivalent to black
            return
        parent = node.parent
        node_is_left = parent.left == node
        # We know sibling exists by invariant 5
        sibling = parent.right if node_is_left else parent.left
        # Since node is double black, sibling must have two children by invariant 5
        sibling_left = sibling.left
        sibling_right = sibling.right
        if parent.red:
            # Sibling must be black by invariant 4
            sibling.red = True
            parent.red = False
            if sibling_left.red and sibling_right.red:
                if node_is_left:
                    self.rotate_left(sibling)
                    sibling_right.red = False
                else:
                    self.rotate_right(sibling)
                    sibling_left.red = False
            elif sibling_left.red:
                self.fix_tree_after_insert(sibling_left)
            else:
                self.fix_tree_after_insert(sibling_right)
        elif sibling.red:
            # sibling_left and sibling_right must be black by invariant 4
            sibling.red = False
            parent.red = True
            if node_is_left:
                self.rotate_left(sibling)
            else:
                self.rotate_right(sibling)
            # We've now set this up as a case where node is double black and parent is red, which is solved above
            self.handle_double_black(node)
        # Sibling is black and parent is black
        else:
            parent.red = True
            if node_is_left:
                self.rotate_left(sibling)
            else:
                self.rotate_right(sibling)
            # Sibling is now at the level parent was at before and is the new double black
            self.handle_double_black(sibling)
            # handle_double_black is agnostic of everything below sibling
            # fix_tree_after_insert is agnostic of everything at and above sibling
            # Thus, the order in which we do these two operations does not matter
            if node_is_left and sibling_left.red:
                self.fix_tree_after_insert(sibling_left)
            if (not node_is_left) and sibling_right.red:
                self.fix_tree_after_insert(sibling_right)

    def handle_deletion_black_no_child_black_parent_black_sibling(self, node):
        parent = node.parent
        node_is_left = parent.left == node
        # Delete the node
        if node_is_left:
            parent.left = None
        else:
            parent.right = None
        sibling = parent.right if node_is_left else parent.left

        # If the sibling has children, they must be red and they must be childless to maintain invariant 5
        sibling_left = sibling.left
        sibling_right = sibling.right
        if sibling_left and sibling_right:
            if node_is_left:
                self.rotate_left(sibling)
                sibling_right.red = False
            else:
                self.rotate_right(sibling)
                sibling_left.red = False
        elif sibling_left:
            sibling_left.red = False
            if node_is_left:
                self.rotate_right(sibling_left)
                self.rotate_left(sibling_left)
            else:
                self.rotate_right(sibling)
        elif sibling_right:
            sibling_right.red = False
            if node_is_left:
                self.rotate_left(sibling)
            else:
                self.rotate_left(sibling_right)
                self.rotate_right(sibling_right)
        # The sibling has no children, so we make it red and consider the parent double black
        else:
            sibling.red = True
            self.handle_double_black(parent)                

    # Here, node is a black node with no children
    def handle_deletion_black_no_child(self, node):
        # If it's a single node with no children and no parent, it's the root and we reset the tree
        if not node.parent:
            self.root = None
            return
        parent = node.parent
        # All non-root black nodes must have a sibling node by invariant 5
        sibling = parent.right if parent.left == node else parent.left
        if parent.red or sibling.red:
            # The sibling must be black by invariant 4
            # Remove both parent and node from the tree
            self.remove_intermediate_generation(sibling)
            sibling.red = False
            # To finish, we need to reinsert parent.value
            self.insert(parent.value)
        else:
            self.handle_deletion_black_no_child_black_parent_black_sibling(node)
        
    # Deletes value in the tree if it exists and returns whether the element is found
    def delete(self, value):
        if not self.root:
            return False
        current = self.root
        while current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            # Delete the current node
            else:
                if not current.right:
                    if current.red:
                        # If current.right is null and current is red, current must have no children
                        parent = current.parent
                        if parent.left == current:
                            parent.left = None
                        else:
                            parent.right = None
                    elif current.left:
                        current_left = current.left
                        current_left.red = False
                        self.remove_intermediate_generation(current_left)
                    else:
                        self.handle_deletion_black_no_child(current)
                else:
                    switch = current.right
                    while switch.left:
                        switch = switch.left
                    # Here, switch contains the lowest value greater than current, and we switch the *values*
                    x = switch.value
                    switch.value = current.value
                    current.value = x
                    # Then we set current to point to the node switch was at
                    current = switch
                    # Here, from the loop above we know that current.left is null
                    if current.red:
                        # If current.left is null and current is red, current must have no children
                        parent = current.parent
                        if parent.left == current:
                            parent.left = None
                        else:
                            parent.right = None
                    elif current.right:
                        # If current.right exists, it must be red, otherwise we break the fifth invariant
                        current_right = current.right
                        current_right.red = False
                        self.remove_intermediate_generation(current_right)
                    else:
                        self.handle_deletion_black_no_child(current)
                return True
        # Value not found in the tree
        return False