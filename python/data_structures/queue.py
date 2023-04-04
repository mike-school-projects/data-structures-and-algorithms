from data_structures.invalid_operation_error import InvalidOperationError

class Queue:
    """
    Node-based queue object class
    """

    def __init__(self):
        self.front = None
        self.back = None

    def some_method(self):
        # method body here
        pass

    def enqueue(self, value_arg):
        # adds a new node with that value to the back of the queue with an O(1) Time performance

        if self.is_empty() is True:
            # Create new Node with value
            new_node = Node(value_arg)

            # Point front and back to new_node
            self.back = new_node
            self.front = new_node

        else:
            # Create new Node with value
            new_node = Node(value_arg)

            # Point the old back to new node
            self.back.next = new_node

            # Point back to new Node
            self.back = new_node

    def dequeue(self):
        # Returns: the value from node from the front of the queue
        # Removes the node from the front of the queue
        # Should raise exception when called on empty queue

        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")

        else:
            old_front_value = self.front.value
            self.front = self.front.next
            return old_front_value

    def peek(self):
        # Returns value of the node located at the front of the queue
        # Raise exception when called on empty stack

        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        else:
            return self.front.value

    def is_empty(self):
        # Returns boolean indicating whether or not the queue is empty
        if self.front is None:
            return True
        else:
            return False


class Node:
    # Code taken from today's lecture
    """"
    A node in a singly-linked list.

    Attributes:
        value (any): The value stored in the node.
        next (Node): The next node in the list.
    """

    def __init__(self, value, next=None):
        # value, next
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())

