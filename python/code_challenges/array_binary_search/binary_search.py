import math
def binary_search(arr, key):
    if key not in arr:
        return -1

    start = 0
    end = len(arr) - 1
    middle = math.floor(len(arr)/2)

    while key != arr[middle]:
        if key < arr[middle]:
            end = middle - 1
            middle = math.floor( (end - start) / 2) + start
        elif key > arr[middle]:
            start = middle + 1
            middle = math.floor( (end - start) / 2) + start

    return middle

print(binary_search([-131, -82, 0, 27, 42, 68, 179, 200, 201, 202], 42))
