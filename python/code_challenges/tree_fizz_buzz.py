from data_structures.kary_tree import KaryTree, Node
from data_structures.queue import Queue

def fizz_buzz_tree(input_tree):
    # empty tree
    if input_tree.root is None:
        return input_tree

    # 1 node tree
    if len(input_tree.root.children) == 0:
        output_tree = KaryTree()
        output_tree.root = Node(str(input_tree.root.value))
        return output_tree

    output_tree = KaryTree()
    output_tree.root = Node(None)

    input_queue = Queue()
    output_queue = Queue()

    input_queue.enqueue((input_tree.root))
    output_queue.enqueue((output_tree.root))

    while input_queue.is_empty() is False:
        current_input_node = input_queue.dequeue()
        current_output_node = output_queue.dequeue()

        # Set value of output_tree node based on fizz buzz logic
        if current_input_node.value == 0:
            print('here')
            current_output_node.value = str('0')
        elif type(current_input_node.value) is not int:
            current_output_node.value = current_input_node.value
        elif current_input_node.value % 15 == 0:
            current_output_node.value = "FizzBuzz"
        elif current_input_node.value % 3 == 0:
            current_output_node.value = "Fizz"
        elif current_input_node.value % 5 == 0:
            current_output_node.value = "Buzz"
        else:
            current_output_node.value = str(current_input_node.value)

        if len(current_input_node.children) > 0:
            for index, input_node_child in enumerate(current_input_node.children):
                # Create child node on output_tree
                output_node_child = Node(None)
                current_output_node.children.append(output_node_child)

                # Add child to queues
                input_queue.enqueue(input_node_child)
                output_queue.enqueue(output_node_child)

    return output_tree

if __name__ == "__main__":
    empty_tree = KaryTree()
    empty_tree.root = Node(0)
    output = fizz_buzz_tree(empty_tree)
    output = output.breadth_first()

    print(output)


