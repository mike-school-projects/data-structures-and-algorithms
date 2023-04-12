from data_structures.stack import Stack
# move from list to stack

def list_to_stack(list_input):
    test = Stack()
    for value in list:
        test.push(value)

    while not(test.is_empty()):
        print(test.pop())

list = ["a", "b", "c", "d", "e", "f"]
list_to_stack(list)




