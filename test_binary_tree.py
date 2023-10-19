import random
import time

from simple_binary_tree import SimpleBinaryTree
from red_black_binary_tree import RedBlackBinaryTree

def binary_tree_general_functionality(tree):
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

def binary_tree_big_tree_linear_insertion(tree):
    # Big tree, linear insertion
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

def binary_tree_big_tree_random_insertion(tree):
    # For debugging, we know what seed caused an error
    random.seed(2)

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

def timer_decorator(name):
    def timer(f):
        start = time.time()
        f()
        end = time.time()
        print(f"{name}: {end - start:.02f}s")
    return timer

# @timer_decorator("Simple Binary Tree, General Functionality")
def test_simple_binary_tree_general_functionality():
    binary_tree_general_functionality(SimpleBinaryTree())

@timer_decorator("Simple Binary Tree, Big Tree Linear Insertion")
def test_simple_binary_tree_big_tree_linear_insertion():
    binary_tree_big_tree_linear_insertion(SimpleBinaryTree())

@ timer_decorator("Simple Binary Tree, Big Tree Random Insertion")
def test_simple_binary_tree_big_tree_random_insertion():
    binary_tree_big_tree_random_insertion(SimpleBinaryTree())

# @timer_decorator("Red Black Binary Tree, General Functionality")
def test_red_black_binary_tree_general_functionality():
    binary_tree_general_functionality(RedBlackBinaryTree())

@timer_decorator("Red Black Binary Tree, Big Tree Linear Insertion")
def test_red_black_binary_tree_big_tree_linear_insertion():
    binary_tree_big_tree_linear_insertion(RedBlackBinaryTree())

@ timer_decorator("Red Black Binary Tree, Big Tree Random Insertion")
def test_red_black_binary_tree_big_tree_random_insertion():
    binary_tree_big_tree_random_insertion(RedBlackBinaryTree())