from data_structures.invalid_operation_error import InvalidOperationError

class Stack:
    """
    Node-based stack object class
    """

    def __init__(self, value=None):
        self.top = Node(value)

    def push(self, value_arg):
        # adds a new node with that value to the top of the stack with O(1) time performance
        # no return

        # Create new Node with value
        new_node = Node(value_arg)

        # Point new Node to top
        new_node.next = self.top

        # Point top to new Node
        self.top = new_node

    def pop(self):
        # Returns value from node from the top of the stack
        # Removes the node from the top of the stack
        # Raise exception when called on empty stack

        try:
            if self.is_empty():
                raise InvalidOperationError("Method not allowed on empty collection")
            else:
                old_top_value = self.top.value
                self.top = self.top.next
                return old_top_value
        except InvalidOperationError:
            raise InvalidOperationError("Method not allowed on empty collection")

    def peek(self):
        # Returns value of the node located at the top of the stack
        # Raise exception when called on empty stack
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        else:
            return self.top.value

    def is_empty(self):
        # Returns boolean indicating whether or not the stack is empty
        if self.top.value is None:
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
    s = Stack()
    s.pop()

