# Challenge Linked List
Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
Methods:
1. insert.  Args: value, Return: none, adds new node with value to the head of the list with O(1) time
2. includes.  Args: value.  Returns boolean if value exists
3. to_string.  Args: none.  Returns string representing all values in the Linked List.  "{ a } -> { b } -> { c } -> NULL"

## Whiteboard Process
N/A for today's code challenge


## Approach & Efficiency
Split in half and check if above or below middle
Continue until you find the key
Time: O(log N) because we're always cutting the array in half so as the list gets bigger, time to search increased logrithmically
Space: O(1) because the space required is always just the size of the list + a few variables

## Solution
[Link to code](https://github.com/mikeshen7/data-structures-and-algorithms/blob/main/python/code_challenges/array_binary_search/binary_search.py)

Run from python folder:
to run single instance: python linked_list/linked_list.py
to run test: pytest
