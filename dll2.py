class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    def display_backward(self):
        temp = self.head

        if temp is None:
            print("None")
            return

        while temp.next:
            temp = temp.next

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")

    def count_occurrences(self, key):
        count = 0
        temp = self.head

        while temp:
            if temp.data == key:
                count += 1
            temp = temp.next

        return count


dll = LinkedList()

dll.insert_end(10)
dll.insert_end(20)
dll.insert_end(10)
dll.insert_end(30)
dll.insert_end(10)

print("Forward Traversal:")
dll.display_forward()

print("Backward Traversal:")
dll.display_backward()

key = 10
print("Occurrences of", key, ":", dll.count_occurrences(key))