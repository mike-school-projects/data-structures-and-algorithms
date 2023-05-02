from data_structures.binary_tree import BinaryTree, Node
from data_structures.hashtable import Hashtable
from data_structures.queue import Queue

def tree_intersection(tree_a, tree_b):
    # Create temp variables
    hashtable = Hashtable(4096)
    tree_a_list = tree_a.pre_order()
    tree_b_list = tree_b.pre_order()
    output_list = []


    # Check empty
    if empty_tree(tree_a) or empty_tree(tree_b):
        return output_list

    # Add tree A to hashtable
    for item in tree_a_list:
        hashtable.set(item, None)

    keys = hashtable.keys()

    # Check to see if tree B items are in list
    for item in tree_b_list:
        if item in hashtable.keys():
            output_list.append(item)
            keys.remove(item)

    return sorted(output_list)

def empty_tree(tree):
    if tree.root.value == None and tree.root.right == None and tree.root.left == None:
        return True
    return False



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

if __name__ == "__main__":
    tree_a = BinaryTree()
    # values = [150, 100, 250, 75, 160, 200, 350, 125, 175, 300, 500]
    # add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    # values = [42, 100, 100, 15, 160, 200, 350, 125, 175, 4, 500]
    # add_values_to_empty_tree(tree_b, values)

    print(tree_intersection(tree_a, tree_b))
