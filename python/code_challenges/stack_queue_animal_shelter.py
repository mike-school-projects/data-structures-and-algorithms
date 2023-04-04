from data_structures.queue import Queue

class AnimalShelter:
    def __init__(self):
        self.cat_queue = Queue()
        self.dog_queue = Queue()

    def enqueue(self, animal):
        if isinstance(animal,Dog):
            self.dog_queue.enqueue(animal)
            return
        elif isinstance(animal,Cat):
            self.cat_queue.enqueue(animal)
            return
        else:
            print("Not a dog or cat!")
            return

    def dequeue(self, animal):
        if animal == 'dog':
            if self.dog_is_empty():
                return "Sorry, no dogs"
            else:
                return self.dog_queue.dequeue()
        elif animal == 'cat':
            if self.cat_is_empty():
                return "Sorry, no cats"
            else:
                return self.cat_queue.dequeue()
        else:
            print("Not a dog or cat!")


    def peek(self):
        return self.queue.peek()

    def dog_is_empty(self):
        return self.dog_queue.is_empty()

    def cat_is_empty(self):
        return self.cat_queue.is_empty()

class Dog:
    def __init__(self):
        self.species = 'dog'

class Cat:
    def __init__(self):
        self.species = 'cat'

if __name__ == "__main__":
    shelter = AnimalShelter()
    cat = Dog()
    shelter.enqueue(cat)
    print(shelter.dequeue('dog'))





