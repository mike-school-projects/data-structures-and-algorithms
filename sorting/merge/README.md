# Merge sort

## Algorithm

1. Input a list
2. Split list in half
3. MergeSort left (recursively) until each half is length=1
4. MergeSort right (recursively) until each half is length=1
5. Sort then merge together left and right into one list
- Compare first item on left with first item on right, add lower to output list
- Compare next items and continue until either left is right is done
- Add the leftover items to the end of output list

## Psuedocode
```pseudocode
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left

```

## Trace
```table

| Mergesort [8,4,23,42,16,15]                               |         | [8,4,23]               |               |            | [42,16,15] |
|-----------------------------------------------------------|---------|------------------------|---------------|------------|------------|
| Mergesort left [8,4,23]                                   |         | [8]                    | [4, 23]       |            | [42,16,15] |
| Mergesort left [8]                                        |         | [8]                    | [4, 23]       |            | [42,16,15] |
| Mergesort right [4, 23]                                   | not > 1 | [8]                    | [4]           | [23]       | [42,16,15] |
| Mergesort left [4]                                        | not > 1 | [8]                    | [4]           | [23]       | [42,16,15] |
| Mergesort right [23]                                      | not > 1 | [8]                    | [4]           | [23]       | [42,16,15] |
|                                                           |         |                        |               |            |            |
|                                                           |         | arr                    | i             | j          | k          |
| Merge [4], [23]                                           |         | []                     | 0             | 0          | 0          |
| while i < left.length && j < right.length                 | TRUE    | []                     | 0             | 0          | 0          |
| if left[i] <= right[j]                                    | TRUE    | []                     | 0             | 0          | 0          |
| arr[k] <-- left[i]                                        |         | [4]                    | 0             | 0          | 0          |
| i <-- i + 1                                               |         | [4]                    | 1             | 0          | 0          |
| k <-- k + 1                                               |         | [4]                    | 1             | 0          | 1          |
|                                                           |         |                        |               |            |            |
| while i < left.length && j < right.length                 | FALSE   | [4]                    | 1             | 0          | 1          |
| if i = left.length                                        | TRUE    | [4]                    | 1             | 0          | 1          |
| set remaining entries in arr to remaining values in right |         | [4, 23]                | 1             | 0          | 1          |
|                                                           |         |                        |               |            |            |
|                                                           |         | [8]                    | [4, 23]       | [42,16,15] |            |
|                                                           |         |                        |               |            |            |
|                                                           |         | arr                    | i             | j          | k          |
| Merge [8] , [4, 23]                                       |         | []                     | 0             | 0          | 0          |
| while i < left.length && j < right.length                 | TRUE    | []                     | 0             | 0          | 0          |
| if left[i] <= right[j]                                    | FALSE   | []                     | 0             | 0          | 0          |
| arr[k] <-- right[j]                                       |         | [4]                    | 0             | 0          | 0          |
| i <-- i + 1                                               |         | [4]                    | 0             | 1          | 0          |
| k <-- k + 1                                               |         | [4]                    | 0             | 1          | 1          |
|                                                           |         |                        |               |            |            |
| while i < left.length && j < right.length                 | TRUE    | [4]                    | 0             | 1          | 1          |
| if left[i] <= right[j]                                    | TRUE    | [4]                    | 0             | 1          | 1          |
| arr[k] <-- left[i]                                        |         | [4, 8]                 | 0             | 1          | 1          |
| i <-- i + 1                                               |         | [4, 8]                 | 1             | 1          | 1          |
| k <-- k + 1                                               |         | [4, 8]                 | 1             | 1          | 2          |
|                                                           |         |                        |               |            |            |
| while i < left.length && j < right.length                 | FALSE   | [4, 8]                 | 1             | 1          | 2          |
| if i = left.length                                        | FALSE   |                        |               |            |            |
| set remaining entries in arr to remaining values in left  |         | [4, 8, 23]             |               |            |            |
|                                                           |         |                        |               |            |            |
| Mergesort right [42, 16, 15]]                             |         | [4, 8, 23]             | [42]          | [16, 15]   |            |
| Mergesort left [42]                                       | not > 1 | [4, 8, 23]             | [42]          | [16, 15]   |            |
| Mergesort right [16, 15]                                  |         | [4, 8, 23]             | [42]          | [16]       | [15]       |
| Mergesort left [16]                                       | not > 1 | [4, 8, 23]             | [42]          | [16]       | [15]       |
| Mergesort right [15]                                      | not > 1 | [4, 8, 23]             | [42]          | [16]       | [15]       |
|                                                           |         |                        |               |            |            |
|                                                           |         | arr                    | i             | j          | k          |
| Merge [16], [15]                                          |         | []                     | 0             | 0          | 0          |
| while i < left.length && j < right.length                 | TRUE    |                        | 0             | 0          | 0          |
| if left[i] <= right[j]                                    | FALSE   |                        | 0             | 0          | 0          |
| arr[k] <-- right[j]                                       |         | [15]                   | 0             | 0          | 0          |
| j <-- j + 1                                               |         | [15]                   | 0             | 1          | 0          |
| k <-- k + 1                                               |         | [15]                   | 0             | 0          | 1          |
|                                                           |         |                        |               |            |            |
| while i < left.length && j < right.length                 | FALSE   | [15]                   | 0             | 0          | 1          |
| if i = left.length                                        | TRUE    |                        | 0             | 0          | 1          |
| set remaining entries in arr to remaining values in left  |         | [15, 16]               | 0             | 0          | 1          |
|                                                           |         |                        |               |            |            |
| Merge [42], [15, 16]                                      |         | arr                    | i             | j          | k          |
| while i < left.length && j < right.length                 | TRUE    | [ ]                    | 0             | 0          | 0          |
| if left[i] <= right[j]                                    | FALSE   |                        | 0             | 0          | 0          |
| arr[k] <-- right[j]                                       |         | [15]                   | 0             | 0          | 0          |
| j <-- j + 1                                               |         | [15]                   | 0             | 1          | 0          |
| k <-- k + 1                                               |         | [15]                   | 0             | 1          | 1          |
|                                                           |         |                        |               |            |            |
| while i < left.length && j < right.length                 | TRUE    | [15]                   | 0             | 1          | 1          |
| if left[i] <= right[j]                                    | FALSE   | [15]                   | 0             | 1          | 1          |
| arr[k] <-- right[j]                                       |         | [15, 16]               | 0             | 1          | 1          |
| j <-- j + 1                                               |         | [15, 16]               | 0             | 2          | 1          |
| k <-- k + 1                                               |         | [15, 16]               | 0             | 2          | 2          |
|                                                           |         |                        |               |            |            |
| if i = left.length                                        | FALSE   | [15, 16]               | 0             | 1          | 1          |
| set remaining entries in arr to remaining values in left  |         | [15, 16, 42]]          | 0             | 1          | 1          |
|                                                           |         |                        |               |            |            |
|                                                           |         | [4, 8, 23]             | [15, 16, 42]] |            |            |
|                                                           |         |                        |               |            |            |
| Merge [4,8,23], [15,16,42]                                |         | arr                    | i             | j          | k          |
| while i < left.length && j < right.length                 | TRUE    | [ ]                    | 0             | 0          | 0          |
| if left[i] <= right[j]                                    | TRUE    | [ ]                    | 0             | 0          | 0          |
| arr[k] <-- left[i]                                        |         | [4]                    | 0             | 0          | 0          |
| i <-- i + 1                                               |         | [4]                    | 1             | 0          | 0          |
| k <-- k + 1                                               |         | [4]                    | 1             | 0          | 1          |
|                                                           |         |                        |               |            |            |
| while i < left.length && j < right.length                 | TRUE    | [4]                    | 1             | 0          | 1          |
| if left[i] <= right[j]                                    | TRUE    | [4]                    | 1             | 0          | 1          |
| arr[k] <-- left[i]                                        |         | [4, 8]                 | 1             | 0          | 1          |
| i <-- i + 1                                               |         | [4, 8]                 | 2             | 0          | 1          |
| k <-- k + 1                                               |         | [4, 8]                 | 2             | 0          | 2          |
|                                                           |         |                        |               |            |            |
| while i < left.length && j < right.length                 | TRUE    | [4, 8]                 | 2             | 0          | 2          |
| if left[i] <= right[j]                                    | FALSE   | [4, 8]                 | 2             | 0          | 2          |
| arr[k] <-- right[j]                                       |         | [4, 8, 15]             | 2             | 0          | 2          |
| j <-- j + 1                                               |         | [4, 8, 15]             | 2             | 1          | 2          |
| k <-- k + 1                                               |         | [4, 8, 15]             | 2             | 1          | 3          |
|                                                           |         |                        |               |            |            |
| while i < left.length && j < right.length                 | TRUE    | [4, 8, 15]             | 2             | 1          | 3          |
| if left[i] <= right[j]                                    | FALSE   | [4, 8, 15]             | 2             | 1          | 3          |
| arr[k] <-- right[j]                                       |         | [4, 8, 15, 16]         | 2             | 1          | 3          |
| j <-- j + 1                                               |         | [4, 8, 15, 16]         | 2             | 2          | 3          |
| k <-- k + 1                                               |         | [4, 8, 15, 16]         | 2             | 2          | 4          |
|                                                           |         |                        |               |            |            |
| while i < left.length && j < right.length                 | TRUE    | [4, 8, 15, 16]         | 2             | 2          | 4          |
| if left[i] <= right[j]                                    | TRUE    | [4, 8, 15, 16]         | 2             | 2          | 4          |
| arr[k] <-- left[i]                                        |         | [4, 8, 15, 16, 23]     | 2             | 2          | 4          |
| i <-- i + 1                                               |         | [4, 8, 15, 16, 23]     | 3             | 2          | 5          |
| k <-- k + 1                                               |         | [4, 8, 15, 16, 23]     | 3             | 2          | 5          |
|                                                           |         |                        |               |            |            |
| while i < left.length && j < right.length                 | FALSE   | [4, 8, 15, 16, 23]     | 3             | 2          | 5          |
| if i = left.length                                        | TRUE    | [4, 8, 15, 16, 23]     | 3             | 2          | 5          |
| set remaining entries in arr to remaining values in right |         | [4, 8, 15, 16, 23, 42] | 3             | 2          | 5          |




```

## Efficiency

Time: O(log n) because we continually half-split the length of the list

Space: O(n) because we need to create 1 new data structure to hold the new list

## Solution

[Link to code](https://github.com/mikeshen7/data-structures-and-algorithms/blob/main/sorting/insertion/insertion_sort.py)

To run file, from sorting/merge directory:

python merge.py

To test, from sorting/merge directory:

pytest
