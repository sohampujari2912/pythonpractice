
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # 2. Traverse and Print Node Values
    def traverse(self):
        if self.head is None:
            print("Linked List is empty")
            return

        temp = self.head
    
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # 3. Insert Node at a Specific Position (1-based)
    def insert(self, data, position):
        new_node = Node(data)

        if position < 1:
            print("Invalid position")
            return

        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        count = 1

        while temp and count < position - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        temp.next = new_node

    # 4. Delete Alternate Nodes
    def delete_alternate(self):
        temp = self.head

        while temp and temp.next:
            temp.next = temp.next.next
            temp = temp.next
# Main Program
ll = SinglyLinkedList()
while True:
    print("\n1. Append")
    print("2. Traverse")
    print("3. Insert at Position")
    print("4. Delete Alternate Nodes")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter node value: "))
        ll.append(data)

    elif choice == 2:
        ll.traverse()

    elif choice == 3:
        data = int(input("Enter node value: "))
        position = int(input("Enter position (starting from 1): "))
        ll.insert(data, position)

    elif choice == 4:
        ll.delete_alternate()
        print("Alternate nodes deleted")

    elif choice == 5:
        print("Exiting program")
        break

    else:
        print("Invalid choice")
