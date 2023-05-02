class Node:
    """"
    A node in a binary tree list.

    Attributes:
        value: value (any)
        left: Node()
        right: Node()
    """

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self):
        self.root = Node()

    def pre_order(self, values=[]):
        # Root -> left -> right
        output = []

        def traverse(current_node):
            if not current_node:
                return

            # Root
            output.append(current_node.value)

            # Left
            if current_node.left:
                traverse(current_node.left)

            # Right
            if current_node.right:
                traverse(current_node.right)

            return output

        traverse(self.root)

        return output

    def in_order(self):
        # left -> root -> right
        output = []

        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)

            output.append(current_node.value)

            if current_node.right:
                traverse(current_node.right)

        traverse(self.root)

        return output

    def post_order(self):
        # left -> right -> root
        output = []

        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)

            if current_node.right:
                traverse(current_node.right)

            output.append(current_node.value)

        traverse(self.root)

        return output

    def find_maximum_value(self):
        # No arguments
        # Returns number
        # Cannot call one of 3 original traversals.  Can redo it.

        # Empty Tree
        if self.root is None:
            return None

        # Root-only Tree
        if self.root.left is None and self.root.right is None:
            return self.root.value

        max_value = self.root.value

        def traverse(node):
            nonlocal max_value

            # Root
            if node.value > max_value:
                max_value = node.value

            # Left
            if node.left is not None:
                traverse(node.left)

            # Right
            if node.right is not None:
                traverse(node.right)

        traverse(self.root)

        return max_value



if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(-7)
    print(tree.find_maximum_value())

