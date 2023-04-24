def insertion_sort_2(lst):
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

def insertion_sort(lst):
    sorted = []
    sorted.append(lst[0])

    def insert(sorted, value):
        i_inner = 0
        while i_inner < len(sorted) and value > sorted[i_inner]:
            i_inner += 1

        while i_inner < len(sorted):
            temp = sorted[i_inner]
            sorted[i_inner] = value
            value = temp
            i_inner += 1

        sorted.append(value)

        return sorted



    for i_outer in range(1, len(lst)):
        sorted = insert(sorted, lst[i_outer])



    return sorted

if __name__ == "__main__":
    lst = [8, 4, 23, 42, 16, 15]
    lst = [20,18,12,8,5,-2]
    lst = [5,12,7,5,5,7]
    lst = [2,3,5,7,13,11]
    print(insertion_sort(lst))




