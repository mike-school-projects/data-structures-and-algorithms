def insertion_sort(lst):
    def insert_one(value):
        nonlocal sorted
        idx = 0

        # Find index where value goes
        while value > sorted[idx]:
            idx += 1
            if idx >= len(sorted):
                # insert at the end
                sorted.append(value)
                return

        # insert value in the middle
        sorted.insert(idx, value)

    sorted = []

    # Add first number to sorted
    sorted.append(lst[0])

    for index in range(1, len(lst)):
        value = lst[index]
        insert_one(value)

    return sorted

if __name__ == "__main__":
    lst = [8, 4, 23, 42, 16, 15]
    lst = [20,18,12,8,5,-2]
    lst = [5,12,7,5,5,7]
    lst = [2,3,5,7,13,11]
    print(insertion_sort(lst))




