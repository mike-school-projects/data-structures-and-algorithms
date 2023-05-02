import pytest
from code_challenges.tree_intersection import tree_intersection, empty_tree
from data_structures.binary_tree import BinaryTree, Node
from data_structures.queue import Queue


def test_exists():
    assert tree_intersection


@pytest.mark.skip("TODO")
def test_tree_intersection():

    tree_a = BinaryTree()
    values = [150, 100, 250, 75, 160, 200, 350, 125, 175, 300, 500]
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    values = [42, 100, 100, 15, 160, 200, 350, 125, 175, 4, 500]
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a, tree_b)
    expected = [125, 175, 100, 160, 500, 200, 350]

    assert sorted(actual) == sorted(expected)

def test_tree_empty():

    tree_a = BinaryTree()
    tree_b = BinaryTree()
    actual = tree_intersection(tree_a, tree_b)
    expected = []

    assert sorted(actual) == sorted(expected)

def test_tree_duplicates():

    tree_a = BinaryTree()
    values = [100, 100, 100]
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    values = [100]
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a, tree_b)
    expected = [100]

    assert sorted(actual) == sorted(expected)

def test_tree_duplicates_alt():

    tree_a = BinaryTree()
    values = [100]
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    values = [100, 100, 100]
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a, tree_b)
    expected = [100]

    assert sorted(actual) == sorted(expected)

def test_tree_strings():

    tree_a = BinaryTree()
    values = [1, 2, 3, 4, 'a']
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    values = [5, 6, 7, 'a', 8]
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a, tree_b)
    expected = ['a']

    assert sorted(actual) == sorted(expected)


def test_tree_no_match():

    tree_a = BinaryTree()
    values = [1,2,3,4,5]
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    values = [6,7,8,9,10]
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a, tree_b)
    expected = []

    assert sorted(actual) == sorted(expected)

def test_empty_tree_1():

    tree_a = BinaryTree()
    values = [1,2,3,4,5]
    add_values_to_empty_tree(tree_a, values)

    actual = empty_tree(tree_a)
    expected = False

    assert actual == expected

def test_empty_tree_2():

    tree_a = BinaryTree()

    actual = empty_tree(tree_a)
    expected = True

    assert actual == expected

def test_empty_tree_3():

    tree_a = BinaryTree()
    values = [None]
    add_values_to_empty_tree(tree_a, values)

    actual = empty_tree(tree_a)
    expected = True

    assert actual == expected


def add_values_to_empty_tree(tree, values):
    """
    Helper function to add given values to BinaryTree
    """
    tree.root = Node(values.pop())
    q = Queue()

    q.enqueue(tree.root)

    while values:
        node = q.dequeue()
        node.left = Node(values.pop())
        node.right = Node(values.pop()) if values else None
        q.enqueue(node.left)
        q.enqueue(node.right)
