
# Stack Implementation

stack = []

# 1. Push
def push():
    value = int(input("Enter element: "))
    stack.append(value)
    print("Element pushed")

# 2. Pop
def pop():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Deleted element:", stack.pop())

# 3. Display
def display():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack:", stack)

# 4. Reverse String using Stack
def reverse_string():
    s = input("Enter a string: ")
    temp = []

    for ch in s:
        temp.append(ch)

    result = ""
    while len(temp) > 0:
        result += temp.pop()

    print("Reversed string:", result)

# 5. Reverse Stack using another Stack
def reverse_stack():
    temp = []

    while len(stack) > 0:
        temp.append(stack.pop())

    while len(temp) > 0:
        stack.append(temp.pop())

    print("Stack reversed:", stack)


# Main Menu
while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Reverse String")
    print("5. Reverse Stack")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        display()
    elif choice == 4:
        reverse_string()
    elif choice == 5:
        reverse_stack()
    elif choice == 6:
        break
    else:
        print("Invalid choice")
