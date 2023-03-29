if __name__ == '__main__':
    import sys
    sys.path.append('../python/linked_list')
    from linked_list import LinkedList
else:
    from linked_list.linked_list import LinkedList


def zip_lists(a, b):
    # Create variables, set current nodes to head
    current_node_1 = a.head
    current_node_2 = b.head

    # Check to see if linked list 1 is empty
    if current_node_1 is None:
        return b

    # Check to see if linked list 2 is empty
    if current_node_2 is None:
        return a

    while True:
        # Check for end of linked list 1
        if current_node_1._next is None:
            current_node_1._next = current_node_2
            b.head = None
            return a

        # Save old next
        current_node_1_old_next = current_node_1._next
        current_node_2_old_next = current_node_2._next

        # Re-direct next to zipper
        current_node_2._next = current_node_1._next
        current_node_1._next = current_node_2


        # Check for end of linked list 2
        if current_node_2._next is None:
            print("here")
            b.head = None
            return a

        # If not end, traverse
        current_node_1 = current_node_1_old_next
        current_node_2 = current_node_2_old_next



if __name__ == '__main__':
    list_a = LinkedList()
    list_b = LinkedList()
    for value in reversed(["a", "b", "c"]):
        list_b.insert(value)

    a = zip_lists(list_a, list_b)
    print(a)
