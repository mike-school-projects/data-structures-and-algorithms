# Insertion Sort

## Algorithm

1. Create a temp list to store sorted values
2. Add the first number from the input list to sorted_list
3. Outer loop: call insert() function for each item in the input list, starting from the 2nd number
- Iterate through sorted list to find the index where the 2nd number is greater than sorted_list index value
4. Inner loop: compare and swap
- Take the value that was at that sorted_list index and append it to the end of the list
- Replace value into that spot
- Iterate through the rest of the sorted_list and replace and append


## Psuedocode
```pseudocode
Insert(int[] sorted, int value)
  initialize i to 0
  WHILE value > sorted[i]
    set i to i + 1
  WHILE i < sorted.length
    set temp to sorted[i]
    set sorted[i] to value
    set value to temp
    set i to i + 1
  append value to sorted

InsertionSort(int[] input)
  LET sorted = New Empty Array
  sorted[0] = input[0]
  FOR i from 1 up to input.length
    Insert(sorted, input[i])
  return sorted
```

## Trace
```table


| Line            |                                             | sorted                 | value | i (outer) |  | i (inner) | value | sorted[i] | sorted.length | temp |
| --------------- | ------------------------------------------- | ---------------------- | ----- | --------- |  | --------- | ----- | --------- | ------------- | ---- |
|                 | LET sorted = New Empty Array                | [ ]                    |       |           |  |           |       |           |               |      |
|                 | sorted[0] = input[0]                        | [8]                    |       |           |  |           |       |           |               |      |
|                 |                                             |                        |       |           |  |           |       |           |               |      |
| i (outer) 0 = 1 | FOR i from 1 up to input.length             |                        |       | 1         |  |           |       |           |               |      |
|                 | Insert(sorted, input[i])                    | [8]                    | 4     | 1         |  |           |       |           |               |      |
|                 | initialize i to 0                           |                        |       |           |  | 0         |       |           |               |      |
|                 | WHILE value > sorted[i]<br>  set i to i + 1 |                        |       |           |  | 0         | 4     | 8         |               |      |
|                 |                                             |                        |       |           |  |           |       |           |               |      |
| WHILE Loop      | WHILE i < sorted.length                     |                        |       |           |  | 0         |       |           | 1             |      |
|                 | set temp to sorted[i]                       |                        |       |           |  |           |       |           |               | 8    |
|                 | set sorted[i] to value                      | [4]                    |       |           |  |           |       | 4         |               |      |
|                 | set value to temp                           |                        |       |           |  |           | 8     |           |               |      |
|                 | set i to i + 1                              |                        |       |           |  | 1         |       |           |               |      |
|                 |                                             |                        |       |           |  |           |       |           |               |      |
|                 | append value to sorted                      | [4, 8]                 |       |           |  |           |       |           |               |      |
|                 |                                             |                        |       |           |  |           |       |           |               |      |
|                 |                                             |                        |       |           |  |           |       |           |               |      |
| i (outer)  = 2  | FOR i from 1 up to input.length             |                        |       | 2         |  |           |       |           |               |      |
|                 | Insert(sorted, input[i])                    | [4, 8]                 | 23    | 2         |  |           |       |           |               |      |
|                 | initialize i to 0                           |                        |       |           |  | 0         |       |           |               |      |
|                 | WHILE value > sorted[i]                     |                        |       |           |  | 0         | 23    | 4         |               |      |
|                 | set i to i + 1                              |                        |       |           |  | 1         |       |           |               |      |
|                 | WHILE value > sorted[i]                     |                        |       |           |  | 0         | 23    | 8         |               |      |
|                 | set i to i + 1                              |                        |       |           |  | 1         |       |           |               |      |
|                 | WHILE value > sorted[i]                     |                        |       |           |  | 1         | 23    | 8         |               |      |
|                 | set i to i + 1                              |                        |       |           |  | 2         |       |           |               |      |
|                 | WHILE value > sorted[i]                     |                        |       |           |  | 2         | 23    | None      |               |      |
|                 |                                             |                        |       |           |  |           |       |           |               |      |
| WHILE Loop      | WHILE i < sorted.length                     |                        |       |           |  | 2         |       |           | 2             |      |
|                 | append value to sorted                      | [4, 8, 23]             |       |           |  |           |       |           |               |      |
|                 |                                             |                        |       |           |  |           |       |           |               |      |
| i (outer)  = 3  | FOR i from 1 up to input.length             |                        |       | 3         |  |           |       |           |               |      |
|                 | Insert(sorted, input[i])                    | [4, 8, 23]             | 42    | 3         |  |           | 42    |           |               |      |
|                 | initialize i to 0                           |                        |       |           |  | 0         |       |           |               |      |
|                 | WHILE value > sorted[i]                     |                        |       |           |  | 0         | 42    | 4         |               |      |
|                 | set i to i + 1                              |                        |       |           |  | 1         |       |           |               |      |
|                 | WHILE value > sorted[i]                     |                        |       |           |  | 1         | 42    | 8         |               |      |
|                 | set i to i + 1                              |                        |       |           |  | 2         |       |           |               |      |
|                 | WHILE value > sorted[i]                     |                        |       |           |  | 2         | 42    | 23        |               |      |
|                 | set i to i + 1                              |                        |       |           |  | 3         |       |           |               |      |
|                 | WHILE value > sorted[i]                     |                        |       |           |  | 3         | 42    | None      |               |      |
|                 |                                             |                        |       |           |  |           |       |           |               |      |
| WHILE Loop      | WHILE i < sorted.length                     |                        |       |           |  | 3         |       |           | 3             |      |
|                 | append value to sorted                      | [4, 8, 23, 42]         |       |           |  |           |       |           |               |      |
|                 |                                             |                        |       |           |  |           |       |           |               |      |
| i (outer)  = 4  | FOR i from 1 up to input.length             |                        |       | 4         |  |           |       |           |               |      |
|                 | Insert(sorted, input[i])                    | [4, 8, 23, 42]         | 16    | 4         |  |           | 16    |           |               |      |
|                 | initialize i to 0                           |                        |       |           |  | 0         |       |           |               |      |
|                 | WHILE value > sorted[i]                     |                        |       |           |  | 0         | 16    | 4         |               |      |
|                 | set i to i + 1                              |                        |       |           |  | 1         |       |           |               |      |
|                 | WHILE value > sorted[i]                     |                        |       |           |  | 1         | 16    | 8         |               |      |
|                 | set i to i + 1                              |                        |       |           |  | 2         |       |           |               |      |
|                 | WHILE value > sorted[i]                     |                        |       |           |  | 2         | 16    | 23        |               |      |
|                 |                                             |                        |       |           |  |           |       |           |               |      |
| WHILE Loop      | WHILE i < sorted.length                     |                        |       |           |  | 2         |       |           | 4             |      |
|                 | set temp to sorted[i]                       |                        |       |           |  |           |       | 23        |               | 23   |
|                 | set sorted[i] to value                      | [4, 8, 16, 42]         |       |           |  |           | 16    | 16        |               |      |
|                 | set value to temp                           |                        |       |           |  |           | 23    |           |               |      |
|                 | set i to i + 1                              |                        |       |           |  | 3         |       |           |               |      |
|                 | WHILE i < sorted.length                     |                        |       |           |  | 3         |       |           | 4             |      |
|                 | set temp to sorted[i]                       |                        |       |           |  |           |       |           |               | 42   |
|                 | set sorted[i] to value                      | [4, 8, 16, 23]         |       |           |  |           | 23    | 23        |               |      |
|                 | set value to temp                           |                        |       |           |  |           | 42    |           |               |      |
|                 | set i to i + 1                              |                        |       |           |  | 4         |       |           |               |      |
|                 | WHILE i < sorted.length                     |                        |       |           |  | 4         |       |           | 4             |      |
|                 | append value to sorted                      | [4, 8, 16, 23, 42]     |       |           |  |           |       |           |               |      |
|                 |                                             |                        |       |           |  |           |       |           |               |      |
| i (outer)  = 5  | FOR i from 1 up to input.length             |                        |       | 5         |  |           |       |           |               |      |
|                 | Insert(sorted, input[i])                    | [4, 8, 16, 23, 42]     | 15    | 3         |  |           | 15    |           |               |      |
|                 | initialize i to 0                           |                        |       |           |  | 0         |       |           |               |      |
|                 | WHILE value > sorted[i]                     |                        |       |           |  | 0         | 15    | 4         |               |      |
|                 | set i to i + 1                              |                        |       |           |  | 1         |       |           |               |      |
|                 | WHILE value > sorted[i]                     |                        |       |           |  | 1         | 15    | 8         |               |      |
|                 | set i to i + 1                              |                        |       |           |  | 2         |       |           |               |      |
|                 | WHILE value > sorted[i]                     |                        |       |           |  | 2         | 15    | 16        |               |      |
|                 |                                             |                        |       |           |  |           |       |           |               |      |
| WHILE Loop      | WHILE i < sorted.length                     |                        |       |           |  | 2         |       |           | 5             |      |
|                 | set temp to sorted[i]                       |                        |       |           |  |           |       | 16        |               | 16   |
|                 | set sorted[i] to value                      | [4, 8, 15, 23, 42]     |       |           |  |           | 15    | 15        |               |      |
|                 | set value to temp                           |                        |       |           |  |           | 16    |           |               |      |
|                 | set i to i + 1                              |                        |       |           |  | 3         |       |           |               |      |
|                 | WHILE i < sorted.length                     |                        |       |           |  | 3         |       |           | 5             |      |
|                 | set temp to sorted[i]                       |                        |       |           |  |           |       |           |               | 23   |
|                 | set sorted[i] to value                      | [4, 8, 15, 16, 42]     |       |           |  |           | 16    | 16        |               |      |
|                 | set value to temp                           |                        |       |           |  |           | 23    |           |               |      |
|                 | set i to i + 1                              |                        |       |           |  | 4         |       |           |               |      |
|                 | WHILE i < sorted.length                     |                        |       |           |  | 4         |       |           | 5             |      |
|                 | set temp to sorted[i]                       |                        |       |           |  |           |       | 42        |               | 42   |
|                 | set sorted[i] to value                      | [4, 8, 15, 16, 23]     |       |           |  |           | 23    | 23        |               |      |
|                 | set value to temp                           |                        |       |           |  |           | 42    |           |               |      |
|                 | set i to i + 1                              |                        |       |           |  | 5         |       |           |               |      |
|                 | WHILE i < sorted.length                     |                        |       |           |  | 5         |       |           | 5             |      |
|                 | append value to sorted                      | [4, 8, 15, 16, 23, 42] |       |           |  |           |       |           |               |      |
```

## Efficiency

Time: O(n!) because in worst case, for each item in the input list, we will have to iterate through the entire sorted list

Space: O(n) because we need to create 1 new data structure to hold the new list
