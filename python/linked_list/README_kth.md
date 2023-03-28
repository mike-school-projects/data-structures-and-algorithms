# Challenge Linked List - kth from end
Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
Methods:
1. insert.  Args: value, Return: none, adds new node with value to the head of the list with O(1) time
2. includes.  Args: value.  Returns boolean if value exists
3. to_string.  Args: none.  Returns string representing all values in the Linked List.  "{ a } -> { b } -> { c } -> NULL"
4. append.  Args: value.  Return: none, add new node to the end of the list
5. insert_before.  Arge: target, value.  Return: none.  Add new node before the node with the target value.
6. insert_after.  Arge: target, value.  Return: none.  Add new node after the node with the target value.

## Whiteboard Process
![Whiteboard image](whiteboard07.png)

[Whiteboard link](https://mikeshen926191.invisionapp.com/freehand/Code-Challenge-07-xICsiMtEB?dsid_h=0409fac6aa1c64050f05c00c7b6fabbdf2cedd3bd26c8e2f424cf36cb97ed41b&uid_h=cb08dec7ece6a9f52098e8b9edfd4330e40a53876f81c120382ecff9ccb5784d)

## Approach & Efficiency
Use two placeholders.
Traverse one kth time over, and leave the other at head.
Then traverse both at the same time

Time: O(n) because it always takes one step to insert at the head
Space: O(n) because it takes the space of the new Node

__str__
Time: O(n) because we always have to traverse to the end, but we can do both placeholders together
Space: O(1) because I just need two variables: kth_from_current_node and current_node

## Solution
[Link to code](https://github.com/mikeshen7/data-structures-and-algorithms/blob/main/python/linked_list/linked_list.py)

Run from python folder:
to run single instance: python linked_list/linked_list.py
to run test: pytest
