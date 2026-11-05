

queue = []

# 1. Enqueue
def enqueue():
    value = int(input("Enter element: "))
    queue.append(value)
    print("Element inserted")

# 2. Dequeue
def dequeue():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Deleted element:", queue.pop(0))

# 3. Display
def display():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Queue:", queue)

# 4. Reverse Queue using Stack
def reverse_queue():
    stack = []

    while len(queue) > 0:
        stack.append(queue.pop(0))

    while len(stack) > 0:
        queue.append(stack.pop())

    print("Reversed queue:", queue)

# 5. Merge Two Queues
def merge_queues():
    q1 = list(map(int, input("Enter Queue 1 elements: ").split()))
    q2 = list(map(int, input("Enter Queue 2 elements: ").split()))

    merged = q1 + q2

    print("Merged Queue:", merged)

# 6. Check if Two Queues are Identical
def identical():
    q1 = list(map(int, input("Enter Queue 1 elements: ").split()))
    q2 = list(map(int, input("Enter Queue 2 elements: ").split()))

    if q1 == q2:
        print("Queues are identical")
    else:
        print("Queues are not identical")


# Main Menu
while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Reverse Queue")
    print("5. Merge Two Queues")
    print("6. Check Identical Queues")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        reverse_queue()
    elif choice == 5:
        merge_queues()
    elif choice == 6:
        identical()
    elif choice == 7:
        break
    else:
        print("Invalid choice")
