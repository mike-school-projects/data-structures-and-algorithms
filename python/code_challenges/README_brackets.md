# Validate Brackets
Write a function called validate brackets

Arguments: string

Return: boolean representing whether or not the brackets in the string are balanced

## Whiteboard Process
![Whiteboard image](whiteboard13.png)

[Whiteboard link](https://www.figma.com/file/r1h8jhIDrUoilGSbWEBdY1/Code-Challenge-13?node-id=0%3A1&t=QCQh9MhCQZ4weK5w-1)

## Approach & Efficiency

Create a stack.

Loop thru string:

If open bracket - push to stack.

If close bracket - pop from stack.
- If empty, return false
- If unmatched, return false

Time: O(n) because we need to iterate through the entire string every time.

Space: O(n) because we need to create a temp stack to store the values.

## Solution

[Link to code](https://github.com/mikeshen7/data-structures-and-algorithms/blob/main/python/code_challenges/stack_queue_brackets.py)

To run file, from python directory:

python -m code_challenges.stack_queue_brackets

To test, from python directory:

pytest


