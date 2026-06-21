# Bubble Sort Program

n = int(input("Enter the size of the array: "))

arr = []

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

# Bubble Sort
for i in range(n - 1):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]            #swapping
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

print("Sorted array:", arr)