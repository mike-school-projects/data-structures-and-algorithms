from data_structures.binary_tree import BinaryTree, Node

def breadth_first(tree_input):
    # Initialize output_list
    output_list = [[],]

    # Check for empty tree
    if tree_input.root.value is None:
        return join_list(output_list)

    # Check for 1 node
    if tree_input.root.left is None and tree_input.root.right is None:
        output_list[0].append(tree_input.root.value)
        return join_list(output_list)

    def traverse(node, depth):
        nonlocal output_list
        # initialize output_list
        if len(output_list) <= depth:
            output_list.append([])

        # Root
        output_list[depth].append(node.value)

        # Left
        if node.left:
            traverse(node.left, depth+1)

        # Right
        if node.right:
            traverse(node.right, depth+1)


    traverse(tree_input.root, 0)
    return join_list(output_list)

def join_list(list_input):
    output_list = []
    for list_item in list_input:
        output_list += list_item
    return output_list

if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node("apples")
    tree.root.left = Node("bananas")
    tree.root.right = Node("cucumbers")
    tree.root.right.right = Node("dates")
    print(breadth_first(tree))
