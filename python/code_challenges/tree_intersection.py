from data_structures.binary_tree import BinaryTree
from data_structures.binary_tree import BinaryTree, Node
from data_structures.queue import Queue

def tree_intersection(tree_a, tree_b):
    # Tree A - pre-order traverse to list
    tree_a_list = tree_a.pre_order()
    output_list = []

    # Tree B - pre-order traverse
    # If current value is in tree a list, append to output list and remove from tree a list
    def traverse(current_node):
        nonlocal tree_a_list
        nonlocal output_list

        if not current_node:
            return

        # Root
        if current_node.value in tree_a_list:
            output_list.append(current_node.value)
            tree_a_list.remove(current_node.value)

        if current_node.left:
            traverse(current_node.left)

        if current_node.right:
            traverse(current_node.right)

    traverse(tree_b.root)

    return output_list

if __name__ == "__main__":
    tree_a = BinaryTree()
    tree_a.root = Node(500)
    tree_a.root.left = Node(300)
    tree_a.root.right = Node(175)

    tree_a.root.left.left = Node(125)
    tree_a.root.left.right = Node(350)

    tree_a.root.left.left.left = Node(75)
    tree_a.root.left.left.right = Node(250)

    tree_a.root.left.right.left = Node(100)
    tree_a.root.left.right.right = Node(150)

    tree_a.root.right.left = Node(200)
    tree_a.root.right.right = Node(160)



    tree_b = BinaryTree()
    tree_b.root = Node(42)
    tree_b.root.left = Node(100)
    tree_b.root.right = Node(100)

    tree_b.root.left.left = Node(15)
    tree_b.root.left.right = Node(160)

    tree_b.root.left.left.left = Node(125)
    tree_b.root.left.left.right = Node(175)

    tree_b.root.left.right.left = Node(4)
    tree_b.root.left.right.right = Node(500)

    tree_b.root.right.left = Node(200)
    tree_b.root.right.right = Node(350)


    print(tree_intersection(tree_a, tree_b))
