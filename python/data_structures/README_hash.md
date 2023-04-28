# Hash Table

Implement a Hashtable Class with the following methods:

set
- Arguments: key, value
- Returns: nothing
- This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
- Should a given key already exist, replace its value from the value argument given to this method.

get
- Arguments: key
- Returns: Value associated with that key in the table

has
- Arguments: key
- Returns: Boolean, indicating if the key exists in the table already.

keys
- Returns: Collection of keys

hash
- Arguments: key
- Returns: Index in the collection for that key

## Whiteboard Process

N/A

## Approach & Efficiency

Create Node class that hold a key/value pair in a list.

Node class has display() method to return list of key/value pari.

Node class has get_value() method to return value.

Hashtable class hashes the key with a basic ascii character value hash.

Hashtable class has set, get, has, hash, and keys functions


Time: O(1) because hashtable has immediate lookup times with a set key.

Space: O(1) because no additional data structures are required.

## Solution

[Link to code](https://github.com/mikeshen7/data-structures-and-algorithms/blob/main/python/data_structures/hashtable.py)


To run file, from python directory:

python -m data_structures.hashtable

To test, from python directory:

pytest
