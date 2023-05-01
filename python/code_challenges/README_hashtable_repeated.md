# Code Challenge 31 Hashtable Repeated Word

Write a function called repeated word that finds the first word to occur more than once in a string.

Arguments: string

Return: string

## Whiteboard Process
![Whiteboard image](whiteboard_12.png)

[Whiteboard link](https://www.figma.com/file/eM1BWi3FdshxBdXsdON2dv/Code-Challenge-31?type=whiteboard&node-id=0%3A1&t=zEnKMzEKx6mG12cx-1)

## Approach & Efficiency

- Create a temp hashtable
- Break string into list of words.  Remove punctuation immediately before / after the word
- Iterate through list
1. Check to see if word is in hashtable
2. If has = true, return word
- If no match, return None

Time: O(2n) = O(n) because worst case will need to iterate through entire string twice

Space: O(2n) = O(n) because worst case we will need both a list and a hashtable of size n.


## Solution

[Link to code](https://github.com/mikeshen7/data-structures-and-algorithms/blob/main/python/code_challenges/hashtable_repeated_word.py)

To run file, from python directory:

python -m code_challenges.hashtable_repeated_word

To test, from python directory:

pytest
