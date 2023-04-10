# Binary Tree - find max

Write the following method for the Binary Tree class
find maximum value
Arguments: none
Returns: number
Find the maximum value stored in the tree. You can assume that the values stored in the Binary Tree will be numeric.

## Whiteboard Process

![Whiteboard image](whiteboard16.png)

[Whiteboard link](https://www.figma.com/file/CGQc87v265OYPvLaPyDD3g/Code-Challenge-16?node-id=0%3A1&t=MegTlgiZNiz5eXnb-1)

## Approach & Efficiency

* Check empty tree - return none
* Check root-only tree - return self.root.value
* Create temp variable max_value, set to self.root.value
* Do pre-order traversal (root, left, right)
* Check if node value is > max_value, save to max_value
* Continue recursive loop
* Return max_value

Time: O(n) because we need to traverse through the entire tree

Space: O(1) because no additional data structures need to be created

## Solution

[Link to BT code](https://github.com/mikeshen7/data-structures-and-algorithms/blob/main/python/data_structures/binary_tree.py)

To run file, from python directory:

python -m data_structures.binary_tree

To test, from python directory:

pytest
