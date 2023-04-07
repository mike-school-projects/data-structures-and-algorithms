from data_structures.binary_tree import BinaryTree
from data_structures.binary_tree import Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    def __init__(self, node=None):
        self.root = node


    def add(self, value):
        # empty tree
        if self.root is None:
            self.root = Node(value)
            return

        def traverse(current_node):
            # If current is None, add here
            if current_node is None:
                current_node = Node(value)
                return

            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = Node(value)
                    return
                traverse(current_node.left)

            else:
                if current_node.right is None:
                    current_node.right = Node(value)
                    return
                traverse(current_node.right)

        traverse(self.root)

    def contains(self, value):
        present = False

        if self.root is None:
            return False

        def traverse(current_node):
            nonlocal present

            if current_node.value == value:
                present = True
                return

            elif value < current_node.value and current_node.left is not None:
                traverse(current_node.left)

            elif current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)

        return present

if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    print(tree.root.left.value)
