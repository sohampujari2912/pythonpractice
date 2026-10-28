arr = [10, 5, 20, 8, 20]

largest = float('-inf')
second = float('-inf')

for n in arr:
    if n > largest:
        second = largest
        largest = n
    elif n > second and n != largest:
        second = n

print(second)