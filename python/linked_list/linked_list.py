class LinkedList:
    """
    A singly-linked list.

    Attributes:
        head (Node): The first node in the linked list.
    """

    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        values = ""
        current = self.head

        while current is not None:
            values = values + '{ ' + current.value + ' } -> '
            current = current._next
        else:
            values = f'{values}NULL'

        return values



    def traverse_list(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current._next
        return "NULL"

    def insert(self, value):
        # Create a node which points at self.head
        node = Node(value, self.head)

        # Redirect self.head to new node
        self.head = node

    def includes(self, value):
        current = self.head
        while current is not None:
            if value in current.value:
                return True
            current = current._next
        return False


class Node:
    # Code taken from today's lecture
    """"
    A node in a singly-linked list.

    Attributes:
        value (any): The value stored in the node.
        next (Node): The next node in the list.
    """

    def __init__(self, value, _next=None):
        # value, next
        self.value = value
        self._next = _next

    def __str__(self):
        return self.value

class TargetError:
    pass

if __name__ == '__main__':

    linked_list = LinkedList()
    linked_list.insert("apple")
    linked_list.insert("banana")
    print(str(linked_list))
