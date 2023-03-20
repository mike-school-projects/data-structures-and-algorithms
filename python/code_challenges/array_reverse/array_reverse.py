def reverse_list(items):
    if type(items) is not list:
        return "null"
    else:
        new_list = []

        for x in range(len(items)):
            new_list.append(items[-(x + 1)])
            print(new_list)
        return new_list

