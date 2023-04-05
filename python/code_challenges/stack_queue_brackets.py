from data_structures.stack import Stack

def multi_bracket_validation(input_string):
    if type(input_string) is not str:
        return False

    stack = Stack()

    for char in input_string:
        if open_bracket(char):
            stack.push(char)

        elif close_bracket(char):
            if stack.is_empty():
                return False

            temp_char = stack.pop()

            if not(match(char, temp_char)):
                return False

    return True

def open_bracket(char):
    if char == '[' or char == '{' or char == '(':
        return True
    else:
        return False

def close_bracket(char):
    if char == ']' or char == '}' or char == ')':
        return True
    else:
        return False

def match(char, char2):
    if char == '[' and char2 == ']':
        return True
    if char2 == '[' and char == ']':
        return True

    if char == '{' and char2 == '}':
        return True
    if char2 == '{' and char == '}':
        return True

    if char == '(' and char2 == ')':
        return True
    if char2 == '(' and char == ')':
        return True

    return False

if __name__ == "__main__":
    input_string = '1'
    print(multi_bracket_validation(input_string))


