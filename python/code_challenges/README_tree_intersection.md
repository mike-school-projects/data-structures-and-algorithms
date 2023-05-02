# Tree Intersection

Write a function called tree_intersection that takes two binary trees as parameters.

Using your Hashmap implementation as a part of your algorithm, return a set of values found in both trees.

## Whiteboard Process
![Whiteboard image](whiteboard_32.png)

[Whiteboard link](https://www.figma.com/file/yCCEnXuOiumCLE1rE26F3s/Code-Challenge-32?type=whiteboard&node-id=0%3A1&t=MRlSZvhTVxcZvP5m-1)

## Approach & Efficiency

Check empty - return empty list

Create temp output_list

Create list of tree a and tree b

Add A to hashtable

Iterate through tree B.
- If item in keys, add to output list.  Pop from tree A

Return output_list

Time: O(n) because we have to go through both trees completely

Space: O(3n) because worst case, we will create 3 temporary lists for a, b, and output

## Solution

[Link to code](https://github.com/mikeshen7/data-structures-and-algorithms/blob/main/python/code_challenges/tree_intersection.py)

To run file, from python directory:

python -m code_challenges.tree_intersection

To test, from python directory:

pytest


