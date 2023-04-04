# Animal Shelter

Create a class called AnimalShelter which holds only dogs and cats.

The shelter operates using a first-in, first-out approach.

Implement the following methods:
1. enqueue
- Arguments: animal
- animal can be either a dog or a cat object.
- It must have a species property that is either "cat" or "dog"
- It must have a name property that is a string.

2. dequeue
- Arguments: pref
- pref can be either "dog" or "cat"
- Return: either a dog or a cat, based on preference.
- If pref is not "dog" or "cat" then return null.


## Whiteboard Process
![Whiteboard image](whiteboard_12.png)

[Whiteboard link](https://www.figma.com/file/Jd7vCe1vErGLFJfhyIeMmU/Code-Challenge-12?node-id=0%3A1&t=WHHmQJVKgP0jI5qf-1)

## Approach & Efficiency

1. Create AnimalShelter class with 2 queues: one for dog, one for cat.

Time: O(1), because we can always find a dog or cat that we need.

Space: O(1), because we don't need to create any temporary arrays.


## Solution

[Link to code](https://github.com/mikeshen7/data-structures-and-algorithms/blob/main/python/code_challenges/stack_queue_pseudo.py)

To run file, from python directory:

python -m code_challenges.stack_queue_animal_shelter

To test, from python directory:

pytest
