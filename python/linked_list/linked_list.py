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
            values = values + '{ ' + str(current.value) + ' } -> '
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

    def append(self, value):
        # Create new node
        new_node = Node(value)

        # Traverse to find end of linked list
        current_node = self.head
        print(current_node)

        while current_node._next is not None:
            current_node = current_node._next

        # Point last node to new node
        current_node._next = new_node

        return

    def insert_before(self,target,value):
        # Create new node
        new_node = Node(value)

        # if linked list is empty, raise TargetError
        if self.head == None:
            raise TargetError
            return

        # Initialize current_node
        current_node = self.head

        # 1st node test - node is target
        if current_node.value == target:
            new_node._next = current_node
            self.head = new_node
            return

        # 1st node test - node is not the target and is only node in linked_list
        if current_node._next is None:
            raise TargetError
            return

        # linked_list is multi-nodes
        previous_node = current_node
        current_node = current_node._next
        print(f'Previous Node: {previous_node}')
        print(f'Current Node: {current_node}')

        while True:
            if current_node.value == target:
                new_node._next = current_node
                previous_node._next = new_node
                return

            if current_node._next is None:
                raise TargetError
                return

            previous_node = current_node
            current_node = current_node._next

        return

    def insert_after(self,target,value):
        # Create new node
        new_node = Node(value)

        # if linked list is empty, raise TargetError
        if self.head == None:
            raise TargetError
            return

        # Initialize current_node
        current_node = self.head

        # Traverse to find node where current node's value is the target
        current_node = self.head

        while current_node.value != target:
            if current_node._next is None:
                raise TargetError
                return
            current_node = current_node._next

        # Point new_node to next node
        new_node._next = current_node._next

        # Point current node to new_node
        current_node._next = new_node

        return

    def kth_from_end(self, k):
        # Check for bad k input

        if type(k) != int or k < 0:
            raise TargetError
            return

        # Set both placeholders to head
        kth_node_from_current = self.head
        current_node = self.head

        # Traverse current_node to kth position
        for node in range(k+1):
            if current_node is None:
                raise TargetError
                return
            else:
                current_node = current_node._next

        # Traverse together until the end
        while True:
            if current_node is None:
                return kth_node_from_current.value
            else:
                current_node = current_node._next
                kth_node_from_current = kth_node_from_current._next


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
        return str(self.value)

class TargetError(Exception):
    pass

if __name__ == '__main__':
    linked_list = LinkedList()
    values = ["apples", "bananas", "cucumbers"]
    for value in reversed(values):
        linked_list.insert(value)
    print(str(linked_list))
    print(linked_list.kth_from_end((1)))


