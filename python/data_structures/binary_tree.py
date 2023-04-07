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

        def traverse(current_node, output):
            if not current_node:
                return

            # Root
            output.append(current_node.value)

            # Left
            if current_node.left:
                traverse(current_node.left, output)

            # Right
            if current_node.right:
                traverse(current_node.right, output)

        traverse(self.root, values)

        return values

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

if __name__ == "__main__":
    tree = BinaryTree()

    tree.root = Node("a")
    tree.root.left = Node("b")
    tree.root.right = Node("c")
    tree.root.left.left = Node("d")
    tree.root.left.right = Node("e")
    tree.root.right.left = Node("f")
    tree.root.right.right = Node("g")
    print(tree.pre_order())
    # print(tree.root.left.left.left)
