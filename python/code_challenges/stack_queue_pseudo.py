from data_structures.stack import Stack


class PseudoQueue:
    def __init__(self):
        self.queue = Stack()

    def enqueue(self,value):
        self.queue.push(value)

    def dequeue(self):
        temp_stack = Stack()

        while self.queue.is_empty() is False:
            temp_value = self.queue.pop()
            temp_stack.push(temp_value)

        temp_output = temp_stack.pop()

        while temp_stack.is_empty() is False:
            temp_value = temp_stack.pop()
            self.queue.push(temp_value)

        return temp_output

    def peek(self):
        temp_stack = Stack()

        while self.queue.is_empty() is False:
            temp_value = self.queue.pop()
            temp_stack.push(temp_value)

        temp_output = temp_stack.peek()

        while temp_stack.is_empty() is False:
            temp_value = temp_stack.pop()
            self.queue.push(temp_value)

        return temp_output

    def is_empty(self):
        return self.queue.is_empty()

if __name__ == "__main__":
    pq = PseudoQueue()
    pq.enqueue("apples")
    pq.enqueue("bananas")

    print(pq.peek())
    # print(pq.dequeue())

    # print(pq.peek())

    # pq.enqueue("cucumbers")
    # pq.enqueue("dates")

