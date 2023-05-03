class Hashtable:
    """
    Hashtable
    """

    def __init__(self, size=1024):
        self._size = int(size)
        self._buckets = size * [None]
        self.key_list = list()

    def __str__(self):
        output_list = list()
        for key in self.key_list:
            output_list.append([key, self.get(key)])
        return str(output_list)

    def set(self, key, value):
        # Hash the key, set the key and value pair in the table
        # If key already exists, replace it's value with the value argument
        self._buckets[self.hash(key)] = Node(key, value)
        self.key_list.append(key)


    def get(self, key):
        # return value associated with the key
        if key not in self.key_list:
            return None

        index = self.hash(key)
        return self._buckets[index].get_value()

    def has(self, key):
        if key in self.key_list:
            return True
        return False

    def keys(self):
        # returns collecion of keys.
        return self.key_list

    def hash(self, key):
        # returns index in the collection for that key
        index = 0
        key =str(key)

        # char hash
        for char in key:
            index += ord(char)

        # first letter hash
        index += ord(key[0]) * 7

        # last letter hash
        index += ord(key[-1]) * 7

        # length hash
        index += len(key) * 7

        # salt: multiply by 53
        index = index * 997

        # divide by length of bucket
        index = index % self._size
        return index



class Node:
    """
    Node class for Hashtable
    display method to output key/value pair
    get_value method to return value
    """
    def __init__(self, key=None, value=None):
        self.data = [key, value]

    def display(self):
        return self.data

    def get_value(self):
        return self.data[1]

if __name__ == "__main__":
    hashtable = Hashtable(1024)
    # hashtable.set(None, 30)
    # hashtable.set("ahmad", True)

    # print(hashtable._buckets)

    # print(hashtable.hash('ahmad'))
    # print(hashtable.keys())
    # print(hashtable.has('ahmad'))
    # print(hashtable.get("ahmad"))

    # node = Node()
    # print(node.display())
