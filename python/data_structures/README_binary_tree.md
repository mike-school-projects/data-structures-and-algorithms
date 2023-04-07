# Binary Tree

## Node
Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

## Binary Tree
Create a Binary Tree class.  Define a method for each of the depth first traversals:
1. pre order
2. in order
3. post order

Each depth first traversal method should return an array of values, ordered appropriately.

## Binary Search Tree
Create a Binary Search Tree class

This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:

Add
1. Arguments: value
2. Return: nothing
3. Adds a new node with that value in the correct location in the binary search tree.

Contains
1. Argument: value
2. Returns: boolean indicating whether or not the value is in the tree at least once.

## Whiteboard Process
![Whiteboard image](whiteboard_15.png)

[Whiteboard link](https://)

## Approach & Efficiency

Create Node class

Create helper recursive function to go root/right/left, depending on the type of order.

Time: O(log n) because we will normally split the data in half as we traverse

Space: O(1) becuase no additional data structures need to be created

## Solution

[Link to code](https://github.com/mikeshen7/data-structures-and-algorithms/blob/main/python/data_structures/binary_tree.py)

[Link to code](https://github.com/mikeshen7/data-structures-and-algorithms/blob/main/python/data_structures/binary_search_tree.py)

To run file, from python directory:

python -m data_structures.binary_tree

python -m data_structures.binary_search_tree

To test, from python directory:

pytest
