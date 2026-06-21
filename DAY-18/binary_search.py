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
            arr[j + 1] = temp        #array sorted

target=int(input("Enter the element to search: "))

low=0
high=n-1

while low<=high:
    mid=(low+high)//2

    if arr[mid]==target:
        print("Element fouund !!!")
        break

    elif arr[mid]>target:
        high=mid-1

    else:
        low=mid+1

else:
    print("Element not found !!!")