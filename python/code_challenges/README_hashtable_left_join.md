# Hashtable Left Join

Write a function that LEFT JOINs two hashmaps into a single data structure.

Write a function called left join
- Arguments: two hash maps
- The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
- The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
- Return: The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic
- Combine the key and corresponding values (if they exist) into a new data structure according to LEFT JOIN logic.
- LEFT JOIN means all the values in the first hashmap are returned, and if values exist in the “right” hashmap, they are appended to the result row.
- If no values exist in the right hashmap, then some flavor of NULL should be appended to the result row.

## Whiteboard Process
![Whiteboard image](whiteboard_33.png)

[Whiteboard link](https://www.figma.com/file/2ApMk8Jcrcx0Hl3rGGJ7pe/Code-Challenge-33?type=whiteboard&node-id=1%3A204&t=YwjokZr0bX2nPEvG-1)

## Approach & Efficiency

1. Create empty hashtable
2. Get list of keys for hash1 and hash2
3. Iterate through hash1_keys:
- value = hash1 value
- if hash2 exists for the same key, append it to value.  If not, append None
- set value into hashtable
4. Return hashtable

Time: O(n) because we have to iterate through the entire left hashtable

Space: O(n) because we need to create 1 temporary hashtable


## Solution

[Link to code](https://github.com/mikeshen7/data-structures-and-algorithms/blob/main/python/code_challenges/hashtable_left_join.py)

To run file, from python directory:

python -m code_challenges.hashtable_left_join

To test, from python directory:

pytest


