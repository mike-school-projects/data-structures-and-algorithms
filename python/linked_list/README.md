# Challenge Linked List
Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
Methods:
1. insert.  Args: value, Return: none, adds new node with value to the head of the list with O(1) time
2. includes.  Args: value.  Returns boolean if value exists
3. to_string.  Args: none.  Returns string representing all values in the Linked List.  "{ a } -> { b } -> { c } -> NULL"

## Whiteboard Process
N/A for today's code challenge


## Approach & Efficiency
For traversing, use while loop.
Check to see if head is None.
Otherwise, set current to next head and loop.

Insert
Time: O(1) because it always takes one step to insert at the head
Space: O(n) because it takes the space of the new Node

__str__
Time: O(n) because you have to traverse the entire linked list
Space: O(1) because you're always just returning one string

## Solution
[Link to code](https://github.com/mikeshen7/data-structures-and-algorithms/blob/main/python/linked_list/linked_list.py)

Run from python folder:
to run single instance: python linked_list/linked_list.py
to run test: pytest
