arr1 = list(map(int, input("Enter first sorted array: ").split()))
arr2 = list(map(int, input("Enter second sorted array: ").split()))

arr3 = arr1 + arr2
arr3.sort()

print("Merged sorted array:", arr3)