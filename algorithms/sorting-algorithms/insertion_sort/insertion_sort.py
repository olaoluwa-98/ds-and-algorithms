def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print("\t\t**INSERTION SORT**")
for x in range(5):
    print("*"*x)

# worst case scenario. array is in descending order
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] # or generate array using range(10, 0, -1)
print(f"Worst case scenario with input arr = {arr}\nResult:\t{insertion_sort(arr)}\n")

# average case scenario.
arr = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6] 
print(f"Average case scenario with input arr = {arr}\nResult:\t{insertion_sort(arr)}\n")

# best case scenario. array is already sorted
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # or generate array using range(1, 11)
print(f"Best case scenario with input arr = {arr}\nResult:\t{insertion_sort(arr)}\n")