# Binary Tree - Breadth

## Node
Write a function called breadth first

Arguments: tree

Return: list of all values in the tree, in the order they were encountered

## Whiteboard Process

![Whiteboard image](whiteboard17.png)

[Whiteboard link](https://www.figma.com/file/9tSVupQomIrhO6A1nxfDvm/Code-Challenge-17?node-id=0%3A1&t=EBbzgChc8pYNMirh-1)


## Approach & Efficiency

1. Create temp list of lists output_list
2. Check for empty, return empty list
3. Check for only 1 node
4. Traverse, passing in depth=1 as an argument
   1. Check output_list size, add empty list if necessary
   2. Root first: Append value to output_list[depth]
   3. Go Right, with depth+1
   4. Go Left, with depth+1
5. Combine list together and return


Time: O(n) because we need to traverse through every node

Space: O(n) because we need a temporary list to hold all the data

## Solution

[Link to code](https://github.com/mikeshen7/data-structures-and-algorithms/blob/main/python/code_challenges/tree_breadth_first.py)

To run file, from python directory:

python -m code_challenges.tree_breadth_first

To test, from python directory:

pytest
