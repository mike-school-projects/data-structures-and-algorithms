def merge_sort(input_list):
    def merge(left, right):
        output_list = list()
        left_index = 0
        right_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                output_list.append(left[left_index])
                left_index += 1
            else:
                output_list.append(right[right_index])
                right_index += 1

        if left_index == len(left):
            output_list = output_list + right[right_index:]
        else:
            output_list = output_list + left[left_index:]

        return output_list

    if len(input_list) == 1:
        return input_list

    n = len(input_list)
    output_list = list()

    if n > 1:
        mid = n // 2
        left = input_list[:mid]
        right = input_list[mid:]

        # Sort left
        left = merge_sort(left)

        # Sort right
        right = merge_sort(right)

        # Merge
        output_list = merge(left, right)

    return output_list

if __name__ == "__main__":
    lst = [8, 4, 23, 42, 16, 15]
    print(merge_sort(lst))
