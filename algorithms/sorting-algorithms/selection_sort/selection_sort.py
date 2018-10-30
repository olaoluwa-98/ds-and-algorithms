def selection_sort(arr):
    for x in range(len(arr)):
        min_index = find_min(arr, x)
        arr[x], arr[min_index] = arr[min_index], arr[x]
    
    return arr

def find_min(arr, start):
    min = arr[start]
    index = start
    for x in range(start + 1, len(arr)):
        if arr[x] < min:
            min = arr[x]
            index = x
    
    return index

print("\t\t**SELECTION SORT**")
for x in range(5):
    print("*"*x)

# worst case scenario. array is in descending order
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] # or generate array using range(10, 0, -1)
print(f"Worst case scenario with input arr = {arr}\nResult:\t{selection_sort(arr)}\n")

# average case scenario.
arr = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6] 
print(f"Average case scenario with input arr = {arr}\nResult:\t{selection_sort(arr)}\n")

# best case scenario. array is already sorted
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # or generate array using range(1, 11)
print(f"Best case scenario with input arr = {arr}\nResult:\t{selection_sort(arr)}\n")