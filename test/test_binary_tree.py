import random
from time import perf_counter

from src.binary_tree import BinaryTree
from src.simple_binary_tree import SimpleBinaryTree
from src.red_black_binary_tree import RedBlackBinaryTree


class TimerContextManager:
    """Context manager to time a block of code"""

    def __init__(self, name: str):
        """Initialize the timer"""
        self.name = name

    def __enter__(self):
        """Start the timer"""
        self.start = perf_counter()
        return self

    def __exit__(self, *_):
        """End the timer"""
        self.end = perf_counter()
        print(f'{self.name}: {self.end - self.start:.3f} seconds')


def binary_tree_general_functionality(tree: BinaryTree):
    """Test general functionality of a binary tree"""
    # Test inserting nodes into the tree
    assert tree.insert(2)
    assert tree.insert(3)
    assert tree.insert(4)
    assert tree.insert(5)
    assert tree.insert(6)
    assert tree.insert(7)
    assert tree.insert(8)
    assert not tree.insert(8)
    assert tree.list() == [2, 3, 4, 5, 6, 7, 8]

    # Test looking up nodes in the tree
    assert tree.lookup(2)
    assert tree.lookup(3)
    assert tree.lookup(4)
    assert tree.lookup(5)
    assert tree.lookup(6)
    assert tree.lookup(7)
    assert tree.lookup(8)
    assert not tree.lookup(1)
    assert not tree.lookup(9)

    # Test additional insertions
    assert tree.insert(0)
    assert tree.insert(10)
    assert tree.list() == [0, 2, 3, 4, 5, 6, 7, 8, 10]

    # Test deleting nodes from the tree
    assert tree.delete(2)
    assert not tree.lookup(2)
    assert tree.delete(3)
    assert not tree.lookup(3)
    assert tree.delete(4)
    assert not tree.lookup(4)
    assert tree.delete(5)
    assert not tree.lookup(5)
    assert tree.delete(6)
    assert not tree.lookup(6)
    assert tree.delete(7)
    assert not tree.lookup(7)
    assert tree.delete(8)
    assert not tree.lookup(8)
    assert not tree.delete(1)
    assert not tree.delete(9)
    assert tree.list() == [0, 10]
    assert tree.delete(0)
    assert tree.delete(10)
    assert tree.list() == []
    assert not tree.delete(1)


def binary_tree_big_tree_linear_insertion(tree: BinaryTree):
    """Test a big tree with linear insertion"""
    n = 10000
    r = range(1, n + 1)
    for i in r:
        assert tree.insert(i)
    for i in r:
        assert tree.lookup(i)
    assert not tree.lookup(0)
    assert not tree.lookup(n + 1)
    assert tree.list() == sorted(r)
    for i in r:
        assert tree.delete(i)
        assert not tree.lookup(i)


def binary_tree_big_tree_random_insertion(tree: BinaryTree):
    """Test a big tree with random insertion"""
    # For debugging, we know what seed caused an error
    random.seed(1)

    # Big tree, random insertion
    population = 1000000
    n = 100000
    r = random.sample(range(1, population + 1), n)
    for i in r:
        assert tree.insert(i)
    for i in r:
        assert tree.lookup(i)
    assert not tree.lookup(0)
    assert not tree.lookup(population + 1)
    assert tree.list() == sorted(r)
    for i in r:
        assert tree.delete(i)
        assert not tree.lookup(i)


def test_simple_binary_tree_general_functionality():
    """Test the general functionality of a simple binary tree"""
    with TimerContextManager("Simple Binary Tree, General Functionality"):
        binary_tree_general_functionality(SimpleBinaryTree())


def test_simple_binary_tree_big_tree_linear_insertion():
    """Test a big tree with linear insertion in a simple binary tree"""
    with TimerContextManager("Simple Binary Tree, Big Tree Linear Insertion"):
        binary_tree_big_tree_linear_insertion(SimpleBinaryTree())


def test_simple_binary_tree_big_tree_random_insertion():
    """Test a big tree with random insertion in a simple binary tree"""
    with TimerContextManager("Simple Binary Tree, Big Tree Random Insertion"):
        binary_tree_big_tree_random_insertion(SimpleBinaryTree())


def test_red_black_binary_tree_general_functionality():
    """Test the general functionality of a red-black binary tree"""
    with TimerContextManager("Red Black Binary Tree, General Functionality"):
        binary_tree_general_functionality(RedBlackBinaryTree())


def test_red_black_binary_tree_big_tree_linear_insertion():
    """Test a big tree with linear insertion in a red-black binary tree"""
    with TimerContextManager("Red Black Binary Tree, Big Tree Linear Insertion"):
        binary_tree_big_tree_linear_insertion(RedBlackBinaryTree())


def test_red_black_binary_tree_big_tree_random_insertion():
    """Test a big tree with random insertion in a red-black binary tree"""
    with TimerContextManager("Red Black Binary Tree, Big Tree Random Insertion"):
        binary_tree_big_tree_random_insertion(RedBlackBinaryTree())
